"""Đóng gói bộ thực hành từ các tệp nguồn, không kèm dữ liệu chạy thử."""
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

base = Path(__file__).resolve().parent
source = base / "hadoop-compose"
files = ["README.md", "compose.yaml", "config", "mapper.py", "reducer.py",
         "run-job.sh", "data/d1.txt", "data/d2.txt"]
with ZipFile(base / "hadoop-compose.zip", "w", ZIP_DEFLATED) as archive:
    for name in sorted(files):
        entry = ZipInfo("hadoop-compose/" + name, (2026, 9, 17, 0, 0, 0))
        entry.compress_type = ZIP_DEFLATED
        entry.external_attr = 0o100644 << 16
        archive.writestr(entry, (source / name).read_bytes())
