import numpy as np
import matplotlib.pylab as plt
import matplotlib.lines as l
import time
import csv
import itertools
import pylab as P
import scipy
#from scipy.stats import pearsonr
#from scipy.stats import linregress
#from scipy.stats import nanmean # nanmedian exists too, if you need it
#from scipy.stats import nanstd # nanmedian exists too, if you need it
#from data_analysis_functions import *

x3=0.91
y3=-25

x2=0.9
y2=1.03


x1=0.01
y1=10

x3=0
y3=25


x2=0.85
y2=0.98

voltage_trace_1_0_mv = np.loadtxt('voltage_1.0.txt')
voltage_trace_0_5_mv = np.loadtxt('voltage_0.5.txt')
voltage_trace__25_mv = np.loadtxt('voltage_0.25.txt')
voltage_trace_0_1_mv = np.loadtxt('voltage_0.1.txt')

voltage_trace_1_0 = [x[1]*1000 for x in voltage_trace_1_0_mv]
voltage_trace_0_5 = [x[1]*1000 for x in voltage_trace_0_5_mv] 
voltage_trace__25 = [x[1]*1000 for x in voltage_trace__25_mv]
voltage_trace_0_1 = [x[1]*1000 for x in voltage_trace_0_1_mv] 

times = [x[0] for x in voltage_trace_1_0_mv]

t1=80
t2=len(times)

fig1 = plt.figure(facecolor='white')

# 1

ax1 = fig1.add_subplot(411, frameon=False)

plt.tick_params(
     axis='both',          # changes apply to the x-axis
     which='both',      # both major and minor ticks are affected
     right=False,
     bottom=False,
     left=False,       # ticks along the bottom edge are off
     top=False,         # ticks along the top edge are off
     labelbottom=True,         # ticks along the top edge are off
     labelleft=False)

plt.plot(times[t1:t2], voltage_trace_1_0[t1:t2], 'g')
plt.xlabel('20 ms', fontsize=14)
ax1.xaxis.set_label_coords(x2, -0.015)
plt.ylabel('20 mV', fontsize=14)
ax1.yaxis.set_label_coords(y2, 0.1)

ax1.text(x1, y1, r'$\bar{g}_l=2$mS/cm$^2$', color='k')
ax1.text(x3,y3,'A', fontsize=16)

x_cs=(0.06-times[t1])/(times[-1]-times[t1])

ax1.annotate('', xy = (x_cs, -0.2),  xycoords = 'axes fraction', \
              xytext = (x_cs, -0.0), textcoords = 'axes fraction', fontsize = 12, \
              color = 'k', arrowprops=dict(edgecolor='black', facecolor='black', arrowstyle = '<|-', shrinkA = 0, shrinkB = 0))

#2

ax1 = fig1.add_subplot(412, frameon=False)
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


#ax1.add_artist(l.Line2D((t2/1000, t2/1000+0.2), (-80, -80), color='black', linewidth=2))
#ax1.add_artist(l.Line2D((t2/1000+0.2, t2/1000+0.2), (-80, -60), color='black', linewidth=4))

plt.plot([x for x in times[t1:t2]], voltage_trace_0_5[t1:t2], 'k')
plt.xlabel('20 ms', fontsize=14)
ax1.xaxis.set_label_coords(x2, -0.015)
plt.ylabel('20 mV', fontsize=14)
ax1.yaxis.set_label_coords(y2, 0.1)

ax1.text(x1, y1, r'$\bar{g}_l=1$mS/cm$^2$', color='k')
ax1.text(x3,y3,'B', fontsize=16)

#ax1.add_artist(l.Line2D((3.32, 3.52), (-61, -61), color='black', linewidth=2))
#ax1.add_artist(l.Line2D((3.52, 3.52), (-61, -41), color='black', linewidth=1))

# ax1.add_artist(l.Line2D((t1/1000, t1/1000+0.2), (-80, -80), color='black', linewidth=2))
# ax1.add_artist(l.Line2D((t1/1000, t1/1000), (-80, -60), color='black', linewidth=2))

#3


ax1 = fig1.add_subplot(413, frameon=False)
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

# ax1.add_artist(l.Line2D((t1/1000, t1/1000+0.2), (-80, -80), color='black', linewidth=2))
# ax1.add_artist(l.Line2D((t1/1000, t1/1000), (-80, -60), color='black', linewidth=2))

plt.plot(times[t1:t2], voltage_trace__25[t1:t2], 'k')
plt.xlabel('20 ms', fontsize=14)
#ax1.xaxis.set_label_coords(x, -0.015)
# plt.ylabel('20 mV', fontsize=14)
# ax1.yaxis.set_label_coords(y, 0.1)

ax1.text(x1, y1, r'$\bar{g}_l=0.5$mS/cm$^2$', color='k')
ax1.text(x3,y3,'C', fontsize=16)

ax1.add_artist(l.Line2D((3.32, 3.52), (-61, -61), color='black', linewidth=2))
ax1.add_artist(l.Line2D((3.52, 3.52), (-61, -41), color='black', linewidth=1))



#4

ax1 = fig1.add_subplot(414, frameon=False)
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


#ax1.add_artist(l.Line2D((3.32, 3.52), (-61, -61), color='black', linewidth=2))
#ax1.add_artist(l.Line2D((3.52, 3.52), (-61, -41), color='black', linewidth=1))

plt.plot(times[t1:t2], voltage_trace_0_1[t1:t2], 'k')
plt.xlabel('20 ms', fontsize=14)
ax1.xaxis.set_label_coords(x2, -0.015)
plt.ylabel('20 mV', fontsize=14)
ax1.yaxis.set_label_coords(y2, 0.1)

ax1.text(x1, y1, r'$\bar{g}_l=0.2$mS/cm$^2$', color='k')
ax1.text(x3,y3,'D', fontsize=16)


ax1.annotate('', xy = (0.3, -0.2),  xycoords = 'axes fraction', \
             xytext = (0.3, -0.0), textcoords = 'axes fraction', fontsize = 12, \
             color = 'k', arrowprops=dict(edgecolor='black', facecolor='black', arrowstyle = '<|-', shrinkA = 0, shrinkB = 0)) 



fig1.subplots_adjust(hspace=.7)

#plt.savefig('figure_4_tau_decay_three_channel_model.jpg', dpi=900)
plt.show()

