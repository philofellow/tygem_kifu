#!/usr/bin/python

import socket
import sys

def GetByteStr(data):
	return ':'.join([a.encode('hex') for a in data])

