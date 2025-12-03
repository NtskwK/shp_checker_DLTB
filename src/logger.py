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
import sys
from loguru import logger as _logger

date_time = datetime.now().strftime("%Y%m%d-%H%M%S")

_logger.remove()
_logger.add(
    f"logs/{date_time}.log",
    level="INFO",
    rotation="10 MB",
    retention="10 days",
    format="[<level>{level: <6}</level>] <level>{message}</level>",
)

_logger.add(
    sys.stdout,
    level="DEBUG",
    colorize=True,
    format="[<level>{level: <6}</level>] <level>{message}</level>",
)

_logger.add(
    f"logs/调试/{date_time}.log",
    level="DEBUG",
    rotation="10 MB",
    retention="10 days",
    format="<green>{time:HH:mm:ss}</green> | <level>{level: <6}</level> | <cyan>{file: >8}</cyan>:<cyan>{line: <3}</cyan> | <level>{message}</level>",
)

logger = _logger.bind()
logger.info("Logger initialized")
