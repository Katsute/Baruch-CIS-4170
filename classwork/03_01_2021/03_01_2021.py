#!/usr/bin/env python
# coding: utf-8

# # Pie Chart

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


# Bare minimum
values = [10, 20]
plt.pie(values)
plt.show()


# In[3]:


values=[5,8,9,10]
colors=['green', 'orange', 'yellow', 'gray']
labels=['a','b','c','d']
explode= [0, 0, 0, 0.5] # dist from center

plt.pie(values,
        colors=colors,
        labels=labels,
        explode=explode,
        autopct="%1.1f%%", # format
        counterclock=True,
        shadow=True
)

plt.title("Pie Chart")
plt.show()


# ## From DataFrame

# In[4]:


df = pd.DataFrame({"mass": [0.330, 4.87, 5.97],"radius": [2439.7,6051.8,6378.1]},index=["Mercury","Venus","Earth"])
print(df)
plot = df.plot.pie(y="mass", figsize=(5, 5))


# In[5]:


df['mass'].plot(kind='pie', figsize=(5,5))


# # Bar Chart
# 
# Recommended for categorical

# In[6]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[7]:


# Bare minimum
x = range(0, 5)
values = [5, 6, 5, 5, 4]

plt.bar(x, values)


# In[8]:


left = ['a', 'b', 'c', 'd', 'e']
values = [5,6,5,5,4]
widths = [0.7,0.7,0.7,0.7,0.9]
colors = ['g', 'g', 'g', 'g', 'r']

# edge is where the key is located (a is on the left instead of center)
# hatch is the design

plt.bar(left, values, width=widths,color=colors, align="edge", hatch="o")
plt.show()


# ## From DataFrame

# In[9]:


np.random.seed(12348)
arr = np.random.rand(6, 4) # rand grid

df = pd.DataFrame(arr, 
                  index=['uk','monaco','czech','france','austria','italy'],
                  columns=pd.Index([2018, 2019, 2020, 2021], name='Country'))
df


# In[10]:


df.plot.bar()


# In[11]:


df.plot.bar(stacked=True)


# In[12]:


df.plot.barh()  # horizontal


# In[13]:


df.plot.barh(stacked=True, alpha=0.5)


# In[14]:


df[2018].plot.bar()  # single col


# ### Bar

# In[15]:


# mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[16]:


src = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv")


# In[17]:


# cross tabulate
ct = pd.crosstab(index=src['day'], columns=src['size'])
ct


# In[18]:


ct.sum(axis=1)


# In[19]:


ct = ct.div(ct.sum(axis=1), axis=0) # divide size by sum of size to get 100% chart ?


# In[20]:


# display
df = pd.DataFrame(ct, 
                  index=pd.Index(['Thur','Fri','Sat','Sun'], name='day'), #cols
                  columns=pd.Index([1,2,3,4,5,6], name='size'))  # size

df.plot.bar(stacked=True)


# # SubPlots

# In[21]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.random import randn


# In[22]:


arr = np.array([1, 2, 3, 4])

fig = plt.figure()

# first two args is the grid and the last arg is the index.
# subplots are in a sense placed one on top of another
# (figure doesn't control subplots).
ax1 = fig.add_subplot(2, 2, 1) # cols, rows, subplot num
ax3 = fig.add_subplot(2, 2, 3)

plt.plot(randn(50).cumsum(), 'k--')  # plots onto the most recently added subplot


# In[23]:


ax1.hist(randn(100), bins=20, color='k', alpha=.3) # modify existing plots
ax2 = fig.add_subplot(2, 2, 2)
ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))
fig


# # SubPlots (2)

# In[24]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.random import randn


# In[25]:


fig, axes = plt.subplots(2, 3) # y * x


# In[26]:


axes[0, 0].hist(randn(500), bins=50, color='k', alpha=.5)
axes[0, 1].hist(randn(500), bins=50, color='k', alpha=.5)
axes[0, 2].hist(randn(500), bins=50, color='k', alpha=.5)
axes[1, 0].hist(randn(500), bins=50, color='k', alpha=.5)
axes[1, 1].hist(randn(500), bins=50, color='k', alpha=.5)
axes[1, 2].hist(randn(500), bins=50, color='k', alpha=.5)

plt.subplots_adjust(wspace=0, hspace=0)


# # Bar Plot (series)

# In[27]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from numpy.random import randn


# In[28]:


data = pd.Series(np.random.rand(16), index=list("abcdefghijklmnop"))

fig, axis = plt.subplots(2, 1)

data.plot.bar(ax=axis[0], alpha=.5)
data.plot.barh(ax=axis[1], color='k', alpha=0.5)


# In[ ]:




