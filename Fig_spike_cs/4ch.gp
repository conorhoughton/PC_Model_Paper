set size 0.6,0.6
set xrange [-15:20]
set yrange [-60.01:30]
set xlabel "$t$ (ms)"
set ylabel "$V$ (mV)"
set ytics (-60,-40,-20,0,20,40)
plot "voltage_4ch_0.txt" us (1000*($1)):(1000*($2)) w l title "0 ms"
replot "voltage_4ch_3.txt" us (1000*($1)):(1000*($2)) w l title "3 ms"
replot "voltage_4ch_6.txt" us (1000*($1)):(1000*($2)) w l title "6 ms"
replot "voltage_4ch_9.txt" us (1000*($1)):(1000*($2)) w l title "9 ms"