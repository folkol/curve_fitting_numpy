import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from sys import stdin


title = stdin.readline()
x = [float(elem) for elem in stdin.readline().split()]

lines = [map(float, row.split()) for row in stdin if row.strip()]
y = np.average(lines, axis=0)

ix = np.linspace(min(x), max(x), 25)
iy = interpolate.interp1d(x, y, kind='cubic')(ix)

plt.xlabel('Number of threads', fontsize=10)
plt.ylabel('Writes per sec', fontsize=10)
plt.axis([0, 1.1*max(x), min(iy) - 0.1*max(iy), 1.1*max(iy)])
plt.grid()
plt.hlines(max(y), 0, 1.1*max(x), colors='g', linestyle='dashed')
plt.title(title)
plt.plot(ix, iy, '-b', label='Writes per second')
plt.plot(x, y, 'or')
plt.legend(loc='upper left')
plt.savefig('plot.png')
plt.close()
