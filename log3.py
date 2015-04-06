#!/usr/bin/env python

# Copyright (C) 2013 National Cheng Kung University, Taiwan
# All rights reserved.

# Configure wether to trace these feature
# Warning : Too many contents may freeze Grasp

log = open('log', 'r')
fout_cs = open('context_switch.txt','wb')
fout_av = open('average.txt','wb')
lines = log.readlines()

width = 15
count = 1
interval = 0.0
average=0.0
string = "{:>{width}}{:>{width}}{:>{width}}\n".format('#id','6_digit','10_digit',width=width)
fout_cs.write(bytes(string,'UTF-8'))

for line in lines :
	line = line.strip()
	inst, args = line.split(' ', 1)
		
	if inst == 'switch' :
		out_task, in_task, tick, tick_reload, out_minitick, in_minitick = args.split(' ')
		
		out_time = (float(tick) + (float(tick_reload) - float(out_minitick)) / float(tick_reload)) / 100
		in_time  = (float(tick) + (float(tick_reload) - float(in_minitick))  / float(tick_reload)) / 100
		interval = in_time - out_time

		string = "{:>{width}}{:>{width}.6f}{:>{width}.10f}\n".format(count,interval,interval,width=width)
		fout_cs.write(bytes(string, 'UTF-8'))

		count+=1
		average+=interval;

average/=count;
fout_av.write(bytes("{:>{width}}{:>{width}}\n".format('#id','average',width=width),'UTF-8'))
for i in range(1,count) : 
	fout_av.write(bytes("{:>{width}}{:>{width}.10f}\n".format(i,average,width=width),'UTF-8'))

log.close()
fout_cs.close()
fout_av.close()
