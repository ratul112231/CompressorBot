#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in < https://github.com/1Danish-00/CompressorBot/blob/main/License> .

from . import *

try:
    APP_ID = config("36172902", cast=int)
    API_HASH = config("c3a7e1d518f38928a21865e75458b62a")
    BOT_TOKEN = config("8222385318:AAH6AK3nSOX2CPxLNAr9CQtqhJZfM-8Jhro")
    OWNER = config("7831735222", default=6992010963, cast=int)
    LOG = config("-1003642494316", cast=int)
except Exception as e:
    LOGS.info("@smmpanelotp")
    LOGS.info("@smmpanelotp")
    LOGS.info(str(e))
    exit(1)
