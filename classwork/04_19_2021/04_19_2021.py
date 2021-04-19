#!/usr/bin/env python
# coding: utf-8

# |module|types|
# |---|---|
# |date|y/m/d|
# |time|h/min/s/ms/tz|
# |datetime|^ all above|
# |timedelta|duration to ms|
# |tzinfo|timezone & dst|

# datetime -> string
# ```python
# str(timestamp)
# ```
# string -> datetime
# ```python
# dateutil.parser.parse(str)
# ```

# In[ ]:


from datetime import datetime
from datetime import date
from datetime import timedelta

import numpy as np
import pandas as pd


# In[ ]:


now = datetime.now()
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, sep='\n')


# In[ ]:


dt = datetime(2020, 4, 15, 0, 1)
print(dt)


# In[ ]:


print(dt + timedelta(2)) # add 2 days


# In[ ]:


from dateutil.parser import parse

print(parse("Apr 15, 2020 10:00 PM"))
print(parse("Apr 15, 2020 10:00 PM", dayfirst = True))


# In[ ]:


datestr = ["2018-11-18", "2018-11-19"]
print(pd.to_datetime(datestr))


# In[ ]:


print(dt > now) # conditionals


# In[ ]:


dates = [datetime(2019, 4, 1), datetime(2019, 4, 2), datetime(2019, 4, 3)]
ts = pd.Series([1, 2, 3], index=dates)
print(ts)
print(ts.index)
print(ts.truncate(after="2019/04/02")) # print after
print(ts.index.is_unique) # unique dates


# In[ ]:


g = pd.Series([1, 2, 3], index=[datetime(2019, 4, 1), datetime(2019, 4, 1), datetime(2019, 4, 2)])
g.groupby(level=0)
print(g.describe())

