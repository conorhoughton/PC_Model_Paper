import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as l
import time
import csv
import itertools
import pylab as P
import scipy


voltage_10_mv  = np.loadtxt('voltage_10.txt')
voltage_20_mv  = np.loadtxt('voltage_20.txt')
voltage_30_mv  = np.loadtxt('voltage_30.txt')
voltage_45_mv  = np.loadtxt('voltage_45.txt')
voltage_60_mv  = np.loadtxt('voltage_60.txt')
voltage_90_mv  = np.loadtxt('voltage_90.txt')
voltage_130_mv = np.loadtxt('voltage_130.txt')
voltage_150_mv = np.loadtxt('voltage_150.txt')

times = [x[0] for x in voltage_10_mv]

voltage_10 = [x[1]*1000 for x in voltage_10_mv]
voltage_20 = [x[1]*1000 for x in voltage_20_mv]
voltage_30 = [x[1]*1000 for x in voltage_30_mv]
voltage_45 = [x[1]*1000 for x in voltage_45_mv]
voltage_60 = [x[1]*1000 for x in voltage_60_mv]
voltage_90 = [x[1]*1000 for x in voltage_90_mv]
voltage_130 = [x[1]*1000 for x in voltage_130_mv]
voltage_150 = [x[1]*1000 for x in voltage_150_mv]


t_length=0.022

#cs time is 0.23225

t1=0
while times[t1]<0.23:
    t1+=1
t2=t1+1
while times[t2]<times[t1]+t_length:
    t2+=1

    
fig1 = plt.figure(facecolor='white')
fig1.set_figheight(3.2)

    

#1
ax1 = fig1.add_subplot(231, frameon=False)

plt.tick_params(
     axis='both',          # changes apply to the x-axis
     which='both',      # both major and minor ticks are affected
     right=False,
     bottom=False,
     left=False,       # ticks along the bottom edge are off
     top=False,         # ticks along the top edge are off
     labelbottom=False,         # ticks along the top edge are off
     labelleft=False)

plt.plot(times[t1:t2], voltage_10[t1:t2], 'k')


#2
ax2 = fig1.add_subplot(232, frameon=False)

plt.tick_params(
     axis='both',          # changes apply to the x-axis
     which='both',      # both major and minor ticks are affected
     right=False,
     bottom=False,
     left=False,       # ticks along the bottom edge are off
     top=False,         # ticks along the top edge are off
     labelbottom=False,         # ticks along the top edge are off
     labelleft=False)

plt.plot(times[t1:t2], voltage_20[t1:t2], 'k')


#3
ax3 = fig1.add_subplot(233, frameon=False)

plt.tick_params(
     axis='both',          # changes apply to the x-axis
     which='both',      # both major and minor ticks are affected
     right=False,
     bottom=False,
     left=False,       # ticks along the bottom edge are off
     top=False,         # ticks along the top edge are off
     labelbottom=False,         # ticks along the top edge are off
     labelleft=False)

plt.plot(times[t1:t2], voltage_45[t1:t2], 'k')


#4
ax4 = fig1.add_subplot(234, frameon=False)

plt.tick_params(
     axis='both',          # changes apply to the x-axis
     which='both',      # both major and minor ticks are affected
     right=False,
     bottom=False,
     left=False,       # ticks along the bottom edge are off
     top=False,         # ticks along the top edge are off
     labelbottom=False,         # ticks along the top edge are off
     labelleft=False)

plt.plot(times[t1:t2], voltage_60[t1:t2], 'k')


#5
ax5 = fig1.add_subplot(235, frameon=False)

plt.tick_params(
     axis='both',          # changes apply to the x-axis
     which='both',      # both major and minor ticks are affected
     right=False,
     bottom=False,
     left=False,       # ticks along the bottom edge are off
     top=False,         # ticks along the top edge are off
     labelbottom=False,         # ticks along the top edge are off
     labelleft=False)

plt.plot(times[t1:t2], voltage_90[t1:t2], 'k')


#6
ax6 = fig1.add_subplot(236, frameon=False)

plt.tick_params(
     axis='both',          # changes apply to the x-axis
     which='both',      # both major and minor ticks are affected
     right=False,
     bottom=False,
     left=False,       # ticks along the bottom edge are off
     top=False,         # ticks along the top edge are off
     labelbottom=False,         # ticks along the top edge are off
     labelleft=False)

plt.plot(times[t1:t2], voltage_150[t1:t2], 'k')

plt.xlabel('5 ms', fontsize=12)
ax6.xaxis.set_label_coords(0.8, -0.015)
plt.ylabel('20 mV', fontsize=12)
ax6.yaxis.set_label_coords(1.1, 0.35)
scale1_x=[times[t2],times[t2]+0.005]
scale1_y=[-65,-65]
plt.plot(scale1_x,scale1_y,color='k')
scale2_x=[times[t2]+0.005,times[t2]+0.005]
scale2_y=[-65,-45]
plt.plot(scale2_x,scale2_y,color='k')



plt.text(0.0,0.9,'A', fontsize=16,transform=ax1.transAxes)
plt.text(0.0,0.9,'B', fontsize=16,transform=ax2.transAxes)
plt.text(0.0,0.9,'C', fontsize=16,transform=ax3.transAxes)
plt.text(0.,0.9,'D', fontsize=16,transform=ax4.transAxes)
plt.text(0.,0.9,'E', fontsize=16,transform=ax5.transAxes)
plt.text(0.,0.9,'F', fontsize=16,transform=ax6.transAxes)


plt.text(0.3,0.9,  '$10\,\mu$A$/$cm$^2$', fontsize=12,transform=ax1.transAxes)
plt.text(0.3,0.9, '$20\,\mu$A$/$cm$^2$', fontsize=12,transform=ax2.transAxes)
plt.text(0.3,.9,   '$45\,\mu$A$/$cm$^2$', fontsize=12,transform=ax3.transAxes)
plt.text(0.3,0.9 ,'$60\,\mu$A$/$cm$^2$', fontsize=12,transform=ax4.transAxes)           
plt.text(0.3,0.9,  '$90\,\mu$A$/$cm$^2$', fontsize=12,transform=ax5.transAxes)
plt.text(0.3,0.9 ,'$150\,\mu$A$/$cm$^2$', fontsize=12,transform=ax6.transAxes)           



fig1.subplots_adjust(hspace=.7)


plt.savefig('figure_cs_i.jpg', dpi=900)
plt.show()

