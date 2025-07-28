# SPDX-FileCopyrightText: 2025-present gjeodnd12165 <gjeodnd12165@gmail.com>
#
# SPDX-License-Identifier: MIT

from .server import mcp
from .raw_data import clone_raw_data_repo

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

def main():
    clone_raw_data_repo()
    mcp.run()

if __name__ == "__main__":
    main()