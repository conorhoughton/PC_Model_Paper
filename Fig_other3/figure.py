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
y1=20

x3=0
y3=25


x2=0.85
y2=0.98

voltage_trace_10_mv = np.loadtxt('voltage_1.0.txt')
voltage_trace_05_mv = np.loadtxt('voltage_0.5.txt')
voltage_trace_01_mv = np.loadtxt('voltage_0.1.txt')

voltage_trace_10 = [x[1]*1000 for x in voltage_trace_10_mv]
voltage_trace_05 = [x[1]*1000 for x in voltage_trace_05_mv]
voltage_trace_01 = [x[1]*1000 for x in voltage_trace_01_mv] 

times = [x[0] for x in voltage_trace_05_mv]

t_length=0.5

t1_10=0
while times[t1_10]<0.13225:
    t1_10+=1
t2_10=t1_10+1
while times[t2_10]<times[t1_10]+t_length:
    t2_10+=1

t1_05=0
while times[t1_05]<0.129835:
    t1_05+=1
t2_05=t1_05+1
while times[t2_05]<times[t1_05]+t_length:
    t2_05+=1
    
t1_01=0
while times[t1_01]<0.13625:
    t1_01+=1
t2_01=t1_01+1
while times[t2_01]<times[t1_01]+t_length:
    t2_01+=1

    

t1=10
t2=min(len(voltage_trace_05),len(voltage_trace_10),len(voltage_trace_01))

fig1 = plt.figure(facecolor='white')

#1

ax1 = fig1.add_subplot(311, frameon=False)

plt.tick_params(
     axis='both',          # changes apply to the x-axis
     which='both',      # both major and minor ticks are affected
     right=False,
     bottom=False,
     left=False,       # ticks along the bottom edge are off
     top=False,         # ticks along the top edge are off
     labelbottom=False,         # ticks along the top edge are off
     labelleft=False)

plt.plot(times[t1_10:t2_10], voltage_trace_10[t1_10:t2_10], 'k')

plt.xlabel('100 ms', fontsize=12)
ax1.xaxis.set_label_coords(0.9, -0.015)
plt.ylabel('20 mV', fontsize=12)
ax1.yaxis.set_label_coords(1.0, 0.375)
scale1_x=[times[t2_10]-0.095,times[t2_10]+0.005]
scale1_y=[-65,-65]
plt.plot(scale1_x,scale1_y,color='k')

scale2_x=[times[t2_10]+0.005,times[t2_10]+0.005]
scale2_y=[-65,-45]
plt.plot(scale2_x,scale2_y,color='k')

plt.ylim(bottom=-70)
plt.ylim(top=+20)

ax1.text(x3,y3,'A', fontsize=16)


ax1.annotate('', xy = (0.10, -70),\
              xytext = (0.10, -55), fontsize = 12, \
              color = 'k', arrowprops=dict(edgecolor='black', facecolor='black', arrowstyle = '<|-', shrinkA = 0, shrinkB = 0))


#2

ax1 = fig1.add_subplot(312, frameon=False)

plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,
    left=False,       # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False,         # ticks along the top edge are off
    labelleft=False)


plt.ylim(bottom=-70)
plt.ylim(top=+20)

plt.plot([x for x in times[t1_05:t2_05]], voltage_trace_05[t1_05:t2_05], 'k')


plt.xlabel('100 ms', fontsize=12)
ax1.xaxis.set_label_coords(0.9, -0.015)
plt.ylabel('20 mV', fontsize=12)
ax1.yaxis.set_label_coords(1.0, 0.375)
scale1_x=[times[t2_05]-0.095,times[t2_05]+0.005]
scale1_y=[-65,-65]
plt.plot(scale1_x,scale1_y,color='k')

scale2_x=[times[t2_05]+0.005,times[t2_05]+0.005]
scale2_y=[-65,-45]
plt.plot(scale2_x,scale2_y,color='k')





ax1.text(x3,y3,'B', fontsize=16)

ax1.annotate('', xy = (0.1, -70),\
              xytext = (0.1, -55), fontsize = 12, \
              color = 'k', arrowprops=dict(edgecolor='black', facecolor='black', arrowstyle = '<|-', shrinkA = 0, shrinkB = 0))


#3


ax1 = fig1.add_subplot(313, frameon=False)

plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,
    left=False,       # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False,         # ticks along the top edge are off
    labelleft=False)


plt.ylim(bottom=-70)
plt.ylim(top=+20)


plt.plot(times[t1_01:t2_01], voltage_trace_01[t1_01:t2_01], 'k')



plt.xlabel('100 ms', fontsize=12)
ax1.xaxis.set_label_coords(0.9, -0.015)
plt.ylabel('20 mV', fontsize=12)
ax1.yaxis.set_label_coords(1.0, 0.375)
scale1_x=[times[t2_01]-0.095,times[t2_01]+0.005]
scale1_y=[-65,-65]
plt.plot(scale1_x,scale1_y,color='k')

scale2_x=[times[t2_01]+0.005,times[t2_01]+0.005]
scale2_y=[-65,-45]
plt.plot(scale2_x,scale2_y,color='k')

ax1.text(x3,y3,'C', fontsize=16)


ax1.annotate('', xy = (0.1, -70),\
              xytext = (0.1, -55), fontsize = 12, \
              color = 'k', arrowprops=dict(edgecolor='black', facecolor='black', arrowstyle = '<|-', shrinkA = 0, shrinkB = 0))


plt.text(0.05,345,'A', fontsize=16)
plt.text(0.05,185,'B', fontsize=16)
plt.text(0.05,25 ,'C', fontsize=16)
plt.text(0.1,335,'$g_{\mathrm{l}}=2\,$mS', fontsize=12)
plt.text(0.1,175,'$g_{\mathrm{l}}=1\,$mS', fontsize=12)
plt.text(0.1,15 ,'$g_{\mathrm{l}}=0.2\,$mS', fontsize=12)           


fig1.subplots_adjust(hspace=.7)

plt.savefig('Fig_gl_3.jpg', dpi=900)
plt.show()

