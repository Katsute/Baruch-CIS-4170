#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns


# In[ ]:


sns.regplot(x="total_bill", y="tips", data=tips)


# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


sns.pairplot(data, diag_kind="kde", plot_kws={"alpha": 0.5, "s": 7})


# In[ ]:


sns.pairplot(stocks, hue="Company", vars=["Open", "Volume", "Close"])


# In[ ]:


sns.pairplot(stocks, 
             hue="Company", 
             aspect=1.5, 
             diag_kind="kde", 
             diag_kws={"share": True},
             plot_kvw={"s": 15, "marker": "+"},
             vars=["Open", "Volume", "Close"]
            )


# In[ ]:


sns.pairplot(stocks,
             hue="Company",
             aspect=1.5,
             x_vars=["Open", "Volume"],
             y_vars=["Close", "Close_change"]
            )

