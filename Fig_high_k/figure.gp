set size 0.6,0.7
set border 3
set ytics nomirror
set xtics nomirror
unset key
set xrange [0:25]
set ytics (-60,-40,-20,0,20)
set yrange [-65.001:20.001]
set xlabel "\$t\$ (ms)"
set ylabel "\$v\$ (mV)"

set arrow from (232.325-229.25),-51.42 to (246.3-229.25),-51.42 heads
set label "\$\\delta t\_1\$" at 5,-54.42

set arrow from (232.8-229.25),20.833 to (245.725-229.25),20.833 heads
set label "\$\\delta t\_2\$" at 8,17.833

plot "voltage_high_k_high_cf.txt" us (1000*($1)-229.25):(1000*($2)) w lines lc black lw 3
