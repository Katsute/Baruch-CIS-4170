#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("diamonds.csv", index_col=0)
data


# In[ ]:


sns.pairplot(
    data, 
    kind="hist", 
    vars=["cut", "clarity"], 
    x_vars=["price"], y_vars=["color"]
)

