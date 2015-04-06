#!/usr/bin/env python

# Copyright (C) 2013 National Cheng Kung University, Taiwan
# All rights reserved.

# Configure wether to trace these feature
# Warning : Too many contents may freeze Grasp

log = open('log', 'r')
fileout = open('context_switch.txt','wb')
lines = log.readlines()

width = 13
count = 1
interval = 0.0
string = "{:>{width}}{:>{width}}{:>{width}}\n".format('#id','10_digit','6_digit',width=width)
fileout.write(bytes(string,'UTF-8'))

for line in lines :
	line = line.strip()
	inst, args = line.split(' ', 1)
		
	if inst == 'switch' :
		out_task, in_task, tick, tick_reload, out_minitick, in_minitick = args.split(' ')
		
		out_time = (float(tick) + (float(tick_reload) - float(out_minitick)) / float(tick_reload)) / 100
		in_time  = (float(tick) + (float(tick_reload) - float(in_minitick))  / float(tick_reload)) / 100
		interval = in_time - out_time
		string = "{:{width}}{:{width}.6f}{:{width}.10f}\n".format(count,interval,interval,width=width)
		fileout.write(bytes(string, 'UTF-8'))
		count+=1

log.close()
fileout.close()
