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

from socket import *
from select import select
import struct
import sys
import time
import random
# Import function from local library
from crypt import decrypt
from crypt import encrypt

# Inforation of Raspberry Pi
HOST = "192.168.3.28"
PORT = 8885
# Magic for the remote attestation
MAGIC = "== SHADOW-BOX RA DATA =="
HTML_TEMPLATE_MAGIC = "<!-- shadow_box_data -->"
html_buffer = ""

# Add a table row.
def add_table_row(row_sum, row):
	row_sum = row_sum + '<tr calss="info">\n' + row + '</tr>\n'
	return row_sum

# Add a table column.
def add_table_column(column_sum, data):
	column_sum = column_sum + '<td>  %s </td>\n' % data
	return column_sum

# Add an error message.
def add_error_info(index, ip, error_log):
	column_sum = ""
	row_sum = ""
	column_sum = add_table_column(column_sum, index)
	column_sum = add_table_column(column_sum, ip)
	column_sum = add_table_column(column_sum, error_log)
	column_sum = add_table_column(column_sum, "-")
	column_sum = add_table_column(column_sum, "-")
	row_sum = add_table_row(row_sum, column_sum)
	return row_sum

# Create index.html file with the templete file.
def create_index_html(row_sum):
	fp_temp = open("index.html.template", "r")
	fp_real = open("index.html", "w")

	template = fp_temp.read()
	template = template.replace(HTML_TEMPLATE_MAGIC, row_sum)
	fp_temp.close()

	fp_real.write(template)
	fp_real.close()

# Main
def main():
	client_socket = socket(AF_INET, SOCK_STREAM)
	client_socket.settimeout(10)
	status_map = {0:"Verifying", 1:"Verification Success", 2:"Kernel Attack Detection"}

	print "Try to connect...",

	try:
		client_socket.connect((HOST, PORT))
	except Exception as e:
		print("Server connect fail IP=%s PORT=%d" % (HOST, PORT))
		row = add_error_info("1", HOST, "Connection failed")
		create_index_html(row)
		sys.exit()

	print "Success"
	row_sum = ""
	column_sum = ""

	column_sum = add_table_column(column_sum, "1")
	column_sum = add_table_column(column_sum, HOST)

	try:
		server_nonce = random.randrange(0, 0xffffffff)
		print "    [*] Nonce: %d" % server_nonce

		packer = struct.Struct("<24s I I")
		unpacker = struct.Struct("<24s I i Q Q")

		print "Request Kernel Status to Shadow-box...",
		send_data = packer.pack(MAGIC, server_nonce, 0)
                send_data = encrypt(send_data)
		client_socket.send(send_data)

		recv_data = client_socket.recv(unpacker.size)

		print "Complete"

		# Decrypt and show messages
		recv_data = decrypt(recv_data)
		unpacked_data = unpacker.unpack(recv_data)
		if (unpacked_data[0] != MAGIC):
			print("    [*] Magic is different, [%s] [%s]" % (unpacked_data[0], MAGIC))
			add_error_info("1", HOST, "Detection of Malware Attack")
			sys.exit();

		if (unpacked_data[1] != server_nonce):
			print("Nonce is different, server nonce %d, recved nonce %d\n" % (server_nonce, unpacked_data[1]))
			add_error_info("1", HOST, "Detection of Malware Attack")
			sys.exit(0)
		
		print "    [*] Status: %s" % status_map.get(unpacked_data[2])
		column_sum = add_table_column(column_sum, status_map.get(unpacked_data[2]))

		if (unpacked_data[3] != 0):
			t = time.localtime(unpacked_data[3])
			print "    [*] Verification Success Time: %04d %02d %02d %02d:%02d:%02d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
			data = "%04d/%02d/%02d %02d:%02d:%02d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
			column_sum = add_table_column(column_sum, data)
		else:
			column_sum = add_table_column(column_sum, "-")

		if (unpacked_data[4] != 0):
			t = time.localtime(unpacked_data[4])
			print "    [*] Attack Detection Time: %04d %02d %02d %02d:%02d:%02d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
			data = "%04d/%02d/%02d %02d:%02d:%02d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
			column_sum = add_table_column(column_sum, data)
		else:
			column_sum = add_table_column(column_sum, "-")

		row_sum = add_table_row(row_sum, column_sum)

		create_index_html(row_sum)

	except KeyboardInterrupt:
		client_socket.close()
		sys.exit()

if __name__ == "__main__":
	main()
