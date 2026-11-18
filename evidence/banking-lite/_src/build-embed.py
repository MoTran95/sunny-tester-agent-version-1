"""Build ../bao-cao-kham-pha-v2.html từ bao-cao-kham-pha-v2.src.html.

Vì sao có bước này: khung xem trước của app Claude chỉ hiển thị file HTML <= 512 KiB và hiển thị
dạng "ảnh chụp tĩnh" (không đọc được ảnh tương đối `screenshots/...`). Nên:
  - Mỗi ảnh được nhúng 1 lần dưới dạng bản thu nhỏ WebP (base64) trong CSS (class .fNN) -> luôn hiện.
  - Khi mở file trong trình duyệt thường và thư mục `screenshots/` nằm cạnh, JS tự thay bằng ảnh gốc nét hơn.
Chạy:  python -X utf8 build-embed.py     (sửa nội dung ở *.src.html rồi chạy lại; đừng sửa file đã build)
"""
import base64, io, os, re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(HERE, 'bao-cao-kham-pha-v2.src.html')
OUT = os.path.join(ROOT, 'bao-cao-kham-pha-v2.html')
SHOTS = os.path.join(ROOT, 'screenshots')
THUMB_W, THUMB_Q = 360, 45
LIMIT = 512 * 1024

html = io.open(SRC, encoding='utf-8').read()
files = sorted(os.listdir(SHOTS))
by_num = {f.split('-')[0]: f for f in files}

# ảnh cần dùng: có trong <img> hoặc được liên kết bằng data-img
used = set(re.findall(r'<img src="screenshots/([^"]+)"', html))
for n in set(re.findall(r'data-img="(\d+)"', html)):
    used.add(by_num[n])

css_rules = []
dims = {}
for f in sorted(used):
    im = Image.open(os.path.join(SHOTS, f)).convert('RGB')
    w, h = im.size
    dims[f] = (w, h)
    th = im.resize((THUMB_W, round(h * THUMB_W / w)), Image.LANCZOS)
    buf = io.BytesIO()
    th.save(buf, 'WEBP', quality=THUMB_Q, method=6)
    b64 = base64.b64encode(buf.getvalue()).decode('ascii')
    num = f.split('-')[0]
    css_rules.append('.f%s{aspect-ratio:%d/%d;background-image:url(data:image/webp;base64,%s)}' % (num, w, h, b64))

# ---- chọn vị trí số thứ tự sao cho KHÔNG đè lên chữ/nút trong ảnh gốc ----
BADGE, BORDER = 20, 0     # khung vẽ bằng outline (nằm ngoài), không có border che chữ
PAD = 5                   # nới khung ra PAD px ảnh gốc mỗi phía để viền không đè lên chữ bên trong
# (neo ngang, lệch ngang, neo dọc, lệch dọc) theo đúng CSS .mk.pXX::after ; thứ tự = mức ưu tiên
CANDS = [
    ('pL',  'l', -28, 't', -10), ('pA',  'l', -6, 't', -28), ('pR',  'r', -28, 't', -10),
    ('pAR', 'r', -6, 't', -28),  ('pLC', 'l', -28, 'c', 0),  ('pRC', 'r', -28, 'c', 0),
    ('pBL', 'l', -6, 'b', -28),  ('pBR', 'r', -6, 'b', -28),
    ('pTL', 'l', -28, 't', -28), ('pTR', 'r', -28, 't', -28), ('pBLD', 'l', -28, 'b', -28), ('pBRD', 'r', -28, 'b', -28),
    ('pI',  'l', 4, 't', 4),
]
_gray = {}
def gray(fname):
    if fname not in _gray:
        _gray[fname] = Image.open(os.path.join(SHOTS, fname)).convert('L')
    return _gray[fname]

def ink(fname, x0, y0, x1, y1):
    """độ 'rối' của vùng (0 = nền phẳng, 1 = toàn chữ/hình): tỉ lệ điểm ảnh lệch xa màu nền chiếm ưu thế.
    Nhờ vậy nền xanh đậm của thanh tiêu đề cũng được coi là trống, còn chữ trên nền nào cũng bị tính."""
    g = gray(fname)
    x0, y0, x1, y1 = max(0, int(x0)), max(0, int(y0)), min(g.width, int(x1)), min(g.height, int(y1))
    if x1 <= x0 or y1 <= y0:
        return 0.0
    hist = g.crop((x0, y0, x1, y1)).histogram()
    total = float((x1 - x0) * (y1 - y0))
    mode = max(range(256), key=lambda i: hist[i])
    flat = sum(hist[max(0, mode - 35):min(255, mode + 35) + 1])
    return 1.0 - flat / total

def inter(a, b):
    """diện tích giao của 2 hình chữ nhật (x0,y0,x1,y1)"""
    w = min(a[2], b[2]) - max(a[0], b[0]); h = min(a[3], b[3]) - max(a[1], b[1])
    return max(0, w) * max(0, h)

def badge_rect(cand, s, box):
    cls, ah, oh, av, ov = cand
    x, y, w, h = box
    bw, bh = w * s, h * s
    left = BORDER + oh if ah == 'l' else bw - BORDER - oh - BADGE
    if av == 't':   top = BORDER + ov
    elif av == 'b': top = bh - BORDER - ov - BADGE
    else:           top = BORDER + (bh - 2 * BORDER) / 2 - BADGE / 2
    gx0, gy0 = x + left / s, y + top / s
    return (gx0, gy0, gx0 + BADGE / s, gy0 + BADGE / s)

REVIEW = []   # (tên ảnh, W, H, disp_w, [(n, neg, box, rect_badge)])

def process_figure(fname, W, H, disp_w, marks):
    """marks: list (neg, n, x, y, w, h) -> list (neg, n, cls, box) với khung đã nới và vị trí số không chồng nhau"""
    s = disp_w / float(W)
    def inflate(m, pad):
        _, _, x, y, w, h = m
        x0, y0, x1, y1 = max(0, x - pad), max(0, y - pad), min(W, x + w + pad), min(H, y + h + pad)
        return (x0, y0, x1 - x0, y1 - y0)
    boxes = [inflate(m, PAD) for m in marks]
    # khung nới mà chạm khung khác thì chỉ nới ít để không chồng lên nhau
    for i in range(len(marks)):
        for j in range(len(marks)):
            if i != j:
                a = (boxes[i][0], boxes[i][1], boxes[i][0] + boxes[i][2], boxes[i][1] + boxes[i][3])
                b = (boxes[j][0], boxes[j][1], boxes[j][0] + boxes[j][2], boxes[j][1] + boxes[j][3])
                if inter(a, b) > 0:
                    boxes[i] = inflate(marks[i], 1)
                    break
    placed, out = [], []
    for i, m in enumerate(marks):
        box = boxes[i]
        best = None
        for ci, cand in enumerate(CANDS):
            r = badge_rect(cand, s, box)
            area = (r[2] - r[0]) * (r[3] - r[1])
            score = 10.0 * ink(fname, *r) + ci * 0.004
            for j, ob in enumerate(boxes):                       # không đè lên khung của ô khác
                if j != i:
                    score += 10.0 * inter(r, (ob[0], ob[1], ob[0] + ob[2], ob[1] + ob[3])) / area
            for pr in placed:                                    # không đè lên số khác
                score += 20.0 * inter(r, pr) / area
            if best is None or score < best[0]:
                best = (score, cand[0], r)
        placed.append(best[2])
        out.append((m[0], m[1], best[1], box))
    REVIEW.append((fname, W, H, disp_w, [(o[1], o[0], o[3], placed[k]) for k, o in enumerate(out)]))
    return out

MK = re.compile(r'<i class="mk( neg)?" data-n="(\d+)" style="--x:(\d+);--y:(\d+);--w:(\d+);--h:(\d+)"></i>')
def fig_sub(m):
    head, style, body = m.group(1), m.group(2), m.group(3)
    mm = re.search(r'<img src="screenshots/([^"]+)"', body)
    if not mm:
        return m.group(0)
    fname = mm.group(1)
    W = int(re.search(r'--W:(\d+)', style).group(1)); H = int(re.search(r'--H:(\d+)', style).group(1))
    wm = re.search(r'(?<![-\w])width:(\d+)px', style)
    disp_w = int(wm.group(1)) if wm else 230      # khung ảnh trong thẻ điểm mơ hồ rộng 230px (nhỏ nhất, an toàn)
    marks = [(k.group(1) or '', k.group(2), *[int(k.group(i)) for i in (3, 4, 5, 6)]) for k in MK.finditer(body)]
    res = iter(process_figure(fname, W, H, disp_w, marks))
    def mk_sub(k):
        neg, n, cls, box = next(res)
        return '<i class="mk%s %s" data-n="%s" style="--x:%d;--y:%d;--w:%d;--h:%d"></i>' % (neg, cls, n, *box)
    return head + MK.sub(mk_sub, body) + '</figure>'
html, n_fig = re.subn(r'(<figure class="shot" style="([^"]*)">)(.*?)</figure>', fig_sub, html, flags=re.S)

def img_sub(m):
    f, rest = m.group(1), m.group(2)
    alt = re.search(r'alt="([^"]*)"', rest)
    return '<span class="im f%s" role="img" aria-label="%s" data-full="screenshots/%s"></span>' % (
        f.split('-')[0], alt.group(1) if alt else '', f)
html, n_img = re.subn(r'<img src="screenshots/([^"]+)"([^>]*)>', img_sub, html)

# CSS
base_css = '.im{display:block;width:100%;background-color:#fff;background-size:100% 100%;background-repeat:no-repeat;border-radius:9px}\n' \
           'a.ev{cursor:pointer;color:var(--brand);text-decoration:underline;white-space:nowrap}\n'
html = html.replace('</style>', base_css + '\n'.join(css_rules) + '\n</style>', 1)

# JS
new_js = '''<script>
(function(){
  /* nếu ảnh gốc nằm cạnh (mở bằng trình duyệt thường) thì thay bản thu nhỏ bằng ảnh nét */
  function upgrade(root){
    root.querySelectorAll(".im[data-full]").forEach(function(el){
      var full=el.getAttribute("data-full"), i=new Image();
      i.onload=function(){el.style.backgroundImage='url("'+full+'")';};
      i.src=full;
    });
  }
  upgrade(document);
  function open(figure){
    var box=document.createElement("div");box.className="lightbox";
    figure.style.width="";box.appendChild(figure);document.body.appendChild(box);
  }
  function close(){var lb=document.querySelector(".lightbox");if(lb)lb.remove();}
  /* thanh điều hướng: bấm tab thì cuộn tới đúng mục (chạy cả khi trang mở dạng ảnh chụp tĩnh, nơi #anchor mặc định không hoạt động) */
  var nav=document.querySelector("nav.top");
  var links=nav?[].slice.call(nav.querySelectorAll('a[href^="#"]')):[];
  function targetOf(a){return document.getElementById(a.getAttribute("href").slice(1));}
  function goTo(el){
    var off=(nav?nav.getBoundingClientRect().height:0)+6;
    var y=el.getBoundingClientRect().top+(window.pageYOffset||document.documentElement.scrollTop)-off;
    try{window.scrollTo({top:y,behavior:"smooth"});}catch(err){window.scrollTo(0,y);}
  }
  links.forEach(function(a){
    a.addEventListener("click",function(e){
      var t=targetOf(a);
      if(t){e.preventDefault();goTo(t);setActive(a);}
    });
  });
  function setActive(cur){links.forEach(function(a){a.classList.toggle("on",a===cur);});}
  function onScroll(){
    var off=(nav?nav.getBoundingClientRect().height:0)+40, cur=links[0];
    links.forEach(function(a){var t=targetOf(a);if(t&&t.getBoundingClientRect().top<=off)cur=a;});
    setActive(cur);
  }
  window.addEventListener("scroll",onScroll,{passive:true});onScroll();
  var FILES={};
  document.querySelectorAll(".im[data-full]").forEach(function(el){
    var m=el.className.match(/\\bf(\\d+)\\b/); if(m)FILES[m[1]]=el.getAttribute("data-full");
  });
  document.addEventListener("click",function(e){
    if(e.target.closest(".lightbox")){close();return;}
    var a=e.target.closest("a.ev[data-img]");
    if(a){
      e.preventDefault();
      var n=a.getAttribute("data-img");
      var fig=document.createElement("figure");fig.className="shot";
      var w=document.createElement("div");w.className="wrap";
      var s=document.createElement("span");s.className="im f"+n;s.setAttribute("role","img");
      s.setAttribute("aria-label","Ảnh "+n);
      if(FILES[n])s.setAttribute("data-full",FILES[n]); else s.setAttribute("data-full","screenshots/"+n);
      w.appendChild(s);fig.appendChild(w);
      var cap=document.createElement("figcaption");cap.textContent="Ảnh "+n+" — bấm để đóng";
      fig.appendChild(cap);open(fig);upgrade(fig);
      return;
    }
    var w2=e.target.closest("figure.shot .wrap");
    if(w2){var c=w2.parentNode.cloneNode(true);open(c);upgrade(c);}
  });
  document.addEventListener("keydown",function(e){if(e.key==="Escape")close();});
})();
</script>'''
html, n_js = re.subn(r'<script>.*?</script>', lambda m: new_js, html, count=1, flags=re.S)

# thu gọn: bỏ chú thích HTML, bỏ thụt đầu dòng và dòng trống
html = re.sub(r'<!--.*?-->', '', html, flags=re.S)
html = '\n'.join(l.lstrip() for l in html.split('\n') if l.strip())

io.open(OUT, 'w', encoding='utf-8', newline='').write(html)
size = os.path.getsize(OUT)
print('span.im:', n_img, '| images:', len(used), '| js:', n_js, '| size: %d bytes (%.1f%% of 512KiB limit)' % (size, size * 100 / LIMIT))
if size > LIMIT:
    print('!!! VƯỢT GIỚI HẠN 512 KiB của khung xem trước')


# ---- chế độ kiểm tra: python build-embed.py --review <thư_mục>  -> xuất tranh ghép ảnh có khung/số để soát bằng mắt ----
import sys
if '--review' in sys.argv:
    from PIL import ImageDraw
    outdir = sys.argv[sys.argv.index('--review') + 1]
    os.makedirs(outdir, exist_ok=True)
    tiles = []
    for idx, (fname, W, H, disp_w, marks) in enumerate(REVIEW):
        im = Image.open(os.path.join(SHOTS, fname)).convert('RGB')
        d = ImageDraw.Draw(im, 'RGBA')
        for n, neg, (x, y, w, h), r in marks:
            col = (217, 119, 6, 255) if neg else (225, 29, 72, 255)
            d.rectangle([x, y, x + w, y + h], outline=col, width=3)
            d.ellipse([r[0], r[1], r[2], r[3]], fill=col)
            d.text((r[0] + (r[2] - r[0]) / 2 - 3, r[1] + (r[3] - r[1]) / 2 - 6), str(n), fill=(255, 255, 255, 255))
        d.rectangle([0, 0, 200, 16], fill=(255, 255, 255, 255))
        d.text((3, 2), '#%d %s' % (idx, fname[:24]), fill=(0, 0, 0, 255))
        tiles.append(im.resize((int(im.width * 0.62), int(im.height * 0.62))))
    per = 4
    for si in range(0, len(tiles), per):
        grp = tiles[si:si + per]
        sheet = Image.new('RGB', (sum(t.width for t in grp) + 8 * len(grp), max(t.height for t in grp)), (200, 200, 200))
        xx = 0
        for t in grp:
            sheet.paste(t, (xx, 0)); xx += t.width + 8
        sheet.save(os.path.join(outdir, 'sheet-%02d.png' % (si // per)))
    print('review sheets:', (len(tiles) + per - 1) // per)
