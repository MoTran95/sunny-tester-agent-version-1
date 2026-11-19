"""Bảng kết quả các lượt chạy bộ test (smoke, sau này regression) và trang HTML xem nhanh.

Dữ liệu gốc: `testing/<dự-án>/run-results/<bộ>.json` (chỉ thêm lượt mới, không sửa tay).
Từ đó script sinh ra (đừng sửa tay, chạy lại là ghi đè):
  - testing/<dự-án>/<bộ>-ket-qua.md
  - testing/<dự-án>/<bộ>-ket-qua.html
Bảng chính 6 cột: ID, Smoke case, Status, Evidence, Bug, Số lần chạy. "Số lần chạy" = số lượt đã có
kết luận Đạt/Không đạt cho case đó (đếm từ lịch sử, không ghi tay).
"""
import html
import json
import re
import time
from pathlib import Path

from . import config

PASS = "Đạt"
PASS_KNOWN_ISSUE = "Đạt kèm lỗi đã biết"
PASS_MINOR_FAIL = "Đạt kèm ý phụ sai"
FAIL = "Không đạt"
NO_VERDICT = "Không kết luận"
NOT_RUN = "Chưa chạy"
NO_SCRIPT = "Chưa có script"
HAS_VERDICT = {PASS, PASS_KNOWN_ISSUE, PASS_MINOR_FAIL, FAIL}
BLOCKED = "Bị chặn"
SKIPPED = "Bỏ qua"
ACCEPT_BUILD, REJECT_BUILD, INCOMPLETE = "Nhận build", "Trả build", "Chưa đủ kết luận"
ALL_PASS, HAS_FAIL, NOT_ALL_RUN = "Đạt toàn bộ", "Có case không đạt", "Chưa chạy hết"
SUITE_NAMES = {"smoke": "Smoke test", "regression": "Regression"}
MATRIX_RUNS = 8

_CELL_SPLIT = re.compile(r"(?<!\\)\|")


# ---------- đọc bảng smoke ----------
def read_smoke_table(cfg):
    """[{so, id, ten, ma_goc, tinh_nang, tc}] đọc từ bảng chính của smoke-test.md."""
    f = cfg.project_dir / "smoke-test.md"
    if not f.exists():
        raise config.ConfigError(f"Không có {f.relative_to(config.ROOT)}")
    entries, seen = [], set()
    for line in f.read_text(encoding="utf-8").splitlines():
        m_so = re.match(r"^\|\s*(\d+)\s*\|", line)
        m_ca = re.search(r"\[([^\]]+)\]\(([\w-]+)/test-case\.md#(tc-\d+)\)", line)
        if not (m_so and m_ca) or m_so.group(1) in seen:
            continue
        o = _CELL_SPLIT.split(line)
        seen.add(m_so.group(1))
        entries.append({"number": m_so.group(1), "id": f"SM-{int(m_so.group(1)):02d}", "title": o[2].strip(),
                   "source_ref": m_ca.group(1), "feature": m_ca.group(2), "tc": m_ca.group(3)})
    return sorted(entries, key=lambda x: int(x["number"]))


def read_feature_table(cfg, feature):
    """Bảng toàn bộ test case của một tính năng (đọc test-case.md theo TÊN cột): cùng dạng với read_smoke_table."""
    f = cfg.project_dir / feature / "test-case.md"
    if not f.exists():
        raise config.ConfigError(f"Không có {f.relative_to(config.ROOT)}")
    names, entries = None, []
    for line in f.read_text(encoding="utf-8").splitlines():
        if names is None and line.startswith("| Mã |"):
            names = [c.strip() for c in _CELL_SPLIT.split(line)[1:-1]]
        elif names:
            m = re.match(r'^\|\s*<a id="(tc-\d+)"></a>(TC-\d+)', line)
            if m:
                d = dict(zip(names, [c.strip() for c in _CELL_SPLIT.split(line)[1:-1]]))
                entries.append({"number": str(int(m.group(1)[3:])), "id": m.group(2), "title": d.get("Tình huống", "").replace("**", ""),
                                "source_ref": "Ưu tiên " + d.get("Ưu tiên", "?"), "feature": feature, "tc": m.group(1)})
    return sorted(entries, key=lambda x: int(x["number"]))


def read_table(cfg, suite):
    return read_smoke_table(cfg) if suite == "smoke" else read_feature_table(cfg, suite)


FEATURE_NAMES = {"dang-nhap": "Đăng nhập", "khuyen-nghi-ltv-dsr": "Khuyến nghị LTV/DSR", "gui-tham-dinh": "Gửi thẩm định"}


def suite_title(suite):
    return SUITE_NAMES.get(suite) or f"Test case {FEATURE_NAMES.get(suite, suite)}"


def case_label(suite):
    return "Smoke case" if suite == "smoke" else "Test case"


def page_dir(cfg, suite):
    return cfg.project_dir if suite == "smoke" else cfg.project_dir / suite


def page_files(cfg, suite):
    d = page_dir(cfg, suite)
    return (d / "smoke-ket-qua.md", d / "smoke-ket-qua.html") if suite == "smoke" else (d / "ket-qua-test-case.md", d / "ket-qua-test-case.html")


# ---------- dữ liệu lượt ----------
def results_data_path(cfg, suite):
    return cfg.project_dir / "run-results" / f"{suite}.json"


def read_results_data(cfg, suite):
    f = results_data_path(cfg, suite)
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))
    return {"project": cfg.project, "suite": suite, "runs": []}


def _normalize_path(path):
    return str(path).replace("\\", "/")


def _find_bug_file(cfg, code):
    pairs = sorted(cfg.project_dir.glob(f"**/bug/{code}.md"))
    return str(pairs[0].relative_to(config.ROOT)).replace("\\", "/") if pairs else None


def add_run(cfg, suite, build, case_results, run_by="Sunny Tran", run_method="Tự động (Playwright)",
              note="", status_override=None, bug=None, sources=None, timestamp=None, add_error_images=None, error_captions=None, blocked_by=None, conclusion=None):
    """Thêm một lượt vào dữ liệu rồi sinh lại md + html.

    ket_qua_ca: danh sách dict {ca: 'dang-nhap/tc-005', ket_luan, ly_do, anh: [...]} (định dạng file result-*.json),
    theo thứ tự thời gian; ca chạy sau thay ca trước nếu ca trước chưa có kết luận.
    ghi_de_status: {"2": "Đạt kèm lỗi đã biết"}; bug: {"2": ["BUG-001"]}; them_anh_loi: {"2": ["evidence/.../anh-loi.png"]}; chu_thich_loi: {"2": "Lỗi ở bước 5: ..."} (gắn cho mọi ảnh tô đỏ của case đó chưa có chú thích).
    Mỗi case lưu thêm `thuc_te` (các ý kiểm tra đúng/sai đã thấy) và `evidence_loi` (ảnh tô đỏ chỗ lỗi).
    """
    table = read_table(cfg, suite)
    by_case = {}
    for b in table:  # một test case có thể đứng ở nhiều dòng smoke: ghi cho tất cả
        by_case.setdefault((b["feature"], b["tc"]), []).append(b["number"])
    results = {b["number"]: {"status": NOT_RUN, "evidence": [], "evidence_error": [], "evidence_error_captions": {}, "video": [], "bug": [], "blocked_by": [], "note": "", "actual": []} for b in table}
    for kq in case_results:
        feature, _, tc = kq["case_id"].partition("/")
        for number in by_case.get((feature, tc), []):
            old = results[number]["status"]
            if old in HAS_VERDICT and kq["verdict"] not in HAS_VERDICT:
                continue  # giữ kết quả đã có kết luận
            results[number] = {
                "status": kq["verdict"] if kq["verdict"] not in (NO_SCRIPT,) else NOT_RUN,
                "evidence": [_normalize_path(a) for a in kq.get("images", [])],
                "evidence_error": [_normalize_path(a) for a in kq.get("error_images", [])],
                "evidence_error_captions": {_normalize_path(k): t for k, t in kq.get("error_image_captions", {}).items()},
                "video": [_normalize_path(a) for a in kq.get("videos", [])],
                "bug": [], "blocked_by": [], "note": kq.get("reason", ""),
                "actual": [{"kind": k["kind"], "title": k["title"], "passed": k["passed"], "note": k.get("note", "")} for k in kq.get("checks", [])],
            }
    for number, st in (status_override or {}).items():
        results[number]["status"] = st
    for number, entries in (add_error_images or {}).items():
        results[number]["evidence_error"] += [_normalize_path(a) for a in entries]
    for number, text in (error_captions or {}).items():
        for a in results[number]["evidence_error"]:
            results[number]["evidence_error_captions"].setdefault(a, text)
    for number, entries in (bug or {}).items():
        for code in entries:
            results[number]["bug"].append({"code": code, "path": _find_bug_file(cfg, code)})

    for number, entries in (blocked_by or {}).items():
        for code in entries:
            results[number]["blocked_by"].append({"code": code, "path": _find_bug_file(cfg, code)})

    statuses = [v["status"] for v in results.values()]
    if suite == "smoke":
        verdict = REJECT_BUILD if FAIL in statuses else ACCEPT_BUILD if all(s in HAS_VERDICT for s in statuses) else INCOMPLETE
    else:
        verdict = HAS_FAIL if FAIL in statuses else ALL_PASS if all(s in HAS_VERDICT for s in statuses) else NOT_ALL_RUN

    data = read_results_data(cfg, suite)
    run_record = {
        "number": len(data["runs"]) + 1, "build": build,
        "timestamp": timestamp or time.strftime("%Y-%m-%d %H:%M:%S"),
        "run_by": run_by, "run_method": run_method, "verdict": verdict, "note": note,
        "sources": [_normalize_path(n) for n in (sources or [])], "results": results,
    }
    if conclusion:
        run_record["conclusion"] = conclusion
    data["runs"].append(run_record)
    f = results_data_path(cfg, suite)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    build_pages(cfg, suite)
    return run_record


def read_test_case(cfg, feature, tc):
    """{'buoc': ..., 'mong_doi': ...} lấy từ dòng test case gốc (đọc theo TÊN cột, nên file 12 hay 13 cột đều được)."""
    f = cfg.project_dir / feature / "test-case.md"
    if not f.exists():
        return {"steps": "", "expected": ""}
    column_names = None
    for line in f.read_text(encoding="utf-8").splitlines():
        if column_names is None and line.startswith("| Mã |"):
            column_names = [c.strip() for c in _CELL_SPLIT.split(line)[1:-1]]
        elif column_names and f'id="{tc}"' in line:
            o = [c.strip() for c in _CELL_SPLIT.split(line)[1:-1]]
            d = dict(zip(column_names, o))
            return {"steps": d.get("Các bước", ""), "expected": d.get("Kết quả mong đợi", "")}
    return {"steps": "", "expected": ""}


_BR = re.compile(r"<br\s*/?>")


def _cell_lines(o):
    """Ô trong bảng md (các dòng ngăn bằng <br>) → danh sách dòng chữ thường (bỏ dấu huyền)."""
    return [x.replace("`", "").strip() for x in _BR.split(o or "") if x.strip()]


def _cell_html(o):
    """Ô md → HTML: mỗi dòng một đoạn, chữ trong dấu huyền thành <code>."""
    out = []
    for line in _BR.split(o or ""):
        line = line.strip()
        if line:
            out.append("<div>" + re.sub(r"`([^`]+)`", lambda m: f"<code>{m.group(1)}</code>", html.escape(line, quote=False).replace("`", "`")) + "</div>")
    return "".join(out) or "—"


def _actual_lines(v):
    """Kết quả thực tế của một case → [(dung, chữ)] từ các ý kiểm tra đã chạy; không có thì dùng ghi chú của lượt."""
    out = []
    for k in v.get("actual", []):
        plain = k["title"].replace("`", "") + (" (ý phụ)" if k["kind"] == "minor" else "")
        if k.get("note"):
            plain += " — " + k["note"].replace("`", "")
        out.append((k["passed"], plain))
    if not out and v.get("note"):
        out.append((None, v["note"]))
    return out


# ---------- tính toán ----------
def run_count(data, number):
    return sum(1 for l in data["runs"] if l["results"].get(number, {}).get("status") in HAS_VERDICT)


def _count_statuses(run_record):
    counts = {}
    for v in run_record["results"].values():
        counts[v["status"]] = counts.get(v["status"], 0) + 1
    return ", ".join(f"{n} {s}" for s, n in counts.items())


def _link(cfg, suite, path_from_root):
    """Đường dẫn tương đối từ thư mục chứa trang kết quả tới file tính từ gốc repo."""
    import os

    return os.path.relpath(config.ROOT / path_from_root, page_dir(cfg, suite)).replace("\\", "/")


def _bug_href(cfg, suite, x, ext):
    return _link(cfg, suite, x["path"]).removesuffix(".md") + ext


def _bug_cell_md(cfg, suite, v):
    lines = [f"[{x['code']}]({_bug_href(cfg, suite, x, '.md')})" if x["path"] else x["code"] for x in v["bug"]]
    lines += ["Bị chặn bởi " + (f"[{x['code']}]({_bug_href(cfg, suite, x, '.md')})" if x["path"] else x["code"]) for x in v.get("blocked_by", [])]
    return "<br>".join(lines) or "—"


def _bug_cell_html(cfg, suite, v):
    e = html.escape

    def one(x):
        return f'<a href="{e(_bug_href(cfg, suite, x, ".html"))}">{e(x["code"])}</a>' if x["path"] else e(x["code"])

    parts = []
    if v["bug"]:
        parts.append(", ".join(one(x) for x in v["bug"]))
    if v.get("blocked_by"):
        parts.append('<div class="small">Bị chặn bởi ' + ", ".join(one(x) for x in v["blocked_by"]) + "</div>")
    return "".join(parts) or "—"


# ---------- Markdown ----------
def build_md(cfg, suite, data, table):
    title = suite_title(suite)
    d = ["# Kết quả chạy " + title.lower() + f" — {cfg.project}", "",
         "> File tự sinh từ `testing/%s/run-results/%s.json` bằng `scripts/build_report.py` — đừng sửa tay, chạy lại là ghi đè. Bản dễ xem: `%s`." % (cfg.project, suite, page_files(cfg, suite)[1].name), ""]
    if not data["runs"]:
        d += ["Chưa có lượt chạy nào.", ""]
        return "\n".join(d)
    new_text = data["runs"][-1]
    d += ["| | |", "|---|---|",
          f"| Build | **{new_text['build']}** |", f"| Lượt | {new_text['number']} / {len(data['runs'])} (lượt mới nhất) |",
          f"| Thời điểm | {new_text['timestamp']} |", f"| Người chạy | {new_text['run_by']} |",
          f"| Cách chạy | {new_text['run_method']} |", f"| Kết luận | **{new_text['verdict']}** |",
          f"| Ghi chú | {new_text['note'] or '—'} |", ""]
    d += _conclusion_md(new_text)
    d += ["## Kết quả lượt mới nhất", "",
          f"| ID | {case_label(suite)} | Các bước | Kết quả mong đợi | Status | Evidence | Bug | Số lần chạy |", "|---|---|---|---|---|---|---|---|"]
    for b in table:
        v = new_text["results"][b["number"]]
        test_case = read_test_case(cfg, b["feature"], b["tc"])
        ev = [f"[{Path(a).name}]({_link(cfg, suite, a)})" for a in v["evidence"]]
        ev += [f"🔴 [{Path(a).name}]({_link(cfg, suite, a)}) (tô đỏ chỗ lỗi)" + (f": {v.get('evidence_error_captions', {}).get(a)}" if v.get("evidence_error_captions", {}).get(a) else "")
               for a in v.get("evidence_error", [])]
        ev += [f"🎬 [{Path(a).name}]({_link(cfg, suite, a)}) (video quay lại ca)" for a in v.get("video", [])]
        bug_cell = _bug_cell_md(cfg, suite, v)
        steps = "<br>".join(_cell_lines(test_case["steps"])) or "—"
        expected = "<br>".join(_cell_lines(test_case["expected"])) or "—"
        case_title = f"{b['title']} ({b['source_ref']})"
        d.append(f"| {b['id']} | {case_title} | {steps} | {expected} | {v['status']} | {'<br>'.join(ev) or '—'} | {bug_cell} | {run_count(data, b['number'])} |")
    d += ["", "## Lịch sử các lượt", "",
          "| Lượt | Build | Thời điểm | Người chạy | Kết quả | Kết luận |", "|---|---|---|---|---|---|"]
    for l in reversed(data["runs"]):
        d.append(f"| {l['number']} | {l['build']} | {l['timestamp']} | {l['run_by']} | {_count_statuses(l)} | {l['verdict']} |")
    entries = data["runs"][-MATRIX_RUNS:]
    d += ["", f"## Từng case qua các lượt (tối đa {MATRIX_RUNS} lượt gần nhất)", "",
          "| ID | " + " | ".join(f"Lượt {l['number']} ({l['build']})" for l in entries) + " |",
          "|---|" + "---|" * len(entries)]
    for b in table:
        d.append(f"| {b['id']} | " + " | ".join(l["results"].get(b["number"], {}).get("status", NOT_RUN) for l in entries) + " |")
    d += ["", "Các bước và Kết quả mong đợi lấy từ test case gốc. Bị chặn: chưa test được vì bug khác (xem cột Bug). Số lần chạy: số lượt có kết luận Đạt, Đạt kèm lỗi đã biết, Đạt kèm ý phụ sai hoặc Không đạt; lượt Không kết luận và Chưa chạy không tính.", ""]
    return "\n".join(d)


# ---------- HTML ----------
_CSS = """
/* Màu lấy mẫu từ ảnh thương hiệu (đỏ #C24E3A, vàng #E8A53C, xanh #2E7D32, nâu #3A2E26); nền và thẻ hạ độ sáng cho đỡ chói.
   Chế độ tối theo hệ điều hành, có nút đổi tay (lưu trong trình duyệt). */
:root{color-scheme:light;--bg:#E8DFD0;--card:#F2EDE5;--text:#3A2E26;--body:#463B34;--muted:#6F6154;--line:#D1C9BB;--coral:#C24E3A;--amber:#D9902A;--amberbg:#F6E6C3;--amberfg:#8A5A0E;--warnline:#E6CC93;--green:#2E7D32;--greenbg:#E1EDE3;--greenline:#BBD6C2;--pinkbg:#F8E4DE;--pinkline:#E0B0A4;--graybg:#DCD4C6;--grayfg:#5F5246}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;--bg:#251F1A;--card:#2E2721;--text:#F1E6D4;--body:#DCCFBE;--muted:#A89A8B;--line:#44392F;--coral:#EE8F7C;--amber:#E8A53C;--amberbg:#3A2F18;--amberfg:#EDBB62;--warnline:#5E4A22;--green:#86D08F;--greenbg:#1F3228;--greenline:#2F5A3E;--pinkbg:#3B2420;--pinkline:#6B3A32;--graybg:#38302A;--grayfg:#B8AA9A}:root:not([data-theme=light]) .brand img{background:#E8DFD0;border-radius:14px;padding:6px 14px}}
:root[data-theme=dark]{color-scheme:dark;--bg:#251F1A;--card:#2E2721;--text:#F1E6D4;--body:#DCCFBE;--muted:#A89A8B;--line:#44392F;--coral:#EE8F7C;--amber:#E8A53C;--amberbg:#3A2F18;--amberfg:#EDBB62;--warnline:#5E4A22;--green:#86D08F;--greenbg:#1F3228;--greenline:#2F5A3E;--pinkbg:#3B2420;--pinkline:#6B3A32;--graybg:#38302A;--grayfg:#B8AA9A}
:root[data-theme=dark] .brand img{background:#E8DFD0;border-radius:14px;padding:6px 14px}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--body);font:16px/1.65 "Hanken Grotesk","Instrument Sans","Segoe UI",system-ui,sans-serif;padding:40px 16px 56px}
main{max-width:1100px;margin:0 auto}
.brand{text-align:center;margin:0 0 14px}.brand img{height:68px;width:auto}
.eyebrow{text-align:center;font-size:12px;font-weight:700;letter-spacing:.22em;text-transform:uppercase;color:var(--amber);margin:0 0 10px}
h1{font:700 40px/1.15 Fraunces,Georgia,"Times New Roman",serif;color:var(--text);text-align:center;margin:0 0 8px}
h1 em{font-style:italic;color:var(--coral)}
h2{font:700 22px/1.3 Fraunces,Georgia,serif;color:var(--text);margin:36px 0 12px}
.sub{text-align:center;color:var(--muted);margin:0 0 26px;font-size:14px}
code{background:var(--graybg);padding:1px 6px;border-radius:5px;font-size:13px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 22px}
dl.meta{display:grid;grid-template-columns:max-content 1fr;gap:8px 24px;margin:0}
dl.meta dt{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);padding-top:3px}
dl.meta dd{margin:0}
.wrap{overflow-x:auto;border:1px solid var(--line);border-radius:14px;background:var(--card)}
table{border-collapse:collapse;width:100%;min-width:640px}
th,td{padding:12px 16px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);background:var(--bg)}
tr:last-child td{border-bottom:0}
a{color:var(--coral);text-decoration-color:var(--pinkline);text-underline-offset:3px}
a:hover{text-decoration-color:var(--coral)}
.badge{display:inline-block;padding:3px 11px;border-radius:999px;font-size:13px;font-weight:700;white-space:nowrap;border:1px solid transparent}
.ok{background:var(--greenbg);color:var(--green);border-color:var(--greenline)}
.warn{background:var(--amberbg);color:var(--amberfg);border-color:var(--warnline)}
.bad{background:var(--pinkbg);color:var(--coral);border-color:var(--pinkline)}
.gray{background:var(--graybg);color:var(--grayfg);border-color:var(--line)}
.num{text-align:center}.nw{white-space:nowrap}
.small{font-size:13px;color:var(--muted)}
ul.ev{margin:0;padding-left:16px}
.note{font:400 18px/1.6 Fraunces,Georgia,serif;color:var(--text);text-align:center;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:18px 8px;margin:36px 0 0}
main.rong{max-width:1840px}
.thumb.kiem{border-color:#1B8F3A}.cap-ok{color:var(--green);font-size:13px;font-weight:700;line-height:1.45;margin:6px 0 2px;max-width:230px}.vid{display:block;margin-top:6px;max-width:250px;border-radius:8px;background:#000}
.kl h3{font:700 16px/1.3 Fraunces,Georgia,serif;color:var(--text);margin:18px 0 6px}.kl p{margin:6px 0}.kl ul{margin:6px 0;padding-left:22px}.kl li{margin:5px 0}.kl-dau{font-size:17px;color:var(--text);font-weight:500}.kl-bang{min-width:0;width:100%}.kl-bang td{font-size:14.5px}
.lon table{min-width:1280px;border-collapse:separate;border-spacing:0}.lon td:nth-child(2){min-width:230px}
.khu-bang{position:relative}.lon{scrollbar-width:none;cursor:grab}.lon::-webkit-scrollbar{display:none}.lon.keo{cursor:grabbing;user-select:none}
.thanh-keo{position:sticky;bottom:0;z-index:6;overflow-x:auto;overflow-y:hidden;height:18px;background:var(--bg);border:1px solid var(--line);border-radius:10px;margin-top:6px}
.thanh-keo>div{height:1px}
.lon th:nth-child(1),.lon td:nth-child(1){position:sticky;left:0;z-index:2;background:var(--card);width:76px;min-width:76px}
.lon th:nth-child(2),.lon td:nth-child(2){position:sticky;left:76px;z-index:2;background:var(--card);box-shadow:3px 0 0 var(--line)}
.lon th:nth-child(1),.lon th:nth-child(2){background:var(--bg);z-index:3}
.goi-y{margin:0 0 8px;font-size:13px;color:var(--muted)}
.cap-loi{color:var(--coral);font-size:13px;font-weight:700;line-height:1.45;margin:6px 0 2px;max-width:230px}.cot-nho{font-size:13.5px;line-height:1.5;min-width:170px}.cot-nho div+div{margin-top:4px}.cot-nho code{font-size:12px}
.thuc-te .dung{color:var(--green)}.thuc-te .sai{color:var(--coral);font-weight:700}
ul.ev li.loi{list-style:none;margin:8px 0 0 -16px}.thumb{display:block;margin-top:6px;max-width:210px;border:3px solid #E5252A;border-radius:8px}
.theme{position:absolute;top:12px;right:12px;z-index:5;background:var(--card);color:var(--body);border:1px solid var(--line);border-radius:999px;padding:6px 14px;font:700 12px/1 inherit;font-family:inherit;letter-spacing:.06em;cursor:pointer}
.theme:hover{border-color:var(--coral);color:var(--coral)}
@media (max-width:600px){h1{font-size:30px}body{padding-top:28px}}
"""


_JS_DRAG_SCROLL = ("document.addEventListener('DOMContentLoaded',function(){document.querySelectorAll('.khu-bang').forEach(function(k){"
           "var w=k.querySelector('.wrap'),p=k.querySelector('.thanh-keo'),i=p.firstElementChild,t=w.querySelector('table'),a=false;"
           "function dat(){i.style.width=t.scrollWidth+'px';p.style.display=(w.scrollWidth>w.clientWidth+2)?'block':'none'}dat();addEventListener('resize',dat);"
           "p.addEventListener('scroll',function(){if(a){a=false;return}a=true;w.scrollLeft=p.scrollLeft});"
           "w.addEventListener('scroll',function(){if(a){a=false;return}a=true;p.scrollLeft=w.scrollLeft});"
           "var x0=0,s0=0,d=false;w.addEventListener('mousedown',function(e){if(e.target.closest('a,button,img')||e.button!==0)return;d=true;x0=e.clientX;s0=w.scrollLeft;w.classList.add('keo')});"
           "addEventListener('mouseup',function(){d=false;w.classList.remove('keo')});"
           "addEventListener('mousemove',function(e){if(d)w.scrollLeft=s0-(e.clientX-x0)})})});")

_JS_THEME = "(function(){var r=document.documentElement;try{var t=localStorage.getItem('smoke-theme');if(t)r.setAttribute('data-theme',t)}catch(e){}document.addEventListener('DOMContentLoaded',function(){var b=document.getElementById('theme');function eff(){var t=r.getAttribute('data-theme');return t||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}function lab(){b.textContent=eff()==='dark'?'Chế độ sáng':'Chế độ tối'}lab();b.onclick=function(){var n=eff()==='dark'?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('smoke-theme',n)}catch(e){}lab()}})})();"


def _badge(status):
    cls = {PASS: "ok", PASS_KNOWN_ISSUE: "warn", PASS_MINOR_FAIL: "warn", FAIL: "bad", BLOCKED: "warn"}.get(status, "gray")
    return f'<span class="badge {cls}">{html.escape(status)}</span>'


LOGO_PATH = "docs/thuong-hieu/logo-sunny-nhan-ra-nen-trong.png"


def _logo_data_uri():
    """Nhúng logo (bản nền trong suốt) thẳng vào trang để gửi file đi không thiếu logo; không có file thì bỏ qua.

    Bản nền trong suốt tạo một lần bằng `python scripts/process_logo.py` từ logo gốc
    `docs/thuong-hieu/logo-sunny-nhan-ra.png` (cần Pillow ở lần đó, không cần khi sinh trang).
    """
    import base64

    f = config.ROOT / LOGO_PATH
    if not f.exists():
        return None
    return "data:image/png;base64," + base64.b64encode(f.read_bytes()).decode("ascii")


def _verdict_badge(verdict):
    cls = "ok" if verdict in (ACCEPT_BUILD, ALL_PASS) else "bad" if verdict in (REJECT_BUILD, HAS_FAIL) else "gray"
    return f'<span class="badge {cls}">{html.escape(verdict)}</span>'


def _bug_severity(cfg, code):
    path = _find_bug_file(cfg, code)
    if not path:
        return ""
    text = (config.ROOT / path).read_text(encoding="utf-8")
    m = re.search(r"## Mức độ nghiêm trọng\s*\n+\*\*([^*]+?)\.?\*\*", text)
    return m.group(1).strip() if m else ""


def _conclusion_counts(run_record):
    c = {}
    for v in run_record["results"].values():
        c[v["status"]] = c.get(v["status"], 0) + 1
    total = len(run_record["results"])
    ran = sum(n for st, n in c.items() if st in HAS_VERDICT)
    return total, ran, c


def _conclusion_html(run_record):
    """Thẻ 'Kết luận và rủi ro': số liệu tự tính + phần người soát viết (headline, đã kiểm, chưa kiểm được, rủi ro, đề xuất)."""
    k = run_record.get("conclusion")
    if not k:
        return ""
    e = html.escape
    total, ran, counts = _conclusion_counts(run_record)
    parts = ['<h2>Kết luận và rủi ro</h2><div class="card kl">',
             f'<p class="kl-dau">{e(k.get("headline", ""))}</p>',
             f'<p class="small">Số liệu lượt này: {ran} trên {total} case đã có kết quả ({round(100 * ran / total)}%): '
             + e(", ".join(f"{n} {st}" for st, n in counts.items())) + ".</p>"]
    if k.get("passed"):
        parts.append("<h3>Đã kiểm và đạt</h3><ul>" + "".join(f"<li>{e(x)}</li>" for x in k["passed"]) + "</ul>")
    if k.get("not_tested"):
        parts.append('<h3>Chưa có kết quả và vì sao</h3><table class="kl-bang"><thead><tr><th>Case</th><th>Trạng thái</th><th>Lý do</th></tr></thead><tbody>'
                     + "".join(f"<tr><td class='nw'>{e(x['cases'])}</td><td>{_badge(x['status'])}</td><td>{e(x['reason'])}</td></tr>" for x in k["not_tested"]) + "</tbody></table>")
    if k.get("risks"):
        parts.append("<h3>Rủi ro để người kiểm thử đánh giá</h3><ul>" + "".join(f"<li><strong>{e(x['title'])}.</strong> {e(x['detail'])}</li>" for x in k["risks"]) + "</ul>")
    if k.get("suggestion"):
        parts.append(f'<h3>Đề xuất (người kiểm thử hoặc PO quyết định)</h3><p>{e(k["suggestion"])}</p>')
    parts.append("</div>")
    return "".join(parts)


def _conclusion_md(run_record):
    k = run_record.get("conclusion")
    if not k:
        return []
    total, ran, counts = _conclusion_counts(run_record)
    d = ["## Kết luận và rủi ro", "", k.get("headline", ""), "",
         f"Số liệu lượt này: {ran} trên {total} case đã có kết quả ({round(100 * ran / total)}%): " + ", ".join(f"{n} {st}" for st, n in counts.items()) + ".", ""]
    if k.get("passed"):
        d += ["**Đã kiểm và đạt**", ""] + [f"- {x}" for x in k["passed"]] + [""]
    if k.get("not_tested"):
        d += ["**Chưa có kết quả và vì sao**", "", "| Case | Trạng thái | Lý do |", "|---|---|---|"] + [f"| {x['cases']} | {x['status']} | {x['reason']} |" for x in k["not_tested"]] + [""]
    if k.get("risks"):
        d += ["**Rủi ro để người kiểm thử đánh giá**", ""] + [f"- **{x['title']}.** {x['detail']}" for x in k["risks"]] + [""]
    if k.get("suggestion"):
        d += ["**Đề xuất (người kiểm thử hoặc PO quyết định)**", "", k["suggestion"], ""]
    return d


def _bug_title(cfg, code):
    path = _find_bug_file(cfg, code)
    if not path:
        return ""
    first = (config.ROOT / path).read_text(encoding="utf-8").splitlines()[0]
    return first.lstrip("# ").replace("`", "").strip()


def _bug_summary_html(cfg, suite, run_record, table):
    """Bảng 'Bug đã mở': mỗi bug, tiêu đề, case thấy lỗi, case bị chặn vì bug đó."""
    e = html.escape
    ids = {b["number"]: b["id"] for b in table}
    found, blocked = {}, {}
    for number, v in run_record["results"].items():
        for x in v["bug"]:
            found.setdefault(x["code"], []).append(ids[number])
        for x in v.get("blocked_by", []):
            blocked.setdefault(x["code"], []).append(ids[number])
    codes = sorted(set(found) | set(blocked))
    if not codes:
        return ""
    rows = []
    for code in codes:
        path = _find_bug_file(cfg, code)
        link = f'<a href="{e(_link(cfg, suite, path).removesuffix(".md") + ".html")}">{e(code)}</a>' if path else e(code)
        rows.append(f"<tr><td class='nw'>{link}</td><td>{e(_bug_title(cfg, code))}</td><td>{e(_bug_severity(cfg, code) or '—')}</td><td>{e(', '.join(found.get(code, [])) or '—')}</td><td>{e(', '.join(blocked.get(code, [])) or '—')}</td></tr>")
    return ('<h2>Bug đã mở</h2><div class="wrap"><table><thead><tr><th>Bug</th><th>Tiêu đề</th><th>Mức độ nghiêm trọng</th><th>Case thấy lỗi</th><th>Case bị chặn vì bug này</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")


def build_html(cfg, suite, data, table):
    e = html.escape
    title = suite_title(suite)
    logo = _logo_data_uri()
    p = [f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
         f"<title>Kết quả {e(title)} {e(cfg.project)}</title>"
         '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,700;1,9..144,700&family=Hanken+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">'
         f"<style>{_CSS}</style><script>{_JS_THEME}{_JS_DRAG_SCROLL}</script></head><body><button id=\"theme\" class=\"theme\" type=\"button\">Chế độ tối</button><main class=\"rong\">",
         (f'<div class="brand"><img src="{logo}" alt="Sunny Nhận Ra"></div>' if logo else ""),
         f'<p class="eyebrow">Kết quả chạy {e(title.lower())}</p>',
         f"<h1>Lượt chạy của <em>{e(cfg.project)}</em></h1>",
         '<p class="sub">Trang tự sinh từ file dữ liệu bằng <code>scripts/build_report.py</code>; không sửa tay.</p>']
    if not data["runs"]:
        p.append("<p>Chưa có lượt chạy nào.</p></main></body></html>")
        return "".join(p)
    new_text = data["runs"][-1]
    p.append('<div class="card"><dl class="meta">')
    for k, v in (("Build", f"<strong>{e(new_text['build'])}</strong>"), ("Lượt", f"{new_text['number']} / {len(data['runs'])} (mới nhất)"),
                 ("Thời điểm", e(new_text["timestamp"])), ("Người chạy", e(new_text["run_by"])), ("Cách chạy", e(new_text["run_method"])),
                 ("Kết quả", e(_count_statuses(new_text))), ("Kết luận", _verdict_badge(new_text["verdict"])),
                 ("Ghi chú", e(new_text["note"]) or "—")):
        p.append(f"<dt>{k}</dt><dd>{v}</dd>")
    p.append("</dl></div>")
    p.append(_conclusion_html(new_text))
    p.append(f'<h2>Kết quả lượt mới nhất</h2><p class="goi-y">Trang rộng gần hết màn hình, bảng tự co theo bề rộng. Nếu màn hình hẹp vẫn phải kéo ngang: dùng thanh cuộn luôn hiện ở cuối màn hình, hoặc giữ chuột trái kéo trên bảng, hoặc giữ Shift và lăn chuột. Hai cột ID và {case_label(suite)} được giữ cố định bên trái.</p><div class="khu-bang"><div class="wrap lon"><table><thead><tr><th>ID</th><th>{case_label(suite)}</th><th>Các bước</th><th>Kết quả mong đợi</th>'
             '<th>Status</th><th>Evidence</th><th>Bug</th><th class="num">Số lần chạy</th></tr></thead><tbody>')
    for b in table:
        v = new_text["results"][b["number"]]
        test_case = read_test_case(cfg, b["feature"], b["tc"])
        ev = "".join(
            (f'<li class="loi"><span class="badge ok">Ảnh kiểm tra</span><div class="cap-ok">Khung xanh: đã kiểm và đạt. Khung đỏ: sai.</div>'
             f'<a href="{e(_link(cfg, suite, a))}" target="_blank" rel="noopener"><img class="thumb kiem" src="{e(_link(cfg, suite, a))}" alt="{e(Path(a).name)}"></a></li>')
            if "-kiem" in Path(a).name else
            f'<li><a href="{e(_link(cfg, suite, a))}" target="_blank" rel="noopener">{e(Path(a).name)}</a></li>' for a in v["evidence"])
        ev += "".join(
            f'<li class="loi"><span class="badge bad">Ảnh tô đỏ chỗ lỗi</span>'
            + (f'<div class="cap-loi">{e(v.get("evidence_error_captions", {}).get(a, ""))}</div>' if v.get("evidence_error_captions", {}).get(a) else "")
            + f'<a href="{e(_link(cfg, suite, a))}" target="_blank" rel="noopener">'
            f'<img class="thumb" src="{e(_link(cfg, suite, a))}" alt="{e(Path(a).name)}"></a></li>' for a in v.get("evidence_error", []))
        ev += "".join(f'<li class="loi"><span class="badge warn">Video quay lại ca</span><video class="vid" controls preload="none" src="{e(_link(cfg, suite, a))}"></video>'
                      f'<a href="{e(_link(cfg, suite, a))}" target="_blank" rel="noopener">{e(Path(a).name)}</a></li>' for a in v.get("video", []))
        ev = f'<ul class="ev">{ev}</ul>' if ev else "—"
        bug_cell = _bug_cell_html(cfg, suite, v)
        p.append(f'<tr><td class="nw">{e(b["id"])}</td><td>{e(b["title"].replace(chr(96), ""))}<div class="small">{e(b["source_ref"])}</div></td>'
                 f'<td class="cot-nho">{_cell_html(test_case["steps"])}</td><td class="cot-nho">{_cell_html(test_case["expected"])}</td>'
                 f'<td>{_badge(v["status"])}</td><td>{ev}</td><td>{bug_cell}</td><td class="num">{run_count(data, b["number"])}</td></tr>')
    p.append("</tbody></table></div><div class=\"thanh-keo\"><div></div></div></div>")
    if suite != "smoke":
        p.append(_bug_summary_html(cfg, suite, new_text, table))
    p.append('<h2>Lịch sử các lượt</h2><div class="wrap"><table><thead><tr><th>Lượt</th><th>Build</th><th>Thời điểm</th><th>Người chạy</th><th>Kết quả</th><th>Kết luận</th></tr></thead><tbody>')
    for l in reversed(data["runs"]):
        p.append(f"<tr><td>{l['number']}</td><td>{e(l['build'])}</td><td>{e(l['timestamp'])}</td><td>{e(l['run_by'])}</td>"
                 f"<td>{e(_count_statuses(l))}</td><td>{_verdict_badge(l['verdict'])}</td></tr>")
    p.append("</tbody></table></div>")
    entries = data["runs"][-MATRIX_RUNS:]
    p.append(f"<h2>Từng case qua các lượt <span class='small'>(tối đa {MATRIX_RUNS} lượt gần nhất)</span></h2><div class='wrap'><table><thead><tr><th>ID</th>"
             + "".join(f"<th>Lượt {l['number']}<div class='small'>{e(l['build'])}</div></th>" for l in entries) + "</tr></thead><tbody>")
    for b in table:
        p.append(f"<tr><td class='nw'>{e(b['id'])}</td>" + "".join(f"<td>{_badge(l['results'].get(b['number'], {}).get('status', NOT_RUN))}</td>" for l in entries) + "</tr>")
    p.append("</tbody></table></div>")
    p.append('<p class="note">Các bước và Kết quả mong đợi lấy từ test case gốc. Bị chặn: chưa test được vì bug khác (xem cột Bug). Số lần chạy: số lượt có kết luận Đạt, Đạt kèm lỗi đã biết, Đạt kèm ý phụ sai hoặc Không đạt. '
             "Lượt Không kết luận (script lỗi, phiên hết hạn, thiếu dữ liệu) và Chưa chạy không tính.</p></main></body></html>")
    return "".join(p)


def build_pages(cfg, suite="smoke"):
    data = read_results_data(cfg, suite)
    table = read_table(cfg, suite)
    md_file, html_file = page_files(cfg, suite)
    md_file.write_text(build_md(cfg, suite, data, table), encoding="utf-8")
    html_file.write_text(build_html(cfg, suite, data, table), encoding="utf-8")
    from . import bug_page

    bug_page.build_all(cfg)  # mỗi BUG-nnn.md có trang BUG-nnn.html cạnh nó
    return md_file, html_file
