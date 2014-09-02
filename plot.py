import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x=np.array(range(1, 20, 2))
y = [
2640.2604712004218,
6401.311398258293,
8679.857098304676,
10114.110428082759,
10673.308595450224,
11629.644662022174,
11843.275565782882,
11879.86933569315,
12537.850202530162,
11615.470319685619]

title='Volatile contents: 100.000 x 0kb, Aspects: 0 x 0kb'

new_length = 25
new_x = np.linspace(x.min(), x.max(), new_length)
new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)

plt.plot(new_x, new_y, label='Volatile writes')
plt.plot(x, y, 'o')
plt.legend(loc='best')
plt.xlabel('Number of threads', fontsize=10)
plt.ylabel('Writes per sec', fontsize=10)
plt.axis([0, 20, 0, max(y) + 1000])
plt.grid()
plt.title(title)
plt.show()


