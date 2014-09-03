import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import sys


def plot_figure(counter, line):
    y = [float(elem) for elem in line.split()]
    x=np.array(range(1, 20, 2))

    title='Volatile contents: 100.000 x 0kb, Aspects: 0 x 0kb'
    
    new_length = 25
    new_x = np.linspace(x.min(), x.max(), new_length)
    new_y = interpolate.interp1d(x, y, kind='cubic')(new_x)
    
    plt.plot(new_x, new_y, label='Volatile writes')
    plt.plot(x, y, 'or')
    plt.legend(loc='best')
    plt.xlabel('Number of threads', fontsize=10)
    plt.ylabel('Writes per sec', fontsize=10)
    plt.axis([0, 20, min(y) - 0.1*max(y), 1.1*max(y)])
    plt.grid()
    plt.title(title)
    plt.savefig('plot_%d.png' % counter)
    plt.close()


for (counter, line) in enumerate(sys.stdin):
    plot_figure(counter, line)
