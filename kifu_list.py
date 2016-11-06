#!/usr/bin/python

import socket, os, sys, time
import util


class KifuList:

	def __init__(self, sock):
		self.sock = sock
		self.recved = 0

	def GetKifu(self, kifu_index):
		cmd = '\x00\x08\x02\x4d' + kifu_index
		while len(cmd) < 8:
			cmd += '\x00'

		print 'send command:'
		print util.GetByteStr(cmd)
		print 'to the tygem server'
		self.sock.send(cmd)

    	# Look for the response
		received = 0
		print 'received kifu below:'
		kifu = ''
		while True:
			kifu += self.sock.recv(1024)
			if kifu.find('\\GE\n') != -1:
				self.Save(kifu)	
				break


	def Save(self, data):
		print '=============== save'
		print data
		begin = data.find('\\HS')
		print begin
		end = data.find('\\GE') + 3
		print end 
		f = open(str(time.time()), 'w')
		f.write(data[begin:end])
		f.close()

	def GetKifuList(self, player_id):
		pre_bytes = '\x00\x20\x02\x46\x00\x00\x00\x00\x00\x1e\x00'
		cmd_len = 32
		resp_len = 92

		print 'begin download kifu list for [' \
				+ player_id.decode('gbk') + ']' \
				+ ' or ' + util.GetByteStr(player_id)

		# build cmd for querying kifu list
		cmd = pre_bytes + player_id
		while len(cmd) < cmd_len:
			cmd += '\x00'
		
		# send command
		print 'send command:'
		print util.GetByteStr(cmd)
		print 'to the tygem server'
		self.sock.send(cmd)

		kifu_list = []
		kifu_received = 0
		print 'kifu list:'
		while kifu_received < 10:
			data = self.sock.recv(resp_len)
			kifu_received += 1
			kifu_list.append(data[0:4])
			print util.GetByteStr(data[0:4])

		return kifu_list





