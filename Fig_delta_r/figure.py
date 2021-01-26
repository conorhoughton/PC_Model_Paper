import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as l
import time
import csv
import itertools

# x1=0.91
# y1=-25

# x2=0.9
# y2=1.03


x1=2.35
y1=10

x2=0.85
y2=0.98

x3=2.3
y3=25


voltage_135_ms = np.loadtxt('voltage_135.txt')
voltage_165_ms = np.loadtxt('voltage_165.txt')


voltage_135 = [x[1]*1000 for x in voltage_135_ms]
voltage_165 = [x[1]*1000 for x in voltage_165_ms]

# sampling_rate=0.0025
sampling_rate=0.001
times = [x[0] for x in voltage_135_ms]

t1=0
while times[t1]<0.1:
    t1+=1

t2=len(times)


x=0.065
y=-0.015


fig1 = plt.figure(facecolor='white')
ax1 = fig1.add_subplot(211, frameon=False)
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()
ax1.get_xaxis().set_tick_params(which='both', direction='out')
ax1.get_yaxis().set_tick_params(which='both', direction='out')

plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,
    left=False,       # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False,         # ticks along the top edge are off
    labelleft=False)

plt.plot(times[t1:t2], voltage_135[t1:t2], 'k')


offset=0.03

plt.xlabel('100 ms', fontsize=12)
ax1.xaxis.set_label_coords(0.9, -0.015)
plt.ylabel('20 mV', fontsize=12)
ax1.yaxis.set_label_coords(1.0, 0.375)
scale1_x=[times[-1]+offset-0.1,times[-1]+offset]
scale1_y=[-65,-65]
plt.plot(scale1_x,scale1_y,color='k')

scale2_x=[times[-1]+offset,times[-1]+offset]
scale2_y=[-65,-45]
plt.plot(scale2_x,scale2_y,color='k')

ax1 = fig1.add_subplot(212, frameon=False)
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()
ax1.get_xaxis().set_tick_params(which='both', direction='out')
ax1.get_yaxis().set_tick_params(which='both', direction='out')

plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,
    left=False,       # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False,         # ticks along the top edge are off
    labelleft=False)



# ax1.add_artist(l.Line2D((t2/1000, t2/1000+0.2), (-80, -80), color='black', linewidth=2))
# ax1.add_artist(l.Line2D((t2/1000+0.2, t2/1000+0.2), (-80, -60), color='black', linewidth=4))


plt.plot([x for x in times[t1:t2]], voltage_165[t1:t2], 'k')


offset=0.03

plt.xlabel('100 ms', fontsize=12)
ax1.xaxis.set_label_coords(0.9, -0.015)
plt.ylabel('20 mV', fontsize=12)
ax1.yaxis.set_label_coords(1.0, 0.375)
scale1_x=[times[-1]+offset-0.1,times[-1]+offset]
scale1_y=[-65,-65]
plt.plot(scale1_x,scale1_y,color='k')

scale2_x=[times[-1]+offset,times[-1]+offset]
scale2_y=[-65,-45]
plt.plot(scale2_x,scale2_y,color='k')


plt.text(0.0,195,'A', fontsize=16)
plt.text(0.0,32 ,'B', fontsize=16)

plt.text(0.05,185,'$\delta r=0.135\,\mu$m', fontsize=12)
plt.text(0.05,22 ,'$\delta r=0.165\,\mu$m', fontsize=12)


fig1.subplots_adjust(hspace=.7)

#plt.legend(loc=2,bbox_to_anchor=(0,0.92),fontsize=12)
#plt.ylim(0,2.2)
#plt.ylabel('Normalised Simple Spike Count Per Bin', fontsize=14, labelpad=2.5)
#plt.xlabel('Time From Complex Spike, ms', fontsize=14, labelpad=5.5)
#plt.text(-550,2.11,'B',fontsize=14)
#plt.tight_layout(pad=0.4, w_pad=3.0, h_pad=1.0)
plt.savefig('figure_gsk.jpg', dpi=900)
plt.show()

