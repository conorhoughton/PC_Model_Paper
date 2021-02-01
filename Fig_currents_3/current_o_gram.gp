
unset key
unset ytics
# set border 0

set multiplot layout 4,1


set xtics out
set xtics nomirror


set xrange [0.2177525:0.29]

plot "currents_short.txt" us (($1)):2 w lines lc rgb "black"


set tmargin 0
set bmargin 0
unset xtics

set yrange [0:0.0005]
plot "currents_short.txt" us 1:(($11)+($14)) w lines 


set yrange [-1:1]
plot "currents_short.txt" us 1:(($3)+($6)) with filledcurve y=0 lc rgb "yellow" title "$I_0$" , "currents_short.txt" us 1:3 with filledcurve y=0 lc rgb "red" title "$I_Na$" , "currents_short.txt" us 1:(-($8)-($9)) with filledcurve y=0 lc rgb "pink" title "$I_l" , "currents_short.txt" us 1:(-($8)) with filledcurve y=0 lc rgb "green" title "$I_K"

set yrange [-0.0005:0] 

plot "currents_short.txt" us 1:(($12)+($13)) w lines

unset multiplot