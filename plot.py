import numpy as np
from scipy.optimize import curve_fit
from scipy.stats.distributions import t

x=np.array([1, 10, 100, 1000, 2000])

cy=np.array([20, 188, 318, 1096, 816])
my=np.array([24, 45, 55, 91, 92])
title='Contents: 10.000 x 10.000kb, Aspects: 0 x 0kb'
filename='write2.png'

import matplotlib.pyplot as plt
plt.plot(x,cy,'bo')
plt.plot(x,cy,'b-', label='Couch')
plt.plot(x,my,'ro')
plt.plot(x,my,'r-', label='MySQL')
plt.legend(loc='best')
plt.xlabel('Number of threads', fontsize=10)
plt.ylabel('Writes per sec', fontsize=10)
plt.axis([-100, 2100, -100, cy.max() + 100])
plt.title(title)
plt.grid()
#plt.show()
plt.savefig('images/' + filename)
