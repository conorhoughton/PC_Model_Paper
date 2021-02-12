import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as l
import time
import csv
import itertools

#plt.rcParams.update({
#    "text.usetex": True,
#    "font.family": "sans-serif",
#    "font.sans-serif": ["Helvetica"]})

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


voltage_a_ms = np.loadtxt('voltage_tau_plus_2.txt')
voltage_b_ms = np.loadtxt('voltage_tau_plus_2_cf45.txt')


voltage_a = [x[1]*1000 for x in voltage_a_ms]
voltage_b = [x[1]*1000 for x in voltage_b_ms]

# sampling_rate=0.0025
sampling_rate=0.001
times = [x[0] for x in voltage_a_ms]

t1=0
while times[t1]<0.18225:
    t1+=1

t2=t1
while times[t2]<0.28725:
    t2+=1


x=0.065
y=-0.015


fig1 = plt.figure(facecolor='white')
fig1.set_figheight(3.2)
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

bottom=-65
top   = 25
ax1.set_ylim(bottom,top)

plt.plot(times[t1:t2], voltage_a[t1:t2], 'k')

offset=0.005

plt.xlabel('20 ms', fontsize=12)
ax1.xaxis.set_label_coords(0.9, -0.015)
plt.ylabel('20 mV', fontsize=12)
ax1.yaxis.set_label_coords(1.0, 0.375)
scale1_x=[times[t2]+offset-0.02,times[t2]+offset]
scale1_y=[-65,-65]
plt.plot(scale1_x,scale1_y,color='k')

scale2_x=[times[t2]+offset,times[t2]+offset]
scale2_y=[-65,-45]
plt.plot(scale2_x,scale2_y,color='k')

ax1 = fig1.add_subplot(212, frameon=False)
ax1.get_xaxis().tick_bottom()
ax1.get_yaxis().tick_left()
ax1.get_xaxis().set_tick_params(which='both', direction='out')
ax1.get_yaxis().set_tick_params(which='both', direction='out')

ax1.set_ylim(bottom,top)

plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,
    left=False,       # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False,         # ticks along the top edge are off
    labelleft=False)


plt.plot([x for x in times[t1:t2]], voltage_b[t1:t2], 'k')


offset=0.005

plt.xlabel('20 ms', fontsize=12)
ax1.xaxis.set_label_coords(0.9, -0.015)
plt.ylabel('20 mV', fontsize=12)
ax1.yaxis.set_label_coords(1.0, 0.375)
scale1_x=[times[t2]+offset-0.02,times[t2]+offset]
scale1_y=[-65,-65]
plt.plot(scale1_x,scale1_y,color='k')

scale2_x=[times[t2]+offset,times[t2]+offset]
scale2_y=[-65,-45]
plt.plot(scale2_x,scale2_y,color='k')


plt.text(0.17,190,'A', fontsize=16)
plt.text(0.17,30 ,'B', fontsize=16)

#plt.text(0.18,353.5,'$\\tau_-=5$ ms', fontsize=12)
#plt.text(0.18,193.5,'$\\tau_-=8$ ms', fontsize=12)
#plt.text(0.18,30 ,'$\\tau_- = 12$ ms and $I_{\\mathrm{cf}}=20\\,\\mu$A/cm$^2$', fontsize=12)

plt.text(0.18,190,'2 ms', fontsize=12)
plt.text(0.18,30 ,'2 ms and $I_{\\mathrm{cf}}=45\\,\\mu$A/cm$^2$', fontsize=12)

fig1.subplots_adjust(hspace=.7)

#plt.legend(loc=2,bbox_to_anchor=(0,0.92),fontsize=12)
#plt.ylim(0,2.2)
#plt.ylabel('Normalised Simple Spike Count Per Bin', fontsize=14, labelpad=2.5)
#plt.xlabel('Time From Complex Spike, ms', fontsize=14, labelpad=5.5)
#plt.text(-550,2.11,'B',fontsize=14)
#plt.tight_layout(pad=0.4, w_pad=3.0, h_pad=1.0)
plt.savefig('figure_tau_plus.jpg', dpi=900)
plt.show()

