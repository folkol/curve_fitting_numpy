import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from sys import stdin


title = stdin.readline()
x = np.array(range(1, 20, 2))
y = [float(elem) for elem in stdin.readline().split()]

interp_x = np.linspace(x.min(), x.max(), 25)
interp_y = interpolate.interp1d(x, y, kind='cubic')(interp_x)

plt.xlabel('Number of threads', fontsize=10)
plt.ylabel('Writes per sec', fontsize=10)
plt.axis([0, 20, min(interp_y) - 0.1*max(interp_y), 1.1*max(interp_y)])
plt.grid()
plt.title(title)
plt.plot(interp_x, interp_y, '-b', label='Writes per second')
plt.plot(x, y, 'or')
plt.legend(loc='upper left')
plt.savefig('plot.png')
plt.close()
