"""Ghép khung đầu của khuôn skill + body.html -> gui-tham-dinh.src.html
Chạy:  python -X utf8 assemble.py   rồi chạy build-embed.py của skill.
Sơ đồ không vẽ ở đây: body.html có <div class="diag" data-so-do="so-do/*.json">, build-embed.py vẽ bằng ve-so-do.py
(2026-11-18 chuyển từ SVG vẽ tay sang JSON để giữ đúng mẫu đã chốt). Sửa sơ đồ = sửa file trong so-do/.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
TEMPLATE = os.path.join(REPO, '.claude', 'skills', 'feature-exploration-report', 'assets', 'report-template.src.html')

tpl = io.open(TEMPLATE, encoding='utf-8').read()
head = tpl[:tpl.index('<body>')].replace('{{TÊN_BÁO_CÁO}}', 'Báo cáo khám phá — Gửi thẩm định')
body = io.open(os.path.join(HERE, 'body.html'), encoding='utf-8').read()
html = head + '<body>\n' + body + '\n<script>/* build-embed.py sẽ thay khối này */</script>\n</body>\n</html>\n'
out = os.path.join(HERE, 'gui-tham-dinh.src.html')
io.open(out, 'w', encoding='utf-8', newline='').write(html)
print('written', out, len(html))
