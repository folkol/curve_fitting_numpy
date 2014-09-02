import numpy as np
from scipy.optimize import curve_fit
from scipy.stats.distributions import t

x = np.array([1, 10, 100, 1000, 2000])
cy = np.array([21, 217, 725, 1631, 1713])
my = np.array([32, 137, 161, 168, 172])

import matplotlib.pyplot as plt
plt.plot(x,cy,'bo')
plt.plot(x,cy,'b-', label='Couch')
plt.plot(x,my,'ro')
plt.plot(x,my,'r-', label='MySQL')
plt.legend(loc='best')
plt.xlabel('Number of threads', fontsize=18)
plt.ylabel('content per sec', fontsize=16)
plt.axis([-100, 2100, -100, cy.max() + 100])
plt.grid()
plt.show()
#savefig('images/nonlin-curve-fit-ci.png')
