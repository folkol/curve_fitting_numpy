import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from sys import stdin


title = stdin.readline()
x = np.array(range(1, 20, 2))
y = [float(elem) for elem in stdin.readline().split()]

new_x = np.linspace(x.min(), x.max(), 25)
new_y = interpolate.interp1d(x, y, kind='cubic')(new_x)

plt.plot(new_x, new_y, '-b', label='Writes per second')
plt.plot(x, y, 'or')
plt.legend(loc='upper left')
plt.xlabel('Number of threads', fontsize=10)
plt.ylabel('Writes per sec', fontsize=10)
plt.axis([0, 20, min(new_y) - 0.1*max(new_y), 1.1*max(new_y)])
plt.grid()
plt.title(title)
plt.savefig('plot.png')
plt.close()
