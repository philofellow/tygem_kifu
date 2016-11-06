#!/usr/bin/python

import os, sys
import util, cfg


class Players:
	name2id = dict()
	def __init__(self):
		f = open(cfg.PLAYER_PATH)
		for line in f:
			data = line.split()
			self.name2id[data[1]] = data[0]
		f.close()
	
	def GetID(self, name):
		if name in self.name2id:
			return self.name2id[name]
		return None

	def GetID_GBK(self, name):
		pid = self.GetID(name)
		if pid == None:
			return 0
		return pid.decode('utf').encode('gbk')


if __name__ == "__main__":
	pls = Players()
	p_utf = pls.GetID(cfg.TEST_PLAYER2)
	p_gbk = pls.GetID_GBK(cfg.TEST_PLAYER2)
	print 'player name = ' + cfg.TEST_PLAYER2
	print 'player id = ' + p_utf
	print 'player id byte in utf = ' + util.GetByteStr(p_utf)
	print 'player id byte in gbk = ' + util.GetByteStr(p_gbk)



