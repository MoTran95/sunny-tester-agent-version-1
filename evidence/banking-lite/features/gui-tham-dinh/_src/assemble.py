"""Ghép body.html + 3 sơ đồ SVG + CSS mẫu của skill -> gui-tham-dinh.src.html
Chạy:  python -X utf8 assemble.py   (xong chạy build-embed.py của skill, xem README trong bộ nhớ)
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
TEMPLATE = os.path.join(REPO, '.claude', 'skills', 'feature-exploration-report', 'assets', 'report-template.src.html')

tpl = io.open(TEMPLATE, encoding='utf-8').read()
head = tpl[:tpl.index('<body>')].replace('{{TÊN_BÁO_CÁO}}', 'Báo cáo khám phá — Gửi thẩm định')
body = io.open(os.path.join(HERE, 'body.html'), encoding='utf-8').read()

# ---------------- SVG 1: sơ đồ tổng quan ----------------
def box(x, y, w, h, fill, stroke, title, lines, tcol):
    s = '<rect x="%d" y="%d" width="%d" height="%d" rx="14" fill="%s" stroke="%s" stroke-width="2.5"/>' % (x, y, w, h, fill, stroke)
    cx = x + w // 2
    s += '<text x="%d" y="%d" text-anchor="middle" font-size="20" font-weight="700" fill="%s">%s</text>' % (cx, y + 32, tcol, title)
    for i, (txt, bold) in enumerate(lines):
        s += '<text x="%d" y="%d" text-anchor="middle" font-size="13" %s fill="#333">%s</text>' % (
            cx, y + 56 + i * 19, 'font-weight="600"' if bold else '', txt)
    return s

def badge(cx, cy, n, col):
    return ('<g class="noh"><circle cx="%d" cy="%d" r="11" fill="%s"/>'
            '<text x="%d" y="%.1f" text-anchor="middle" font-size="12.5" font-weight="700" fill="#fff" stroke="none">%s</text></g>') % (cx, cy, col, cx, cy + 4.5, n)

o = ['<svg viewBox="0 0 1100 520" role="img" aria-label="Sơ đồ tổng quan Gửi thẩm định">',
     '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#334"/></marker>'
     '<marker id="ahd" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#777"/></marker></defs>']
o.append(box(10, 50, 230, 190, '#e3f4ed', '#177a5c', 'P100001', [('Chuyên viên khách hàng', 1), ('Hoàn thiện bước 1–5,', 0), ('kiểm tra điều kiện,', 0), ('bấm Gửi thẩm định', 0)], '#177a5c'))
o.append(box(10, 340, 230, 130, '#e4eefa', '#2b6cb0', 'P300001', [('Chuyên viên thẩm định', 1), ('tín dụng', 1), ('Nhận hồ sơ để quyết định', 0)], '#2b6cb0'))
o.append('<rect x="450" y="30" width="230" height="460" rx="16" fill="#fff" stroke="#0b5d4e" stroke-width="3"/>')
o.append('<text x="565" y="66" text-anchor="middle" font-size="21" font-weight="700" fill="#0b5d4e">Banking Lite</text>')
o.append('<text x="565" y="88" text-anchor="middle" font-size="14" fill="#555">Bước 6 “Kiểm tra và gửi”</text>')
for i, t in enumerate(['▸ Kiểm tra 12 điều kiện gửi', '▸ Nút “Gửi thẩm định”:', '    bật hoặc vô hiệu hóa', '▸ Lấy CIC, thẩm định chính thức', '▸ Trạng thái: Nháp → Đã gửi', '▸ Hồ sơ Đã gửi bị khóa', '▸ Bước 7: Đang chờ xử lý']):
    o.append('<text x="470" y="%d" font-size="13.5" fill="#333">%s</text>' % (130 + i * 28, t))
o.append(box(880, 190, 210, 110, '#efe9fb', '#6b46c1', 'CIC', [('thông tin tín dụng', 0)], '#6b46c1'))
# mũi tên: (x1,y1,x2,y2,dashed,label,lx)
arrows = [
    (240, 90, 448, 90, False, 'Hoàn thiện bước 1–5', 1, '#177a5c', 258, 85),
    (448, 130, 242, 130, True, 'Mục còn thiếu / sẵn sàng', 2, '#4a5568', 252, 125),
    (240, 170, 448, 170, False, 'Bấm Gửi thẩm định', 3, '#177a5c', 258, 165),
    (680, 220, 878, 220, False, 'Lấy báo cáo tín dụng', 4, '#6b46c1', 722, 215),
    (878, 262, 682, 262, True, '“Nhóm nợ …”', 5, '#6b46c1', 700, 257),
    (448, 210, 242, 210, True, 'Đã gửi, hồ sơ bị khóa', 6, '#4a5568', 252, 205),
    (448, 400, 242, 400, False, 'Chờ quyết định', 7, '#2b6cb0', 252, 395),
]
for x1, y1, x2, y2, dashed, label, n, col, lx, ly in arrows:
    o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"%s marker-end="url(#%s)"/>' % (
        x1, y1, x2, y2, '#777' if dashed else '#334', ' stroke-dasharray="6 4"' if dashed else '', 'ahd' if dashed else 'ah'))
    o.append('<text x="%d" y="%d" font-size="12.5" fill="%s">%s</text>' % (lx, ly, '#555' if dashed else '#222', label))
    bx = x1 + (16 if x2 > x1 else -16)
    o.append(badge(bx, y1, n, col))
o.append('<text x="565" y="515" text-anchor="middle" font-size="12" fill="#555" stroke="none">Bước 7 đã thấy ở HL-000019 (báo cáo v2); HL-000022 chưa kiểm tra bằng P300001.</text>')
o.append('</svg>')
svg_overview = '\n'.join(o)

# ---------------- SVG 2: sơ đồ tuần tự ----------------
X = dict(RM=110, S=400, CIC=700, AP=980)
parts = [('RM', 'P100001', 'Chuyên viên KH', '#177a5c', 150), ('S', 'Banking Lite', 'hệ thống', '#4a5568', 160),
         ('CIC', 'CIC', None, '#6b46c1', 110), ('AP', 'P300001', 'Thẩm định tín dụng', '#2b6cb0', 160)]
col = dict(RM='#177a5c', S='#4a5568', CIC='#6b46c1', AP='#2b6cb0')
msgs = [
    (1, 'RM', 'S', ['Mở bước “Kiểm tra và gửi”'], False),
    (2, 'S', 'RM', ['Mục còn thiếu (nút bị vô hiệu hóa)', 'hoặc “Hồ sơ đã đầy đủ và sẵn sàng gửi.”'], True),
    (3, 'RM', 'S', ['Bấm “Gửi thẩm định”'], False),
    (4, 'S', 'CIC', ['Lấy báo cáo tín dụng'], False),
    (5, 'CIC', 'S', ['“A1: nhóm nợ 1, trả nợ 0 VND”'], True),
    (6, 'S', 'RM', ['Đã gửi (khóa) · Thẩm định: Phê duyệt'], True),
    (7, 'S', 'AP', ['Hồ sơ vào “Chờ quyết định”'], False),
]
H = 560
q = ['<svg viewBox="0 0 1100 %d" role="img" aria-label="Sơ đồ tuần tự Gửi thẩm định">' % H,
     '<defs><marker id="a2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#334"/></marker>'
     '<marker id="a2d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#777"/></marker></defs>',
     '<g stroke="#b9c4c0" stroke-width="1.5" stroke-dasharray="5 5">']
for k, x in X.items():
    q.append('<line x1="%d" y1="64" x2="%d" y2="%d"/>' % (x, x, H - 20))
q.append('</g><g font-size="14" font-weight="700" text-anchor="middle" fill="#fff" class="noh">')
for k, t, sub, c, w in parts:
    x = X[k]
    q.append('<rect x="%d" y="14" width="%d" height="48" rx="10" fill="%s"/>' % (x - w // 2, w, c))
    if sub:
        q.append('<text x="%d" y="34" stroke="none">%s</text><text x="%d" y="52" font-size="11.5" font-weight="500" stroke="none">%s</text>' % (x, t, x, sub))
    else:
        q.append('<text x="%d" y="43" stroke="none">%s</text>' % (x, t))
q.append('</g>')
y = 118
badges = []
for n, a, b, lines, dashed in msgs:
    xa, xb = X[a], X[b]
    d = 1 if xb > xa else -1
    q.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="2"%s marker-end="url(#%s)"/>' % (
        xa, y, xb - d * 2, y, '#777' if dashed else '#334', ' stroke-dasharray="6 4"' if dashed else '', 'a2d' if dashed else 'a2'))
    cx = (xa + xb) / 2 + 10 * d
    fill = '#555' if dashed else '#222'
    if len(lines) == 1:
        q.append('<text x="%d" y="%d" text-anchor="middle" font-size="13" fill="%s">%s</text>' % (cx, y - 7, fill, lines[0]))
    else:
        q.append('<text x="%d" y="%d" text-anchor="middle" font-size="13" fill="%s">%s</text>' % (cx, y - 23, fill, lines[0]))
        q.append('<text x="%d" y="%d" text-anchor="middle" font-size="13" fill="%s">%s</text>' % (cx, y - 8, fill, lines[1]))
    badges.append((n, xa + d * 17, y, col[a]))
    y += 62 if len(lines) == 2 else 56
q.append('<rect x="150" y="%d" width="700" height="34" rx="8" fill="#fff6e0" stroke="#f0c36d" stroke-width="1.5"/>' % (y - 8))
q.append('<text x="500" y="%d" text-anchor="middle" font-size="13" fill="#6b4a00" stroke="none">Bước 7 đã thấy ở HL-000019 (báo cáo v2). HL-000022 chưa kiểm tra bằng P300001.</text>' % (y + 14))
q.append('<g font-size="12.5" font-weight="700" text-anchor="middle" fill="#fff" class="noh">')
for n, bx, by, c in badges:
    q.append('<circle cx="%d" cy="%d" r="11" fill="%s"/><text x="%d" y="%.1f" stroke="none">%s</text>' % (bx, by, c, bx, by + 4.5, n))
q.append('</g></svg>')
svg_seq = '\n'.join(q)

# ---------------- SVG 3: trạng thái ----------------
st = '''<svg viewBox="0 0 1000 380" role="img" aria-label="Trạng thái hồ sơ liên quan Gửi thẩm định">
<defs><marker id="a3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#334"/></marker>
<marker id="a3d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#999"/></marker></defs>
<g class="noh" font-size="17" font-weight="700" text-anchor="middle">
<rect x="20" y="80" width="140" height="56" rx="12" fill="#eef1f4" stroke="#6b7a86" stroke-width="2.5"/><text x="90" y="115" fill="#33414d" stroke="none">Nháp</text>
<rect x="330" y="150" width="150" height="56" rx="12" fill="#e4eefa" stroke="#2b6cb0" stroke-width="2.5"/><text x="405" y="185" fill="#2b6cb0" stroke="none">Đã gửi</text>
<rect x="20" y="250" width="160" height="56" rx="12" fill="#fff0cf" stroke="#b7791f" stroke-width="2.5"/><text x="100" y="285" fill="#8a5a00" stroke="none">Bị trả lại</text>
</g>
<rect x="640" y="125" width="330" height="106" rx="12" fill="#f4f4f4" stroke="#999" stroke-width="2" stroke-dasharray="6 4"/>
<text x="805" y="155" text-anchor="middle" font-size="14" font-weight="700" fill="#555" stroke="none">Quyết định của P300001</text>
<text x="805" y="178" text-anchor="middle" font-size="13" fill="#555" stroke="none">Phê duyệt / Từ chối / Trả lại</text>
<text x="805" y="200" text-anchor="middle" font-size="12" fill="#777" stroke="none">(ngoài phạm vi feature này, xem báo cáo v2)</text>
<g stroke="#334" stroke-width="2.2" fill="none" marker-end="url(#a3)">
<line x1="160" y1="110" x2="328" y2="165"/>
<line x1="180" y1="278" x2="330" y2="200"/>
</g>
<line x1="482" y1="178" x2="638" y2="178" stroke="#999" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#a3d)"/>
<g font-size="13" fill="#222">
<text x="214" y="118" text-anchor="middle">Gửi thẩm định</text>
<text x="236" y="262" text-anchor="middle">Gửi thẩm định</text>
<text x="560" y="168" text-anchor="middle" fill="#777">P300001</text>
</g>
<g class="noh" font-size="12" font-weight="700" fill="#fff" text-anchor="middle">
<circle cx="244" cy="138" r="11" fill="#334"/><text x="244" y="142.5" stroke="none">1</text>
<circle cx="250" cy="248" r="11" fill="#334"/><text x="250" y="252.5" stroke="none">2</text>
</g>
<text x="20" y="360" font-size="12.5" fill="#555" stroke="none">Điều kiện bấm được: đủ mục theo danh sách (ảnh 07). Sau khi Đã gửi, hồ sơ bị khóa (ảnh 05).</text>
</svg>'''

body = body.replace('{{SVG_OVERVIEW}}', svg_overview).replace('{{SVG_SEQ}}', svg_seq).replace('{{SVG_STATE}}', st)
html = head + '<body>\n' + body + '\n<script>/* build-embed.py sẽ thay khối này */</script>\n</body>\n</html>\n'
out = os.path.join(HERE, 'gui-tham-dinh.src.html')
io.open(out, 'w', encoding='utf-8', newline='').write(html)
print('written', out, len(html))
