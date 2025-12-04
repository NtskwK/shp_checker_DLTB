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

install_dir:=install
python_version:=3.12.9
tmp_dir:=tmp
app_name:=AppTemplate


ifeq ($(OS),Windows_NT)
    TIMESTAMP := $(shell powershell -Command "(Get-Date).ToString('yyyyMMdd_HHmm')")
else
    TIMESTAMP := $(shell date +$(TIME_FORMAT))
endif

all: packup

check-uv:
	pip install uv

configure: check-uv
	rm -rf .venv
	uv sync

clean:
	cmd /c rmdir /s /q $(install_dir)

packup: check-uv
# 	download python embed
	python tools/download_python.py --install_path=$(install_dir) --is_embed=true --version=$(python_version) --tmp_dir=$(tmp_dir)

# 	compile requirements.txt
	uv pip compile --output-file=requirements.txt pyproject.toml
# 	install packages
	uv pip install -r .\requirements.txt --target .\$(install_dir)\python\Lib
# 	copy files
	cp -p ./tools/start.bat ./$(install_dir)/start.bat
	cp -r ./src ./$(install_dir)/src
	cp -p ./LICENSE ./$(install_dir)/LICENSE
	mkdir dist -p
	cd $(install_dir) && zip -r ../dist/$(app_name)_$(TIMESTAMP).zip ./*
