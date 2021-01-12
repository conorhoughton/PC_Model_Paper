set key bottom right

set size 0.6,0.6

set xrange [58:82]
set yrange [0:120]

set xlabel "input current ($\mu$A/cm\$^2\$)"
set ylabel "firing rate (Hz)"

plot "fi_current.txt" us 1:2 w lines lw 2 title "Three"
replot "fi_4ch_current.txt" us 1:2 w lines lw 2 title "Five"