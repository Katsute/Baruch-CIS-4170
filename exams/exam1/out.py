#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = pd.read_csv("out.csv")

x.plot.bar(x='day',stacked=True)

