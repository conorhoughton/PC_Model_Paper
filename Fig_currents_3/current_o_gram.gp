
unset key
unset ytics
unset xtics
# set border 0
set size 0.7,0.6

set multiplot

set xrange [0.0:0.075]
set yrange [-0.08:0.025]

set tmargin 0
set bmargin 0

set size 1,0.2
set origin 0,0.8
set border 0
set ylabel "105 mV"
plot "currents_short.txt" us (($1)):3 w lines lc rgb "black" lw 3


set border 15




set size 1,0.10
set origin 0,0.70


set ylabel "0.6 nA"
set yrange [0:6]

plot "currents_short.txt" us 1:(10000*(($12)+($15))) w lines 


set size 1,0.25
set origin 0,0.45


set ylabel "inwards"
set yrange [0:1]
plot "currents_short.txt" us 1:(($4)+($7)) with filledcurve y=0 lc rgb "yellow" title "$I_0$" , "currents_short.txt" us 1:4 with filledcurve y=0 lc rgb "red" title "$I_Na$"


set size 1,0.25
set origin 0,0.20


set ylabel "outwards"
set yrange [-1:0]
plot"currents_short.txt" us 1:(-($9)-($10)) with filledcurve y=0 lc rgb "pink" title "$I_l" , "currents_short.txt" us 1:(-($9)) with filledcurve y=0 lc rgb "green" title "$I_K"


set ylabel "0.6 nA"
set yrange [-6:0]

set size 1,0.10
set origin 0,0.1

set xrange [0:75]
set xtics out
set xtics nomirror
set ylabel "0.6 nA"
set xlabel "ms"

plot "currents_short.txt" us (1000*($1)):(10000*(($13)+($14))) w lines

unset multiplot