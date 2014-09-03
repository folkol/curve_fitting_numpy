import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from sys import stdin, argv


if len(argv) > 1:
    print 'usage: python %s' % argv[0]
    print ''
    print ('       This script will read data from stdin and write a '
           'cubic spline plot to plot.png')
    print ''
    print '        The expected input format is:'
    print ''
    print '            1: [Title of the graph]'
    print '            2: [list of x values]'
    print '            *: [lists of y values]'
    print ''
    print ('       If you supply more than one line of y values, their '
           'average will be used.')
    exit()


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
plt.hlines(max(y), 0, 1.1*max(x), 'g', 'dashed', 'Max: %.2f' % max(y))
plt.title(title)
plt.plot(ix, iy, '-b', label='Writes per second')
plt.plot(x, y, 'or')
plt.legend(loc='lower right')
plt.savefig('plot.png')
plt.close()
