# AGPL-3.0 License
# https://github.com/MAA1999/M9A
"""
安装pip和依赖库的脚本

该脚本用于嵌入式Python环境中，执行以下操作:
1. 下载并安装pip
"""

import os
import sys
import urllib.request
import subprocess


def install_pip():
    print("Setting up pip...")

    get_pip_url = "https://bootstrap.pypa.io/get-pip.py"
    get_pip_path = os.path.join(os.path.dirname(__file__), "get-pip.py")
    if not os.path.exists(get_pip_path):
        print(f"Downloading {get_pip_url}...")
        urllib.request.urlretrieve(get_pip_url, get_pip_path)
    else:
        print("get-pip.py already exists.")

    print("Install pip...")
    subprocess.check_call([sys.executable, get_pip_path, "--no-warn-script-location"])

    print("pip installed.")


if __name__ == "__main__":
    install_pip()
