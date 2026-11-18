"""Lối tắt build báo cáo v2 của Banking Lite. Logic build nằm DUY NHẤT trong skill:
.claude/skills/feature-exploration-report/scripts/build-embed.py (chèn CSS + font chuẩn, vẽ sơ đồ từ _src/so-do/*.json).
Chạy: python -X utf8 _src/build-embed.py   (từ evidence/banking-lite) — thêm tham số sẽ được chuyển tiếp, vd --review <thư_mục>.
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKILL = os.path.join(ROOT, '..', '..', '.claude', 'skills', 'feature-exploration-report', 'scripts', 'build-embed.py')
sys.exit(subprocess.call([sys.executable, '-X', 'utf8', SKILL,
                          '--src', os.path.join(HERE, 'bao-cao-kham-pha-v2.src.html'),
                          '--out', os.path.join(ROOT, 'bao-cao-kham-pha-v2.html'),
                          '--shots', os.path.join(ROOT, 'screenshots')] + sys.argv[1:]))
