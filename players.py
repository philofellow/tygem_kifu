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
	
	def GetID(self, name):
		if name in self.name2id:
			return self.name2id[name]
		return None
	
	def GetIDByte(self, name):
		pid = self.GetID(name)
		if pid == None:
			return 0
		return pid.encode('gbk')



