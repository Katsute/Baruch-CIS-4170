#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns

tips = pd.read_csv("tips.csv")


# In[ ]:


tips['tip_pct'] = tips['tips'] / (tips['total_bill'] - tips['tips'])
tips.head()


# In[ ]:


sns.barplot(x='tip_pct', y='day', data=tips, orient='h', order=['Thur', 'Fri', 'Sat', 'Sun'])


# In[ ]:


sns.barplot(x='tip_pct', y='day', hue='tips', data=tips, orient='h', order=['Thur', 'Fri', 'Sat', 'Sun'])


# In[ ]:


tips['tip_pct'].plot.density()


# distplot

# In[ ]:





# catplot

# In[ ]:


sns.catplot(x='day', y='tip_pct', hue='time', col='smoker', kind='bar', data=tips[tips.tips_pct < 1])


# boxplot

# In[ ]:


sns.boxplot(x=tips.tip_pct[tips.tips_pct < 1])

