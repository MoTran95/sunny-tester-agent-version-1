#!/usr/bin/env python3
"""Kiểm thông tin của dự án này không lẫn sang chỗ dùng chung hoặc sang dự án khác.

    python -X utf8 scripts/kiem-tra-lan-du-an.py

Mỗi dự án có "dấu hiệu nhận ra": tên thư mục (slug), tiền tố `.env`, tên miền của địa chỉ test, tên hiển thị
(bảng trong memories/project/overview.md), mã tài khoản test (khóa `<TIỀN_TỐ>_<MÃ>_PASSWORD` trong .env.example),
nhãn ô đăng nhập (`login.id_labels` trong auto-config.json), mã tính năng dạng `<MÃ>-S01`, `<MÃ>-R02` (khóa `tien_to`
trong truy-vet-cau-hinh.json).
Hai kiểm tra:
1. Chỗ dùng chung KHÔNG được chứa dấu hiệu của bất kỳ dự án nào: skill (`.claude/skills/`), khuôn dùng chung
   (`srs/*.md` ở gốc, `testing/_template*`), script tạo dự án (`scripts/tao-du-an.py`).
2. Thư mục riêng của dự án P (`memories/modules/P`, `srs/P`, `testing/P`, `evidence/P`) KHÔNG được chứa dấu hiệu của dự án Q khác.
Chỉ đọc file văn bản (md, json, py, txt, csv); bỏ qua HTML sinh tự động. Thoát mã 1 nếu có chỗ lẫn.
"""
import json
import os
import re
import sys
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT_EXT = (".md", ".json", ".py", ".txt", ".csv")
SKIP_DIRS = {"__pycache__", ".git", "node_modules"}


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return ""


def projects():
    base = os.path.join(ROOT, "testing")
    if not os.path.isdir(base):
        return []
    return sorted(d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)))


def display_names():
    """slug → tên hiển thị, đọc bảng dự án trong memories/project/overview.md."""
    names = {}
    for line in read(os.path.join(ROOT, "memories", "project", "overview.md")).splitlines():
        m = re.match(r"\|\s*`([a-z0-9-]+)`\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            names[m.group(1)] = m.group(2)
    return names


def markers(slug, names, env_example):
    """Danh sách (nhãn, mẫu regex) nhận ra dự án `slug`."""
    found = [("tên thư mục", re.compile(r"(?<![\w-])" + re.escape(slug) + r"(?![\w-])", re.I))]
    cfg_path = os.path.join(ROOT, "testing", slug, "auto-config.json")
    prefix = ""
    if os.path.exists(cfg_path):
        try:
            cfg = json.loads(read(cfg_path))
        except ValueError:
            cfg = {}
        prefix = str(cfg.get("env_prefix", ""))
        host = urlparse(str(cfg.get("default_url", ""))).hostname or ""
        if host and "<" not in host:
            found.append(("tên miền địa chỉ test", re.compile(re.escape(host), re.I)))
        for label in (cfg.get("login") or {}).get("id_labels", []):
            label = str(label).strip()
            if label and "<" not in label and len(label) >= 6:
                found.append((f"nhãn ô đăng nhập '{label}'", re.compile(r"(?<![\w])" + re.escape(label) + r"(?![\w])", re.I)))
    for tv in sorted((os.path.join(ROOT, "testing", slug, d, "truy-vet-cau-hinh.json")
                      for d in (os.listdir(os.path.join(ROOT, "testing", slug)) if os.path.isdir(os.path.join(ROOT, "testing", slug)) else []))):
        if os.path.exists(tv):
            try:
                code = str(json.loads(read(tv)).get("tien_to", "")).strip()
            except ValueError:
                code = ""
            if code:
                found.append((f"mã tính năng {code}", re.compile(r"(?<![\w-])" + re.escape(code) + r"-(?:S\d\d|R\d\d|M\d\d|Q\d\d|E\d\d)")))
    if not prefix:
        prefix = slug.upper().replace("-", "_")
    found.append(("tiền tố .env", re.compile(r"(?<![\w])" + re.escape(prefix) + r"_")))
    name = names.get(slug)
    if name and "<" not in name and len(name) >= 4:
        found.append(("tên hiển thị", re.compile(r"(?<![\w])" + re.escape(name) + r"(?![\w])", re.I)))
    for m in re.finditer(r"^" + re.escape(prefix) + r"_([A-Za-z0-9]+)_PASSWORD", env_example, re.M):
        code = m.group(1)
        if len(code) >= 4:
            found.append((f"mã tài khoản {code}", re.compile(r"(?<![\w])" + re.escape(code) + r"(?![\w])")))
    return found


def text_files(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.lower().endswith(TEXT_EXT):
                yield os.path.join(dirpath, name)


def scan(files, other_markers):
    """[(file tương đối, số dòng, nhãn, dự án)] chỗ chứa dấu hiệu của dự án khác."""
    hits = []
    for path in files:
        text = read(path)
        for slug, marks in other_markers.items():
            for label, pattern in marks:
                m = pattern.search(text)
                if m:
                    line = text.count("\n", 0, m.start()) + 1
                    hits.append((os.path.relpath(path, ROOT).replace(os.sep, "/"), line, label, slug))
                    break
    return hits


def main():
    slugs = projects()
    names = display_names()
    env_example = read(os.path.join(ROOT, ".env.example"))
    all_markers = {s: markers(s, names, env_example) for s in slugs}
    problems = []
    skills_dir = os.path.join(ROOT, ".claude", "skills")
    shared = list(text_files(skills_dir)) if os.path.isdir(skills_dir) else []
    srs_root = os.path.join(ROOT, "srs")
    if os.path.isdir(srs_root):
        shared += [os.path.join(srs_root, f) for f in os.listdir(srs_root) if f.lower().endswith(TEXT_EXT)]
    test_root = os.path.join(ROOT, "testing")
    if os.path.isdir(test_root):
        shared += [os.path.join(test_root, f) for f in os.listdir(test_root) if f.startswith("_template") and f.lower().endswith(TEXT_EXT)]
    shared.append(os.path.join(ROOT, "scripts", "tao-du-an.py"))
    for f, line, label, slug in scan([x for x in shared if os.path.exists(x)], all_markers):
        problems.append(f"chỗ dùng chung chứa thông tin dự án `{slug}` ({label}): {f}:{line}")
    for p in slugs:
        folders = [os.path.join(ROOT, d, p) for d in ("memories/modules", "srs", "testing", "evidence")]
        files = [f for folder in folders if os.path.isdir(folder) for f in text_files(folder)]
        others = {s: m for s, m in all_markers.items() if s != p}
        for f, line, label, slug in scan(files, others):
            problems.append(f"thư mục dự án `{p}` chứa thông tin dự án `{slug}` ({label}): {f}:{line}")
    if problems:
        print(f"{len(problems)} chỗ thông tin dự án bị lẫn:")
        for x in problems[:30]:
            print("  -", x)
        if len(problems) > 30:
            print(f"  … và {len(problems) - 30} chỗ nữa")
        return 1
    print(f"Không lẫn thông tin giữa các dự án ({len(slugs)} dự án, skill dùng chung sạch).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
