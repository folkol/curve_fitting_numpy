import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from sys import stdin, argv


def printUsage():
    print 'usage: python %s' % argv[0]
    print ''
    print ('       This script will read data from stdin and write a '
           'cubic spline plot to plot.png')
    print ''
    print '        The expected input format is:'
    print '            [Title of the graph]'
    print '            [a list of x values]'
    print '            (one or more) [a list of y values]'
    print ''
    print ('       If you supply more than one line of y values, the '
           'average will be used.')


def main():
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


if __name__ == "__main__":
    if len(argv) > 1:
        printUsage()
    else:
        main()
