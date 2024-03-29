#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Use the "ggplot" style and create new Figure/Axes
plt.style.use("ggplot")
fig, ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()


# In[ ]:


# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()


# In[ ]:


# Show the figure
plt.show()


# In[ ]:


# Save as a PNG file
fig.savefig("my_figure.png")


# In[ ]:


# Save as a PNG file with 300 dpi
# Save as a PNG file
fig.savefig("my_figure_300dpi.png", dpi=300)


# In[ ]:


# Set figure dimensions and save as a PNG
fig.set_size_inches([3, 5])
fig.savefig("figure_3_5.png")


# In[ ]:


# Set figure dimensions and save as a PNG
# Set figure dimensions and save as a PNG
fig.set_size_inches([5, 3])
fig.savefig("figure_5_3.png")


# In[ ]:


# Extract the "Sport" column
sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)


# In[ ]:


fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports:
  # Extract the rows only for this sport
  sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
  # Add a bar for the "Weight" mean with std y error bar
  ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file
fig.savefig("sports_weights.png")

