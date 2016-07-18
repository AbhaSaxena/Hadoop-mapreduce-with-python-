#!/usr/bin/env python
import sys

rt=0
abc_found=False
prev_key="xxx"

for line in sys.stdin:
	line       = line.strip()       #strip out carriage return
	key_value  = line.split('\t')   #split line, into key and value, returns a list
	key=key_value[0]
	if key!=prev_key and prev_key!="xxx":
		if abc_found==True:
			print('{0}\t{1}'.format(prev_key,rt))
			abc_found=False
			rt=int(key_value[1])
		
		elif key_value[1]=="ABC":
			abc_found=True
			rt=0
		
		else:
			rt=int(key_value[1])
			abc_found=False
		prev_key=key
	else:
		if key_value[1]!="ABC":		
			rt=int(key_value[1]) + rt
			prev_key=key
		else:
			abc_found=True
			prev_key=key
		
