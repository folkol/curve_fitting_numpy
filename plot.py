import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from sys import stdin


title = stdin.readline()
x = [float(elem) for elem in stdin.readline().split()]

lines = [map(float, row.split()) for row in stdin]
y = np.average(lines, axis=0)

interp_x = np.linspace(min(x), max(x), 25)
interp_y = interpolate.interp1d(x, y, kind='cubic')(interp_x)

plt.xlabel('Number of threads', fontsize=10)
plt.ylabel('Writes per sec', fontsize=10)
plt.axis([0, 2000, min(interp_y) - 0.1*max(interp_y), 1.1*max(interp_y)])
plt.grid()
plt.title(title)
plt.plot(interp_x, interp_y, '-b', label='Writes per second')
plt.plot(x, y, 'or')
plt.legend(loc='upper left')
plt.savefig('plot.png')
plt.close()
