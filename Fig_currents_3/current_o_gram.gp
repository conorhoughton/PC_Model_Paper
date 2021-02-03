
unset key
unset ytics
unset xtics
# set border 0
set size 0.6,0.6

set multiplot

set xrange [0.0:0.075]


set tmargin 0
set bmargin 0

set size 1,0.2
set origin 0,0.8
set border 0

plot "currents_short.txt" us (($1)):3 w lines lc rgb "black" lw 3


set border 15




set size 1,0.10
set origin 0,0.70


set yrange [0:0.0005]


plot "currents_short.txt" us 1:(($12)+($15)) w lines 


set size 1,0.50
set origin 0,0.20



set yrange [-1:1]
plot "currents_short.txt" us 1:(($4)+($7)) with filledcurve y=0 lc rgb "yellow" title "$I_0$" , "currents_short.txt" us 1:4 with filledcurve y=0 lc rgb "red" title "$I_Na$" , "currents_short.txt" us 1:(-($9)-($10)) with filledcurve y=0 lc rgb "pink" title "$I_l" , "currents_short.txt" us 1:(-($9)) with filledcurve y=0 lc rgb "green" title "$I_K"

set yrange [-0.0005:0] 


set size 1,0.10
set origin 0,0.1

set xtics out
set xtics nomirror

plot "currents_short.txt" us 1:(($13)+($14)) w lines

unset multiplot