"""Đọc cấu hình dự án và tài khoản test.

Quy ước `.env` (gốc repo, không commit): `<TIỀN_TỐ>_URL`, `<TIỀN_TỐ>_<MÃ>_USER`, `<TIỀN_TỐ>_<MÃ>_PASSWORD`.
Tiền tố do cấu hình dự án quy định (`tien_to_env`), ví dụ BANKING_LITE.
Mật khẩu chỉ được lấy qua `CauHinh.thong_tin_dang_nhap`, và chỉ module `phien` (đăng nhập) gọi hàm này.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # gốc repo; các hàm bên dưới đọc biến này lúc gọi

REQUIRED_KEYS = ["env_prefix", "default_url", "login"]
REQUIRED_LOGIN_KEYS = ["id_labels", "button_labels", "login_api", "session_check_api", "session_minutes"]


class ConfigError(Exception):
    pass


def read_env():
    path = ROOT / ".env"
    if not path.exists():
        return {}
    results = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        results[key.strip()] = value.strip().strip('"').strip("'")
    return results


def current_project():
    f = ROOT / ".du-an-hien-tai"
    if not f.exists():
        raise ConfigError("Chưa có .du-an-hien-tai; truyền --project <slug>.")
    return f.read_text(encoding="utf-8").strip()


class Config:
    def __init__(self, project, data, env):
        self.project = project
        self.data = data
        self._env = env
        self.env_prefix = data["env_prefix"]
        self.url = (env.get(f"{self.env_prefix}_URL") or data["default_url"]).rstrip("/")
        login_cfg = data["login"]
        self.id_labels = login_cfg["id_labels"]
        self.button_labels = login_cfg["button_labels"]
        self.login_api = login_cfg["login_api"]
        self.session_check_api = login_cfg["session_check_api"]
        self.session_minutes = login_cfg["session_minutes"]
        self.max_consecutive_failures = login_cfg.get("max_consecutive_failures", 9)

    @property
    def project_dir(self):
        return ROOT / "testing" / self.project

    @property
    def test_data(self):
        """Dữ liệu test của dự án (id hồ sơ nháp…), file `testing/<dự-án>/auto-data.json`, không bắt buộc."""
        f = self.project_dir / "auto-data.json"
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}

    @property
    def sessions_dir(self):
        return ROOT / ".phien-dang-nhap" / self.project

    @property
    def screenshots_dir(self):
        return ROOT / "evidence" / self.project / "chay-test"

    def available_accounts(self):
        code = set()
        pattern = re.compile(rf"{re.escape(self.env_prefix)}_([A-Za-z0-9]+)_PASSWORD")
        for key in self._env:
            m = pattern.fullmatch(key)
            if m:
                code.add(m.group(1).upper())
        return sorted(code)

    def get_credentials(self, code):
        """(tên đăng nhập, mật khẩu). Chỉ dùng trong module phien."""
        code = code.upper()
        password = self._env.get(f"{self.env_prefix}_{code}_PASSWORD")
        if password is None:
            raise ConfigError(f"Không có tài khoản {code} trong .env. Hiện có: {', '.join(self.available_accounts()) or '(chưa có)'}")
        return self._env.get(f"{self.env_prefix}_{code}_USER") or code, password


def load(project=None):
    project = project or current_project()
    f = ROOT / "testing" / project / "auto-config.json"
    if not f.exists():
        raise ConfigError(
            f"Chưa có {f.relative_to(ROOT)}. Tạo file này theo mẫu ở docs/chay-test-tu-dong.md (mục Thêm dự án mới)."
        )
    data = json.loads(f.read_text(encoding="utf-8"))
    missing = [k for k in REQUIRED_KEYS if k not in data]
    if not missing:
        missing = [f"dang_nhap.{k}" for k in REQUIRED_LOGIN_KEYS if k not in data["login"]]
    if missing:
        raise ConfigError(f"{f.relative_to(ROOT)} thiếu khóa: {', '.join(missing)}")
    return Config(project, data, read_env())
