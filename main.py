#!/usr/bin/python

import socket, os, sys
import util, cfg
from kifu_list import *
from players import *

class TygemKifu:
	
	def InitSocket(self, ip, port):
		# Create a TCP/IP socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# Connect the socket to the port where the server is listening
		server_address = (ip, port)
		print 'connecting to %s port %s' % server_address
		self.sock.connect(server_address)
	
	def ShutDown(self):
		print 'closing socket'
		self.sock.close()

	def Run(self):
		try:
			self.InitSocket(cfg.IP, cfg.PORT)
			player = Players().GetID(cfg.TEST_PLAYER2)
			print 'player name = ' + cfg.TEST_PLAYER2
			print 'player id byte = ' + util.GetByteStr(player)


			kifu_list = KifuList(self.sock)
			kifu_list.GetKifuList(player)
		finally:
			self.ShutDown()

if __name__ == "__main__":
	app = TygemKifu()
	app.Run()
