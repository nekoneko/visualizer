#!/usr/bin/gnuplot
set style data lines
set yrange[0:0.00003]
plot 'context_switch.txt' using 1:3, 'average.txt'
pause -1
