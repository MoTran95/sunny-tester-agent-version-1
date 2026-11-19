"""Bộ đếm số lần đăng nhập sai liên tiếp, để không bao giờ chạm ngưỡng chặn của hệ thống đang test.

Quy tắc (người dùng chốt trần 9 lần ngày 2026-11-19, memories/project/tu-dong-hoa-test.md):
- Trần 9 lần sai TỔNG CỘNG kể từ lần bộ đếm về 0. Đăng nhập đúng KHÔNG đưa bộ đếm về 0: ngày 2026-11-19 trên staging,
  đăng nhập đúng xen giữa các ca mà P100001 vẫn bị chặn ở lần sai thứ 11 cộng dồn (khác TL-06 của BA).
- Bộ đếm chỉ về 0 khi hết thời gian chặn sau một lần 429 (giả định theo TL-09, chưa kiểm) hoặc người dùng đặt lại bằng tay
  (`python -X utf8 scripts/run_tests.py --reset-failure-counter`).
- Trước mỗi lần cố ý nhập sai, thư viện hỏi bộ đếm; vượt trần thì từ chối (ca thành "Không kết luận").
- Hệ thống trả 429 (đang chặn) thì ghi mốc hết chặn; các ca nhập sai dừng tới mốc đó.

Bộ đếm chỉ đếm những gì thư viện này gửi; lần nhập tay của người khác không thấy được.
Tệp: `.phien-dang-nhap/<dự-án>/failure-counter.json` (đã .gitignore).
"""
import json
import time

DEFAULT_MAX = 9
DEFAULT_BLOCK_MINUTES = 5


def _file(cfg):
    return cfg.sessions_dir / "failure-counter.json"


def read(cfg):
    try:
        state = json.loads(_file(cfg).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"consecutive_failures": 0, "blocked_until": 0}
    if state.get("blocked_until", 0) and time.time() >= state["blocked_until"]:
        state = {"consecutive_failures": 0, "blocked_until": 0}   # hết chặn: coi như đếm lại từ 0 (giả định theo TL-09)
        _write(cfg, state)
    return state


def reset(cfg):
    """Người dùng chắc chắn bộ đếm của hệ thống đã về 0 (đã chờ hết chặn, hoặc hệ thống mới)."""
    _write(cfg, {"consecutive_failures": 0, "blocked_until": 0})


def _write(cfg, state):
    cfg.sessions_dir.mkdir(parents=True, exist_ok=True)
    _file(cfg).write_text(json.dumps(state), encoding="utf-8")


def seconds_blocked(cfg):
    """Số giây còn bị chặn theo ghi nhận gần nhất (0 nếu không)."""
    return max(0, int(read(cfg).get("blocked_until", 0) - time.time()))


def refusal_reason(cfg):
    """None nếu được phép cố ý nhập sai thêm một lần; ngược lại câu giải thích vì sao từ chối."""
    state = read(cfg)
    wait = seconds_blocked(cfg)
    if wait:
        return f"hệ thống đang chặn đăng nhập theo ghi nhận trước đó, còn khoảng {wait} giây"
    maximum = cfg.max_consecutive_failures
    if state.get("consecutive_failures", 0) + 1 > maximum:
        return f"đã {state['consecutive_failures']} lần sai, thêm một lần nữa vượt trần {maximum} (đăng nhập đúng không đưa bộ đếm về 0; chờ hệ thống hết chặn hoặc đặt lại bằng tay nếu chắc chắn)"
    return None


def record(cfg, status):
    """Ghi kết quả một lần gửi form đăng nhập theo mã trả về của máy chủ."""
    state = read(cfg)
    if status in (400, 401):
        state["consecutive_failures"] = state.get("consecutive_failures", 0) + 1
    elif status == 429:
        state["consecutive_failures"] = cfg.max_consecutive_failures
        state["blocked_until"] = time.time() + DEFAULT_BLOCK_MINUTES * 60
    else:
        return
    _write(cfg, state)
