# Copyright (C) 2025 natsuu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from datetime import datetime
from pathlib import Path
import shutil
from ssl import SSLError
import subprocess
import sys
from zipfile import ZipFile
import requests
from tqdm import tqdm
import zipfile
import hashlib
import json

sys.stdout.reconfigure(encoding="utf-8")  # type: ignore

install_path = Path("./install")
tmp_path = Path("./tmp")
python_dir = install_path / "python"
mirror = "https://mirrors.ustc.edu.cn/pypi/simple"

shutil.rmtree(install_path / "src", ignore_errors=True)

Path(install_path).mkdir(parents=True, exist_ok=True)
Path(tmp_path).mkdir(parents=True, exist_ok=True)


def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)  # stream=True 分块下载
        total_size = int(response.headers.get("Content-Length", 0))  # 总字节数

        progress_bar = tqdm(
            total=total_size, unit="B", unit_scale=True, desc=str(save_path)
        )

        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):  # 1MB
                if chunk:
                    f.write(chunk)
                    progress_bar.update(len(chunk))

        progress_bar.close()
        if total_size != 0 and progress_bar.n != total_size:
            print(f"❌ 下载失败：{save_path} 大小不匹配")
        else:
            print(f"✅ 下载完成：{save_path}")
    except SSLError as e:
        print(f"❌ 下载失败：{save_path}，请检查代理设置！\n{e}")


def copy_files():
    shutil.copy2("./LICENSE", install_path / "LICENSE")
    shutil.copy2("./tools/start.bat", install_path / "start.bat")
    shutil.copytree("./src", install_path / "src")


def install_python_embed():
    python_embed_zip_path = tmp_path / "python-3.12.9-embed-amd64.zip"
    python_embed_url = (
        "https://mirrors.huaweicloud.com/python/3.12.9/python-3.12.9-amd64.zip"
    )
    if not python_embed_zip_path.exists():
        print(f"Downloading Python embed zip from {python_embed_url}...")
        download_file(python_embed_url, python_embed_zip_path)
        print("Download completed.")
    else:
        print("Python embed zip already exists.")

    with ZipFile(python_embed_zip_path, "r") as zip_ref:
        zip_ref.extractall(install_path / "python")


def install_dependencies():
    res = subprocess.run(
        [
            str(python_dir / "python.exe"),
            "download_deps.py",
        ]
    )
    if res.returncode != 0:
        print(
            "\033[93m[WARNING]\033[0m {}".format("download whl files failed"),
            file=sys.stderr,
        )
        # sys.exit(1)
        print("Try to install dependencies with local whl files...")

    # 从deps目录安装所有whl文件
    deps_dir = Path("./deps")
    whl_files = list(deps_dir.glob("*.whl"))
    if not whl_files:
        print(
            "\033[93m[WARNING]\033[0m {}".format(
                "no whl files found in deps directory"
            ),
            file=sys.stderr,
        )
        sys.exit(1)

    res = subprocess.run(
        [
            str(python_dir / "python.exe"),
            "-m",
            "pip",
            "install",
            "--no-index",
            "--find-links",
            str(deps_dir),
            "--no-warn-script-location",
        ]
        + [str(f) for f in whl_files]
    )
    if res.returncode != 0:
        print(
            "\033[93m[WARNING]\033[0m {}".format("install whl files failed"),
            file=sys.stderr,
        )
        sys.exit(1)


def compress_files():
    now = datetime.now()
    fname = f"shp-check-{now.strftime('%Y%m%d_%H%M%S')}.zip"
    print(f"开始压缩文件: {fname}")
    zipfile_path = Path("./" + fname)
    with ZipFile(zipfile_path, "w", zipfile.ZIP_LZMA) as zipf:
        for files in Path(install_path).rglob("*"):
            zipf.write(
                files,
                files.relative_to(install_path.parent),
            )

    print(f"✅ 打包完成：{zipfile_path}")


def get_file_md5(fname):
    if not Path(fname).exists():
        return ""
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_dir_md5(dir_path):
    if not Path(dir_path).exists():
        return ""
    hash_md5 = hashlib.md5()
    # Sort to ensure consistent order
    for path in sorted(Path(dir_path).rglob("*")):
        if path.is_file():
            # Hash the relative path to detect file moves/renames
            try:
                rel_path = path.relative_to(dir_path)
                hash_md5.update(str(rel_path).encode())
                with open(path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)
            except (ValueError, OSError):
                continue
    return hash_md5.hexdigest()


STATE_FILE = install_path / "install_state.json"


def load_state():
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=4)


if __name__ == "__main__":
    copy_files()

    print("Checking installation state...")
    current_req_hash = get_file_md5("requirements.txt")
    current_deps_hash = get_dir_md5("deps")
    current_python_hash = get_dir_md5(python_dir)

    state = load_state()

    # Check if we can skip installation
    # We need to ensure python_dir exists and is not empty (hash not empty)
    if (
        current_python_hash
        and state.get("requirements_hash") == current_req_hash
        and state.get("deps_hash") == current_deps_hash
        and state.get("python_hash") == current_python_hash
    ):
        print(
            "Dependencies and Python environment are up to date. Skipping installation."
        )
    else:
        install_python_embed()
        install_dependencies()

        # Update state
        print("Updating installation state...")
        new_state = {
            "requirements_hash": get_file_md5("requirements.txt"),
            "deps_hash": get_dir_md5("deps"),
            "python_hash": get_dir_md5(python_dir),
        }
        save_state(new_state)

    compress_files()
