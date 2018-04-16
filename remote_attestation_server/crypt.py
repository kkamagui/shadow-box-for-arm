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

from Crypto.Cipher import AES
import sys

#key=52DA55AC3CB64D4C905F5688B47B7F8D
#iv =13BE10DC8C89F640CB1B1771C668419F
key = "\x52\xDA\x55\xAC\x3C\xB6\x4D\x4C\x90\x5F\x56\x88\xB4\x7B\x7F\x8D"
IV = "\x13\xBE\x10\xDC\x8C\x89\xF6\x40\xCB\x1B\x17\x71\xC6\x68\x41\x9F"

# Encrypt file with the key.
def encrypt_file(in_filename, out_filename):
	mode = AES.MODE_CBC
	encryptor = AES.new(key, mode, IV=IV)
	in_file = open(in_filename, "rb")
	in_data = in_file.read()
	# 16byte padding
	if (len(in_data) % 16 != 0):
		print("Length %d, Padding %d byte" %  (len(in_data), 16 - (len(in_data) % 16)))
		for i in range(0, 16 - (len(in_data) % 16)):
			in_data = in_data + "\x00"

	cipher_text = encryptor.encrypt(in_data)

	out_file = open(out_filename, "wb")
	out_file.write(cipher_text)
	in_file.close()
	out_file.close()

# Decrypt file with the key.
def decrypt_file(in_filename, out_filename):
	mode = AES.MODE_CBC
	decryptor = AES.new(key, mode, IV=IV)
	in_file = open(in_filename, "rb")
	in_data = in_file.read()

	plain_text = decryptor.decrypt(in_data)

	out_file = open(out_filename, "wb")
	out_file.write(plain_text)
	in_file.close()
	out_file.close()

# Decrypt data.
def decrypt(enc_data):
	mode = AES.MODE_CBC
	decryptor = AES.new(key, mode, IV=IV)

	plain_text = decryptor.decrypt(enc_data)

	return plain_text

# Encrypt data.
def encrypt(enc_data):
	mode = AES.MODE_CBC
	encryptor = AES.new(key, mode, IV=IV)

	plain_text = encryptor.encrypt(enc_data)

	return plain_text

# Show help
def print_help():
	print("ex>  -e  infile outfile : Encrypt file\n"
		  "     -d  infile outfile : Decrypt file\n");

# Main
if __name__ == "__main__":
	if (len(sys.argv) < 4):
		print_help()
		sys.exit(0)

	if (sys.argv[1] == "-e"):
		encrypt_file(sys.argv[2], sys.argv[3])
	elif (sys.argv[1] == "-d"):
		decrypt_file(sys.argv[2], sys.argv[3])
	else:
		print_help()
