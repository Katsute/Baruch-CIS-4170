#!/usr/bin/env python
# coding: utf-8

# # patches

# In[ ]:


import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
plt.rc('figure', figsize=(10, 6))


# In[ ]:


fig = plt.figure(figsize=(6, 6))   #figsize: width, height in inches. 
                                   #If not provided, defaults to rcParams["figure.figsize"] = [6.4, 4.8]

ax = fig.add_subplot(1, 1, 1)

# Rectangle
# xy - the bottom left rectangle coordinates
# alpha - float (0.0 transparent through 1.0 opaque)
rect = plt.Rectangle(xy=(0.2, 0.75), width=0.4, height=0.15, 
                     color='k', alpha=.3)

# Circle
#xy - circle center
circ = plt.Circle(xy=(0.7, 0.2), radius=0.15, color='b', alpha=.3)


# Polygon
pgon = plt.Polygon(xy=[[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
                   color='g', alpha=.3)

ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)

