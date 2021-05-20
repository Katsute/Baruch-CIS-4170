#!/usr/bin/env python
# coding: utf-8

# ## ����� ���� - CIS 4170 Data Visualization - matplotlib Dashboard
# 
# - [NYC Coronavirus Data](https://github.com/nychealth/coronavirus-data) - Coronavirus case data for New York City

# From day 1 New York City has provided their case counts publicly to promote transparency; using the provided data, we can determine case loads over time and by location. Initially case loads were low, averaging less than a 100 cases, mainly due to slow reporting and lack a resources dedicated to reporting cases. Cases reached an all time high, averaging 5 thousand daily cases, caused from uncontrolled spread from previous months and New York's aggressive campaign to test and trace new cases. As New York enacted lock down measures and travel bans, cases subsequently declines in the later months as everyone switched to remote workspaces and taking new measures to fight the virus. Around the holiday season cases began to spike to March levels in a second wave of new cases, mainly caused by holiday travel and ignorance of COVID guidelines. The effects of post-holiday travel and gatherings resulted in a higher average case count in the city, roughly 3 thousand daily cases, and only recently have started to decline partially due to the vaccine rollout. Over the year, majority of the cases have consistently come from the outer boroughs, Brooklyn, Queens, and the Bronx; citywide, cases have mainly come from those aged 18 and older. With these trends we can expect cases to decline first within the city then to the boroughs as the vaccine rollout continues.

# [scroll to bottom](#Figure)

# ### Import Data

# In[ ]:


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np

fig = plt.figure(figsize=(20, 25))
plt.subplots_adjust(wspace=.5, hspace=.5)

color = ['#FFB266','#99FFFF','#FF9999','#CCFF99','#CC99FF']  # softer colors

daily_cases = pd.read_csv("cases-by-day.csv")

by_boro = pd.read_csv("by-boro.csv")
by_boro = by_boro.sort_values("CASE_COUNT", ascending=False)

by_age = pd.read_csv("group-cases-by-boro.csv")

for col in ["group", "BK_CASE_RATE", "BX_CASE_RATE", "QN_CASE_RATE", "MN_CASE_RATE", "SI_CASE_RATE"]:
    by_age = by_age.drop(col, 1)
for row in [0,11,12,13,14,15,16]:
    by_age = by_age.drop(row, 0)
by_age = by_age.T

age_sum = {}
for k, v in by_age.items():
    age_sum[v[0].split('-')[0] if '-' in v[0] else v[0]] = v[1:].sum()


# ### Line Chart 

# In[ ]:


ax1 = fig.add_subplot(4, 1, 1)

ax1.plot(
    daily_cases["date_of_interest"], 
    daily_cases["CASE_COUNT"], 
    color=color[2],
    linewidth=4
)

ax1.xaxis.set_major_locator(mdates.MonthLocator())
[tick.set_rotation(45) for tick in ax1.get_xticklabels()]
ax1.title.set_text("Cases per Day")
ax1.set_xlabel("Day")
ax1.set_ylabel("Case Count")
ax1.set_facecolor("#222222")
ax1.grid()


# ### Pie Chart

# In[ ]:


ax2 = fig.add_subplot(4, 2, 5)

ax2.pie(
    by_boro["CASE_COUNT"][1:],
    colors=color,
    labels=by_boro["BOROUGH_GROUP"][1:],
    autopct="%1.1f%%"
)
ax2.title.set_text("Cases by Borough")


# ### Bar Chart

# In[ ]:


ax3 = fig.add_subplot(4, 2, 6)

ax3.bar(
    by_boro["BOROUGH_GROUP"][1:],
    by_boro["CASE_COUNT"][1:],
    color=color
)
[tick.set_rotation(45) for tick in ax3.get_xticklabels()]
ax3.title.set_text("Cases by Borough")
ax3.set_xlabel("Borough")
ax3.set_ylabel("Case Count")


# ### Histogram

# In[ ]:


ax4 = fig.add_subplot(4, 2, 7)

ax4.hist(
    age_sum.keys(),
    weights=age_sum.values(),
    color = color[2],
    bins=range(10) # fix x axis not lining up with bars
)
ax4.title.set_text("Case Distribution by Age")
ax4.set_xlabel("Age")
ax4.set_ylabel("Case Count")


# ### Scatterplot

# In[ ]:


ax5 = fig.add_subplot(4, 1, 2)
size = 15

ax5.scatter(
    daily_cases["date_of_interest"],
    daily_cases["QN_CASE_COUNT"],
    label="Queens",
    color=color[0],
    s=size
)
ax5.scatter(
    daily_cases["date_of_interest"],
    daily_cases["BK_CASE_COUNT"],
    label="Brooklyn",
    color=color[1],
    s=size
)
ax5.scatter(
    daily_cases["date_of_interest"],
    daily_cases["BX_CASE_COUNT"],
    label="Bronx",
    color=color[2],
    s=size
)
ax5.scatter(
    daily_cases["date_of_interest"],
    daily_cases["MN_CASE_COUNT"],
    label="Manhattan",
    color=color[3],
    s=size
)
ax5.scatter(
    daily_cases["date_of_interest"],
    daily_cases["SI_CASE_COUNT"],
    label="StatenIsland",
    color=color[4],
    s=size
)

ax5.xaxis.set_major_locator(mdates.MonthLocator())
[tick.set_rotation(45) for tick in ax5.get_xticklabels()]
ax5.title.set_text("Cases per Day by Borough")
ax5.legend(loc='upper left')
ax5.set_xlabel("Borough")
ax5.set_ylabel("Case Count")
ax5.set_facecolor("#222222")
ax5.grid()


# ## Figure

# In[ ]:


fig

