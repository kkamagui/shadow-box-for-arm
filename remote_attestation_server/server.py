#!/usr/bin/python
# -*- coding: utf8 -*-
#
#                      Shadow-Box for ARM
#                      ------------------
#             ARM TrustZone-Based Kernel Protector
#
#               Copyright (C) 2018 Seunghun Han
#     at National Security Research Institute of South Korea
#

# This software has dual license (MIT and GPL v2). See the GPL_LICENSE and
# MIT_LICENSE file.

import os
import time
import sys
import subprocess

# Start a simple web server.
server = subprocess.Popen('python -m SimpleHTTPServer 8888', shell=True)

# Update the status of Raspberry Pi.
try:
	while True:
		time.sleep(5)
		os.system("python ./get_shadow_box_status.py")
except:
	server.kill()
	sys.exit(0)
