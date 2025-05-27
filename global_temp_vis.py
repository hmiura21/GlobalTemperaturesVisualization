#!/usr/bin/env python3

#import packages
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
import csv

file = sys.argv[1]  

#assign empty lists
x=[]
y=[]
year=[]

#open csv file
with open(file) as csvfile:
    #separate columns by comma
    data= csv.reader(csvfile, delimiter=',')
    #skip first 5 lines outside of data
    for i in range(5):
        next(data)
    #add x and y data while separating date into year and month
    for line in data:
        if len(line)>1:
            x.append(int(line[0]))
            time=str(line[0])
            year.append(time[0:4])
            y.append(float(line[1]))

#plot
plt.plot(x,y)
plt.xlabel('Year')
plt.ylabel('Difference from Avg Temp (degrees C)')
plt.title('Global Average Temperature Anomaly')

plt.ylim(-1.0, 1.5) 
plt.axhspan(0, 1.5, color='red', alpha=0.3)
plt.xticks(ticks=x, labels=year)
plt.xticks(x[::120]) 

plt.show()

