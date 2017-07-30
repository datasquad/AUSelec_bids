# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
#x = mu + sigma * np.random.randn(10000)

# the histogram of the data

plt.axis([amin(x),amax(x), amin(x),amax(x)])
plt.plot(x,x, 'r-')
plt.show()
