#!/usr/bin/env python
# coding: utf-8

# # Scatter Plot

# In[ ]:


import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5, 6]

plt.scatter(x, y, label='scatter', color='k')


# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as plb

a = np.random.rand(3)
print(a)
print(10 * a + 100)  # multiply/add all elements


# In[ ]:


x1 = 5 * np.random.rand(50);  # middle
x2 = 5 * np.random.rand(50) + 25;  # top (right)
x3 = 30 * np.random.rand(25);  # bottom (left)
x = np.concatenate((x1, x2, x3))  # merge

y1 = 5 * np.random.rand(50);  # middle
y2 = 5 * np.random.rand(50) + 25;  # (top) right
y3 = 30 * np.random.rand(25);  # (bottom) left
y = np.concatenate((y1, y2, y3))

plt.scatter(x, y, s=30, marker='*')
plt.show()


# In[ ]:


color_list = ['b'] * 50 + ['g'] * 50 + ['r'] * 25  # set color for each point
print(color_list)
'''
first 50 will be blue, next 50 green, final 25 red.
this is the order that we added them in with the concatenate method.
this doesn't actually check values, the color is fixed.
'''
plt.scatter(x, y, c=color_list)
plt.show()


# In[ ]:


plt.scatter(x, y, s=50, marker='D', c=color_list)

z = np.polyfit(x, y, 1) # add line width 1
p = np.poly1d(z) # ?
plt.plot(x, p(x), 'm-') # add correlation

plt.show()


# # Histogram

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

x = 200 * np.random.randn(1000)
plt.hist(x)
plt.show()


# In[ ]:


plt.hist(x,
        100, # bin number
        range=(-500, 500),
        histtype='stepfilled',
        align='mid',
        color='orange',
        label='test data')
plt.legend()
plt.show()

