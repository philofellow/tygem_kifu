#!/usr/bin/python

import socket, os, sys
import util


class KifuList:
	pre_bytes = '\x00\x20\x02\x46\x00\x00\x00\x00\x00\x1e\x00'
	cmd_len = 32
	def __init__(self, sock):
		self.sock = sock

	def GetKifuList(self, player_id):
		# todo accept chinese character and translater to bytes
		
		print 'begin download kifu list for [' \
				+ player_id.decode('gbk') + ']' \
				+ ' or ' + util.GetByteStr(player_id)

		cmd = self.pre_bytes + player_id
		while len(cmd) < self.cmd_len:
			cmd += '\x00'
		print 'send command:'
		print util.GetByteStr(cmd)
		print 'to the tygem server'
		self.sock.send(cmd)

    	# Look for the response
		amount_received = 0
		amount_expected = 10000
		print 'kifu list:'
		while amount_received < amount_expected:
			data = self.sock.recv(1024)
			amount_received += len(data)
			print data

