set size 0.6,0.4
set border 3
set ytics nomirror
set xtics nomirror
unset key
set xrange [0:150]
set ytics (-60,-40,-20,0,20)
set yrange [-70.001:20.001]
set xlabel "\$t\$ (ms)"
set ylabel "\$v\$ (mV)"

set arrow from 47.3255,20 to 60.7505,20 heads
set label "\$\\delta t\_1\$" at 50,17

set arrow from 60.7505,20 to 89.6755,20 heads
set label "\$\\delta t\_2\$" at 75,17

plot "voltage_3.txt" us (1000*($1)-78.325):(1000*($2)) w lines lc black lw 2

