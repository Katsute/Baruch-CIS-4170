#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


s = pd.Series(['a', 'd', 'a', 'a', 'b', 'b'])
s.value_counts()


# In[ ]:


s = pd.Series([1, 2, None])
s.fillna(-1)


# In[ ]:


s.dropna()


# In[ ]:


arr = np.array([5, 0, 2])
indexer = arr.argsort() # organize the values, ordred by the index they appear in


# In[ ]:


arr[indexer] # sort using indexer

