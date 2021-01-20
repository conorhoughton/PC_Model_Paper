#set size 0.6,0.4
set border 3
set ytics nomirror
set xtics nomirror
unset key
set xrange [0:9]
set ytics (-60,-40,-20,0,20)
set yrange [-70.001:20.001]
set xlabel "\$t\$ (ms)"
set ylabel "\$v\$ (mV)"

set arrow from 2.05,-46.636 to 3.45,-46.636 heads
set label "\$\\delta t\_1\$" at 3,-43

set arrow from 2.575,20.26 to 3.575,20.26 backhead
set label "max" at 4.025,17.0

set arrow from 3.925,-60.8 to 3.925,-30.8 backhead
set label "min" at 4.2,-27.5

set arrow from 3.925,-46.636 to 7,-46.636 heads
set label "\$\\delta t\_2\$" at 4.5,-43

plot "4p_voltage.txt" us (1000*($1)-91.05):(1000*($2)) w lines lc black lw 3
