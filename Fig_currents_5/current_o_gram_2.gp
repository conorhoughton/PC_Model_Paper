

# time v na+ ca+ k+ sk+ l+ i0+  na- ca- k-  sk- l-  i0- na   ca  k   sk  l  i0
# 1    2 3   4   5  6   7  8    9  10   11  12  13  14  15   16  17  18  19 20
# then add one to everything - the new 1 is the adjusted time, ie starts at 0


unset key
unset ytics
unset xtics
# set border 0
set size 0.7,0.6


set multiplot

set xrange [0.0:0.075]
set yrange [-0.080:0.025]
set tmargin 0
set bmargin 0


unset yrange
set size 1.0,0.20
set origin 0,0.80
set border 0
set ylabel "105 mV"

plot "currents_short.txt" us 1:3 w lines lc rgb "black" lw 3

set border 15




set size 1.0,0.10
set origin 0,0.70

set ylabel "0.6 nA"
set yrange [0:6]
plot "currents_short.txt" us 1:(10000*(($16)+($17)+($21))) w lines 
unset ytics

set size 1.0,0.25
set origin 0,0.45

set ylabel "inwards"
set yrange [0:1]
plot "currents_short.txt" us 1:(($4)+($5)+($9)) with filledcurve y=0 lc rgb "blue" title "$I_0$" , "currents_short.txt" us 1:(($4)+($9)) with filledcurve y=0 lc rgb "yellow" title "$I_Na$" ,  "currents_short.txt" us 1:4 with filledcurve y=0 lc rgb "red" title "$I_Ca$" ,


set ylabel "outwards"
set size 1.0,0.25
set origin 0,0.20
set yrange [-1:0]
plot "currents_short.txt" us 1:(-($12)-($13)-($14)) with filledcurve y=0 lc rgb "orange" title "$I_l" , "currents_short.txt" us 1:(-($12)-($13)) with filledcurve y=0 lc rgb "pink" title "$I_K", "currents_short.txt" us 1:(-($12)) with filledcurve y=0 lc rgb "green" title "$I_SK"

unset ylabel
set yrange [-0.0006:0] 


set size 1.0,0.10
set origin 0,0.1

set xrange [0:75]
set xtics out
set xtics nomirror
set ylabel "0.6 nA"
set xlabel "ms"
plot "currents_short.txt" us (1000*($1)):(($18)+($19)+($20)) w lines

unset multiplot