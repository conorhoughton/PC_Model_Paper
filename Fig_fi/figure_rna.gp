unset key

set size 0.6,0.6

set xrange [80:150]
set yrange [0:120]

set xlabel "\bar{g}_{\leak} ($\msi$)"
set ylabel "firing rate (Hz)"

plot "fr_v_grna_mS.txt" us 1:2 w lines lw 2 lc black
