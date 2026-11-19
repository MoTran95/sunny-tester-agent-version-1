"""Trang HTML dễ xem cho tài liệu markdown của dự án (SRS, bảng soát requirement, câu hỏi BA, checklist, test case, truy vết…)
và trang tổng `testing/<dự-án>/index.html` link tới mọi tài liệu, kết quả chạy và bug.

- File md vẫn là bản gốc (AI đọc md). HTML sinh ra cạnh file md, đừng sửa tay: chạy `python -X utf8 scripts/build_docs.py`.
- Không dùng AI để sinh: chỉ là chương trình đổi md sang HTML và đọc số liệu từ file có sẵn, nên xem hay cập nhật đều 0 token.
- Bảng rộng giữ cố định hai cột đầu, có thanh cuộn ngang luôn hiện; có ô lọc dòng; trạng thái (Đạt, Không đạt…) hiện thành huy hiệu màu.
"""
import html
import os
import re
import time
from pathlib import Path

from . import config
from . import report as report_mod

GENERATOR = '<meta name="generator" content="build_docs.py">'
_CELL_SPLIT = re.compile(r"(?<!\\)\|")
STATUSES = {"Đạt": "ok", "Không đạt": "bad", "Bị chặn": "warn", "Bỏ qua": "gray", "Chưa chạy": "gray", "Đạt kèm ý phụ sai": "warn", "Đạt kèm lỗi đã biết": "warn"}

DOC_LABELS = [("srs", "SRS"), ("bang-soat-requirement", "Bảng soát requirement"), ("phan-tich-requirement", "Phân tích requirement"),
              ("cau-hoi-cho-ba", "Câu hỏi cho BA"), ("checklist", "Checklist"), ("test-case", "Test case"), ("truy-vet", "Truy vết"),
              ("ket-qua-test-case", "Kết quả chạy")]


# ---------------------------------------------------------------- tìm tài liệu
def collect_sources(project):
    """Danh sách file md cần đổi sang HTML của một dự án."""
    root = config.ROOT
    found = []
    for d in (root / "srs" / project,):
        found += sorted(d.glob("*.md"))
    t = root / "testing" / project
    found += [f for f in sorted(t.glob("*.md")) if f.name != "smoke-ket-qua.md"]
    for sub in sorted(x for x in t.iterdir() if x.is_dir()):
        found += [f for f in sorted(sub.glob("*.md")) if f.name != "ket-qua-test-case.md"]
    e = root / "evidence" / project
    for f in sorted(e.rglob("*.md")):
        if not {"_src", "screenshots", "chay-test"} & set(f.relative_to(e).parts):
            found.append(f)
    for name in ("chay-test-tu-dong.md",):
        if (root / "docs" / name).exists():
            found.append(root / "docs" / name)
    return found


# ---------------------------------------------------------------- markdown → HTML
def _slug(text):
    s = re.sub(r"[^\w\- ]", "", re.sub(r"[`*_\[\]()]", "", text).lower(), flags=re.U).strip().replace(" ", "-")
    return s or "muc"


def _fix_link(url, src, converted):
    if re.match(r"^(https?:|mailto:|#)", url):
        return url
    path, sep, frag = url.partition("#")
    if path.endswith(".md"):
        target = (src.parent / path).resolve()
        if target in converted:
            return path[:-3] + ".html" + (sep + frag if sep else "")
    return url


def render_inline(text, src, converted):
    holders = []

    def hold(h):
        holders.append(h)
        return f"\x00{len(holders) - 1}\x00"

    text = re.sub(r"`([^`]+)`", lambda m: hold("<code>" + html.escape(m.group(1), quote=False) + "</code>"), text)
    text = re.sub(r"<br\s*/?>", lambda m: hold("<br>"), text, flags=re.I)
    text = re.sub(r'<a id="?([\w.-]+)"?></a>', lambda m: hold(f'<a id="{m.group(1)}"></a>'), text)
    text = html.escape(text, quote=False)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)",
                  lambda m: hold(f'<a href="{_fix_link(m.group(2), src, converted).replace(chr(34), "%22")}">{m.group(1)}</a>'), text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*\s][^*]*?)\*(?![*\w])", r"<em>\1</em>", text)
    text = re.sub(r"(?<![=\"\w/>])(https?://[^\s<)\x00]+[^\s<).,;\x00])", lambda m: f'<a href="{m.group(1)}">{m.group(1)}</a>', text)
    while "\x00" in text:
        text = re.sub(r"\x00(\d+)\x00", lambda m: holders[int(m.group(1))], text)
    return text


def _cell_html(cell, src, converted):
    plain = re.sub(r"`", "", cell).strip()
    if plain in STATUSES:
        return f'<span class="badge {STATUSES[plain]}">{html.escape(plain)}</span>'
    return render_inline(cell.strip(), src, converted) or "—"


def _split_row(line):
    cells = _CELL_SPLIT.split(line.strip())
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1].strip() == "":
        cells = cells[:-1]
    return [c.replace("\\|", "|") for c in cells]


def _render_table(rows, src, converted):
    header, body = rows[0], rows[2:]
    n = len(header)
    wide = n >= 6
    empty_head = all(not h.strip() for h in header)
    out = ['<div class="khu-bang"><div class="wrap' + (" lon" if wide else "") + '"><table>']
    if not empty_head:
        out.append("<thead><tr>" + "".join(f"<th>{render_inline(h.strip(), src, converted)}</th>" for h in header) + "</tr></thead>")
    out.append("<tbody>")
    for r in body:
        cells = (r + [""] * n)[:n]
        out.append("<tr>" + "".join(f'<td class="cot-nho">{_cell_html(c, src, converted)}</td>' if wide else f"<td>{_cell_html(c, src, converted)}</td>" for c in cells) + "</tr>")
    out.append('</tbody></table></div><div class="thanh-keo"><div></div></div></div>')
    return "".join(out)


_LIST_RE = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")


def _render_list(items, src, converted):
    """items: [(indent, kind, text)] → HTML lồng nhau theo độ thụt."""
    out, stack = [], []
    for indent, kind, text in items:
        while stack and indent < stack[-1][0]:
            out.append(f"</li></{stack.pop()[1]}>")
        tag = "ol" if kind[0].isdigit() else "ul"
        if stack and indent == stack[-1][0] and stack[-1][1] != tag:
            out.append(f"</li></{stack.pop()[1]}>")   # đổi từ danh sách gạch đầu dòng sang đánh số (hoặc ngược lại): mở danh sách mới
        if stack and indent == stack[-1][0]:
            out.append("</li>")
        elif not stack or indent > stack[-1][0]:
            stack.append((indent, tag))
            out.append(f"<{tag}>")
        out.append(f"<li>{render_inline(text, src, converted)}")
    while stack:
        out.append(f"</li></{stack.pop()[1]}>")
    return "".join(out)


def render_markdown(md, src, converted):
    """→ (html thân trang, tiêu đề, [(mức, id, chữ)] của các đề mục)."""
    lines = md.splitlines()
    out, heads, used, title = [], [], set(), ""
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("<!--"):
            while i < len(lines) and "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        m = re.match(r'^<a id="?([\w.-]+)"?></a>\s*$', stripped)
        if m:
            out.append(f'<a id="{m.group(1)}"></a>')
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level, text = len(m.group(1)), m.group(2).strip()
            sid = base = _slug(text)
            n = 2
            while sid in used:
                sid, n = f"{base}-{n}", n + 1
            used.add(sid)
            if level == 1 and not title:
                title = re.sub(r"[`*]", "", text)
            if 2 <= level <= 3:
                heads.append((level, sid, re.sub(r"[`*]", "", text)))
            out.append(f'<h{level} id="{sid}">{render_inline(text, src, converted)}</h{level}>')
            i += 1
            continue
        if re.match(r"^-{3,}$", stripped):
            out.append("<hr>")
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:|-]+\|?\s*$", lines[i + 1]):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(_split_row(lines[i]))
                i += 1
            out.append(_render_table(rows, src, converted))
            continue
        if stripped.startswith(">"):
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote>" + "<br>".join(render_inline(b, src, converted) for b in block if b) + "</blockquote>")
            continue
        if _LIST_RE.match(line):
            items = []
            while i < len(lines):
                cur = lines[i].rstrip()
                lm = _LIST_RE.match(cur)
                if lm:
                    items.append([len(lm.group(1).replace("\t", "    ")), lm.group(2), lm.group(3)])
                elif cur.strip() and cur.startswith(" ") and items:
                    items[-1][2] += " " + cur.strip()
                elif not cur.strip():
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and _LIST_RE.match(lines[j].rstrip()):
                        i = j
                        continue
                    break
                else:
                    break
                i += 1
            out.append(_render_list([tuple(x) for x in items], src, converted))
            continue
        para = [stripped]
        i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,4}\s|\||>|-{3,}$|<!--)", lines[i].strip()) and not _LIST_RE.match(lines[i].rstrip()):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{render_inline(' '.join(para), src, converted)}</p>")
    return "".join(out), title, heads


# ---------------------------------------------------------------- khung trang
_CSS_DOC = """
main.rong{max-width:1840px}
.doc h1{text-align:left;font-size:34px;margin:6px 0 14px}.doc h2{margin:34px 0 10px;padding-top:6px;border-top:1px solid var(--line)}.doc h3{font:700 18px/1.3 Fraunces,Georgia,serif;color:var(--text);margin:24px 0 8px}
.doc p,.doc ul,.doc ol,.doc blockquote{max-width:1100px}.doc ul,.doc ol{padding-left:24px}.doc li{margin:4px 0}
.doc blockquote{margin:14px 0;padding:10px 16px;border-left:4px solid var(--amber);background:var(--amberbg);color:var(--amberfg);border-radius:0 10px 10px 0}
.doc hr{border:0;border-top:1px solid var(--line);margin:26px 0}
.khu-bang{margin:12px 0 18px}
.doc table{min-width:0}.doc .lon table{min-width:1280px}
.nav-doc{display:flex;flex-wrap:wrap;gap:6px 8px;margin:0 0 18px;font-size:14px}.nav-doc a,.nav-doc b{padding:5px 12px;border-radius:999px;border:1px solid var(--line);background:var(--card);text-decoration:none;color:var(--body)}
.nav-doc b{background:var(--coral);border-color:var(--coral);color:#fff}.nav-doc a:hover{border-color:var(--coral);color:var(--coral)}
.muc-luc{margin:0 0 16px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 18px}.muc-luc summary{cursor:pointer;font-weight:700}
.muc-luc ul{margin:8px 0 4px;padding-left:20px;columns:2;column-gap:36px}.muc-luc li{margin:3px 0;break-inside:avoid}
.loc{display:flex;gap:10px;align-items:center;margin:0 0 16px}.loc input{flex:1;max-width:520px;padding:9px 14px;border:1px solid var(--line);border-radius:999px;background:var(--card);color:var(--body);font:inherit}
.loc span{color:var(--muted);font-size:13px}
tr.an{display:none}
.the{display:grid;grid-template-columns:repeat(auto-fill,minmax(420px,1fr));gap:16px;margin:12px 0 8px}
.the .card h3{margin:0 0 4px;font:700 20px/1.3 Fraunces,Georgia,serif;color:var(--text)}
.the .card h4{margin:14px 0 6px;font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.links{display:flex;flex-wrap:wrap;gap:6px}.links a{padding:4px 11px;border-radius:999px;border:1px solid var(--line);background:var(--bg);text-decoration:none;font-size:13.5px}.links a:hover{border-color:var(--coral)}
.links .none{padding:4px 11px;border-radius:999px;border:1px dashed var(--line);color:var(--muted);font-size:13.5px}
.bar-tt{display:flex;height:14px;border-radius:7px;overflow:hidden;border:1px solid var(--line);background:var(--graybg)}.bar-tt i{display:block;height:100%}
.bar-tt .s-ok{background:var(--green)}.bar-tt .s-bad{background:var(--coral)}.bar-tt .s-warn{background:var(--amber)}.bar-tt .s-gray{background:var(--graybg)}
.chu-thich{display:flex;flex-wrap:wrap;gap:4px 14px;margin:6px 0 0;font-size:13px;color:var(--muted)}
.bugs{margin:4px 0 0;padding:0;list-style:none}.bugs li{margin:5px 0;font-size:14px}
.so-lieu{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:0 0 6px}.so-lieu div{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px}.so-lieu b{display:block;font:700 26px/1.1 Fraunces,Georgia,serif;color:var(--text)}.so-lieu span{font-size:13px;color:var(--muted)}
@media (max-width:700px){.the{grid-template-columns:1fr}.muc-luc ul{columns:1}}
"""

_JS_FILTER = ("document.addEventListener('DOMContentLoaded',function(){var q=document.getElementById('loc-q');if(!q)return;var c=document.getElementById('loc-n');"
              "q.addEventListener('input',function(){var v=q.value.trim().toLowerCase(),n=0,t=0;document.querySelectorAll('.doc tbody tr').forEach(function(r){t++;"
              "var ok=!v||r.textContent.toLowerCase().indexOf(v)>=0;r.classList.toggle('an',!ok);if(ok)n++});c.textContent=v?(n+' / '+t+' dòng'):''})});")


def _page(title, body, nav_html="", toc_html="", has_table=False, back=None, extra_head=""):
    e = html.escape
    logo = report_mod._logo_data_uri()
    flt = ('<div class="loc"><input id="loc-q" type="search" placeholder="Lọc dòng trong các bảng (gõ chữ hoặc mã)…"><span id="loc-n"></span></div>' if has_table else "")
    return ('<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">' + GENERATOR +
            f"<title>{e(title)}</title>"
            '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,700;1,9..144,700&family=Hanken+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">'
            f"<style>{report_mod._CSS}{_CSS_DOC}</style><script>{report_mod._JS_THEME}{report_mod._JS_DRAG_SCROLL}{_JS_FILTER}</script></head><body>"
            '<button id="theme" class="theme" type="button">Chế độ tối</button><main class="rong doc">'
            + (f'<div class="brand"><img src="{logo}" alt="Sunny Nhận Ra"></div>' if logo else "") + nav_html + toc_html + flt + body +
            '<p class="small" style="margin-top:36px">Trang tự sinh từ file markdown bằng <code>scripts/build_docs.py</code>; không sửa tay, hãy sửa file md rồi chạy lại.</p></main></body></html>')


def _rel(from_dir, target):
    return os.path.relpath(target, from_dir).replace("\\", "/")


def feature_docs(project, feature):
    """[(nhãn, đường dẫn tuyệt đối tới HTML)] các tài liệu của một tính năng, theo thứ tự đọc (tính theo file md có hoặc HTML có sẵn)."""
    root = config.ROOT
    t = root / "testing" / project / feature
    cand = {"srs": root / "srs" / project / f"{feature}.html"}
    for key in ("bang-soat-requirement", "phan-tich-requirement", "cau-hoi-cho-ba", "checklist", "test-case", "truy-vet", "ket-qua-test-case"):
        cand[key] = t / f"{key}.html"
    out = []
    for key, label in DOC_LABELS:
        h = cand.get(key)
        if h is not None and (h.exists() or h.with_suffix(".md").exists() and key != "ket-qua-test-case"):
            out.append((label, h))
    if (root / "evidence" / project / "features" / feature / "bao-cao.md").exists():
        out.append(("Nhật ký khám phá", root / "evidence" / project / "features" / feature / "bao-cao.html"))
    return out


def build_doc(project, src, converted):
    md = src.read_text(encoding="utf-8")
    body, title, heads = render_markdown(md, src, converted)
    out = src.with_suffix(".html")
    if out.exists() and GENERATOR not in out.read_text(encoding="utf-8", errors="ignore")[:600]:
        return None  # file HTML làm tay trùng tên: không ghi đè
    root = config.ROOT
    if "features" in src.parts:
        feature = src.parent.name
    elif "testing" in src.parts and src.parent.parent.name == project:
        feature = src.parent.name
    else:
        feature = src.stem if "srs" in src.parts else None
    parts = ['<nav class="nav-doc">']
    idx = root / "testing" / project / "index.html"
    parts.append(f'<a href="{_rel(src.parent, idx)}">← Trang tổng</a>')
    if feature:
        for label, p in feature_docs(project, feature):
            parts.append(f"<b>{html.escape(label)}</b>" if p == out else f'<a href="{_rel(src.parent, p)}">{html.escape(label)}</a>')
    parts.append("</nav>")
    toc = ""
    if len(heads) >= 4:
        toc = '<details class="muc-luc"><summary>Mục lục</summary><ul>' + "".join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for lv, i, t in heads if lv == 2) + "</ul></details>"
    out.write_text(_page(title or src.stem, body, "".join(parts), toc, has_table="<table>" in body), encoding="utf-8")
    return out


# ---------------------------------------------------------------- trang tổng
def _status_counts(test_case_file):
    names, counts = None, {}
    for line in test_case_file.read_text(encoding="utf-8").splitlines():
        if names is None and line.startswith("| Mã |"):
            names = [c.strip() for c in _CELL_SPLIT.split(line)[1:-1]]
        elif names and re.match(r'^\|\s*<a id="tc-\d+"></a>', line):
            d = dict(zip(names, [c.strip() for c in _CELL_SPLIT.split(line)[1:-1]]))
            st = d.get("Trạng thái", "Chưa chạy") or "Chưa chạy"
            counts[st] = counts.get(st, 0) + 1
    return counts


def _links(from_dir, items):
    if not items:
        return '<div class="links"><span class="none">Chưa có</span></div>'
    return '<div class="links">' + "".join(f'<a href="{_rel(from_dir, p)}">{html.escape(l)}</a>' for l, p in items) + "</div>"


def _bar(counts):
    total = sum(counts.values()) or 1
    order = ["Đạt", "Không đạt", "Bị chặn", "Bỏ qua", "Chưa chạy"]
    segs = "".join(f'<i class="s-{STATUSES.get(k, "gray")}" style="width:{100 * counts[k] / total:.1f}%" title="{html.escape(k)}: {counts[k]}"></i>' for k in order if counts.get(k))
    legend = "".join(f'<span><span class="badge {STATUSES.get(k, "gray")}">{html.escape(k)}</span> {counts[k]}</span>' for k in order if counts.get(k))
    return f'<div class="bar-tt">{segs}</div><div class="chu-thich">{legend}</div>'


def build_index(project):
    cfg = config.load(project)
    root = config.ROOT
    tdir = cfg.project_dir
    e = html.escape
    features = [d for d in sorted(tdir.iterdir()) if d.is_dir() and (d / "test-case.md").exists()]
    names = report_mod.FEATURE_NAMES
    version = cfg.test_data.get("version", "")
    cards, total_tc, total_bug, total_ran, total_fail = [], 0, 0, 0, 0
    for d in features:
        f = d.name
        counts = _status_counts(d / "test-case.md")
        n = sum(counts.values())
        total_tc += n
        total_ran += counts.get("Đạt", 0) + counts.get("Không đạt", 0)
        total_fail += counts.get("Không đạt", 0)
        auto = len(list((d / "auto").glob("tc-*.py"))) if (d / "auto").exists() else 0
        bugs = sorted((d / "bug").glob("BUG-*.md")) if (d / "bug").exists() else []
        total_bug += len(bugs)
        data = report_mod.read_results_data(cfg, f)
        last = data["runs"][-1] if data["runs"] else None
        run_line = (f'Lượt {last["number"]} ({e(last["timestamp"][:10])}, bản {e(last["build"])}): {report_mod._verdict_badge(last["verdict"])}' if last else "Chưa có lượt chạy ghi lại")
        bug_items = "".join(
            f'<li><a href="{_rel(tdir, b.with_suffix(".html"))}">{e(b.stem)}</a> <span class="badge gray">{e(report_mod._bug_severity(cfg, b.stem) or "?")}</span> {e(report_mod._bug_title(cfg, b.stem))}</li>' for b in bugs) or "<li>Chưa có bug</li>"
        title = names.get(f, f)
        cards.append(
            f'<div class="card"><h3>{e(title)}</h3><div class="small">{n} test case · {auto} có script tự động</div>'
            f"<h4>Tài liệu</h4>{_links(tdir, feature_docs(project, f))}"
            f"<h4>Tiến độ test case</h4>{_bar(counts)}"
            f"<h4>Lượt chạy gần nhất</h4><div>{run_line}</div>"
            f'<h4>Bug đã ghi ({len(bugs)})</h4><ul class="bugs">{bug_items}</ul></div>')
    smoke_card = ""
    sm = tdir / "smoke-test.md"
    if sm.exists():
        sdata = report_mod.read_results_data(cfg, "smoke")
        srun = sdata["runs"][-1] if sdata["runs"] else None
        links = [("Bộ smoke test", tdir / "smoke-test.html")] + ([("Kết quả smoke", tdir / "smoke-ket-qua.html")] if (tdir / "smoke-ket-qua.html").exists() else [])
        n_smoke = len(report_mod.read_smoke_table(cfg))
        srun_line = (f'Lượt {srun["number"]} ({e(srun["timestamp"][:10])}, bản {e(srun["build"])}): {report_mod._verdict_badge(srun["verdict"])}; {e(report_mod._count_statuses(srun))}' if srun else "Chưa có lượt chạy ghi lại")
        smoke_card = f'<div class="card"><h3>Bộ smoke test</h3><div class="small">{n_smoke} case chọn từ các test case</div><h4>Tài liệu</h4>{_links(tdir, [x for x in links if x[1].exists()])}<h4>Lượt chạy gần nhất</h4><div>{srun_line}</div></div>'
    ev = root / "evidence" / project
    ev_items = [(f"Báo cáo khám phá: {p.stem}", p) for p in sorted(ev.glob("*.html"))]
    for p in sorted((ev / "features").glob("*/*.html")) if (ev / "features").exists() else []:
        ev_items.append((f"{names.get(p.parent.name, p.parent.name)}: {p.stem}", p))
    guide = [("Hướng dẫn chạy test tự động", root / "docs" / "chay-test-tu-dong.html")]
    other = (f'<div class="card"><h3>Khám phá hệ thống và hướng dẫn</h3><h4>Báo cáo khám phá</h4>{_links(tdir, ev_items)}'
             f'<h4>Hướng dẫn</h4>{_links(tdir, [x for x in guide if x[1].exists()])}</div>')
    stats = ('<div class="so-lieu">' + "".join(f"<div><b>{v}</b><span>{k}</span></div>" for k, v in (
        ("tính năng có test case", len(features)), ("test case", total_tc), ("đã chạy có kết luận", total_ran), ("không đạt", total_fail), ("bug đã ghi", total_bug))) + "</div>")
    body = (f'<h1>Trang tổng · {e(project)}</h1><p class="small">Hệ thống: <a href="{e(cfg.url)}/">{e(cfg.url)}</a>' + (f" · bản test {e(version)}" if version else "") +
            f" · sinh lúc {time.strftime('%Y-%m-%d %H:%M')}. Mọi số liệu đọc từ file có sẵn; chạy lại <code>python -X utf8 scripts/build_docs.py</code> để cập nhật.</p>"
            + stats + '<h2>Từng tính năng</h2><div class="the">' + "".join(cards) + "</div>" + '<h2>Bộ smoke và tài liệu chung</h2><div class="the">' + smoke_card + other + "</div>")
    out = tdir / "index.html"
    out.write_text(_page(f"Trang tổng {project}", body), encoding="utf-8")
    return out


def build_all(project):
    sources = collect_sources(project)
    converted = {s.resolve() for s in sources}
    done, skipped = [], []
    for s in sources:
        r = build_doc(project, s, converted)
        (done if r else skipped).append(r or s)
    index = build_index(project)
    return done, skipped, index


def stale(project):
    """Các file md mới hơn HTML sinh từ nó (hoặc chưa có HTML)."""
    out = []
    for s in collect_sources(project):
        h = s.with_suffix(".html")
        if not h.exists() or h.stat().st_mtime < s.stat().st_mtime:
            out.append(s)
    return out
