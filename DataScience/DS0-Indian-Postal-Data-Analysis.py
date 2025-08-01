"""
ALL INDIA PINCODE DIRECTORY

"""
# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
postal = pd.read_csv("./data/AIPD 2025.csv")
# first view of data
postal.head(5)

#%%
data = postal
# get some basic info of data
print(data.info)
# list of all column of data
print(data.columns)
print(data.columns.astype)
# check the missing values in each column
print(data.isna().sum())
# %%
data['latitude'] = pd.to_numeric(data['latitude'], errors='coerce')
data['longitude'] = pd.to_numeric(data['longitude'], errors='coerce')

# %% Filling missing region, district and statename with Unknown
data[['regionname', 'district', 'statename']] = data[['regionname', 'district', 'statename']].fillna('Unknown') 

#%% removing duplicate rows 
data = data.drop_duplicates()

#%% converting text columns to lowercase for consitency but they are already
data = data.apply(lambda x: x.lower() if isinstance(x, str) else x)

# %% exploration
print("\nSummary Statistics:\n", data.describe(include='all'))
print("\nMissing Values:\n", data.isnull().sum())

#%%
# 3. Visualizations
sns.set_style("whitegrid")

# Plot distribution of pincode
plt.figure(figsize=(10, 5))
sns.histplot(data['pincode'], bins=50, kde=True, color='blue')
plt.title("Distribution of Pincode")
plt.xlabel("Pincode")
plt.ylabel("Count")
plt.show()


# %%
# Countplot of officetype
plt.figure(figsize=(10, 5))
sns.countplot(y=data['officetype'], order=data['officetype'].value_counts().index, palette="viridis")
plt.title("Office Type Distribution")
plt.xlabel("Count")
plt.ylabel("Office Type")
plt.show()

#%%
# Scatter plot of latitude and longitude
plt.figure(figsize=(8, 6))
sns.scatterplot(x=data['longitude'], y=data['latitude'], alpha=0.5)
plt.title("Geographical Distribution of Offices")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
# %%
# 4. Correlation Analysis
plt.figure(figsize=(8, 6))
sns.heatmap(data[['pincode', 'latitude', 'longitude']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

print("Data Cleaning and Analysis Complete!")
# %%

"""
All india pincode distribution dataset
contains postal information like circles, regions, divisions, office names, 
pincode, office types, delivery status, district, state, and geolocation (latitude & longitude). 

1. Descriptive Analysis based question
✔ How many unique post offices exist? (by name, pincode, district, state)
✔ Which office type (BO, SO, HO) is most common?
✔ Which states have the highest number of post offices?
✔ How many offices provide delivery services versus non-delivery services? 

"""
#%%
df = data
import numpy as np
# 1. How many unique post offices exist? (by name, pincode, district, state)
print(len(df['officename'].unique()), 
      len(df['pincode'].unique()), 
      len(df['district'].unique()), 
    len(df['statename'].unique()))


# List of Indian States
indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

# List of Indian Union Territories (UTs)
indian_union_territories = [
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Lakshadweep", "Delhi", "Puducherry", "Ladakh", "Jammu and Kashmir"
]
#%%
print(df['statename'].unique())

#%%
# Extract unique state names and corresponding districts
unique_states = df['statename'].unique()
for state in unique_states:
    districts = df.loc[df['statename'] == state, 'district'].unique()
    print(f"State: {state}")
    print(len(districts.tolist()))
    print("--------------------")

#%%
print(len(districts['UTTER PRADESH']))


"""
2. Geographic Insights
✔ Which states or districts have the most postal offices?
✔ What is the geographic distribution of post offices across latitude & longitude?
✔ Which pincode areas have overlapping or missing latitude/longitude data?
✔ Are there regions with an unusually high density of post offices?

"""

"""
3. Trend Analysis & Clustering
✔ Are post offices evenly distributed across different states/districts?
✔ Which regions have the most missing postal information?
✔ Are there clusters of post offices in specific areas? (using K-Means clustering)
✔ Can we group post offices based on office type and delivery status?


"""


"""
4. Machine Learning Insights
✔ Predict missing latitude/longitude values using other location data
✔ Classify office types based on features like region, pincode, and delivery status
✔ Find anomalies in postal data (e.g., duplicate pincodes, incorrect states, missing entries)
"""

"""
5. Visualization-Based Questions
✔ What is the distribution of post offices per state? (Bar chart)
✔ How is the distribution of delivery vs. non-delivery offices across different regions? (Pie chart)
✔ How do postal office locations look on a map? (Scatter plot of lat-long)
✔ Which regions have missing values in postal data? (Heatmap)
"""
# %%
