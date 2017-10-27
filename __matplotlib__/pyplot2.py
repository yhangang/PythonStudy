# -*- coding: utf-8 -*-  

import numpy as np
import matplotlib.pyplot as plt

# t = np.linspace(-1, 2, 300)
t = np.arange(-1, 2, 0.01)
s = np.sin(2 * np.pi * t)


# draw a thick red hline at y=0 that spans the xrange
# plt.plot(t, s)
plt.axhline(linewidth=4, color='r')
plt.axis([-1, 2, -1, 2])
# plt.show()
# plt.close()


# draw a default hline at y=1 that spans the xrange
# plt.plot(t,s)
l = plt.axhline(y=1, color='b')
plt.axis([-1, 2, -1, 2])
# plt.show()
# plt.close()


# draw a thick blue vline at x=0 that spans the upper quadrant of the yrange
# plt.plot(t,s)
l = plt.axvline(x=0, ymin=0, linewidth=4, color='b')
plt.axis([-1, 2, -1, 2])
# plt.show()
# plt.close()


# draw a default hline at y=.5 that spans the the middle half of the axes
plt.plot(t,s)
l = plt.axhline(y=.5, xmin=0.25, xmax=0.75)
plt.axis([-1, 2, -1, 2])
plt.show()
plt.close()



