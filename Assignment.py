#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


df=pd.read_csv("asset_1.csv")


# In[4]:


df.head()


# In[5]:


df['position'] = 0
build_threshold = 0.6
liquidate_threshold = 0.2
current_position = 0

for i in range(1, len(df)):
    if current_position == 0:
        if df.loc[i, 'alpha'] >= build_threshold:
            current_position = 1 
        elif df.loc[i, 'alpha'] <= -build_threshold:
            current_position = -1
    elif current_position == 1:
        if df.loc[i, 'alpha'] <= liquidate_threshold:
            current_position = 0
    elif current_position == -1:
        if df.loc[i, 'alpha'] >= -liquidate_threshold:
            current_position = 0 
    
    df.loc[i, 'position'] = current_position

df.loc[len(df)-1, 'position'] = 0

df.to_csv('asset_data_with_positions.csv', index=False)
df.head()


# In[6]:


df['trade'] = df['position'].diff().fillna(0)
df['price_change'] = df['price'].diff().fillna(0)
df['pnl'] = 0

for i in range(1, len(df)):
    if df.loc[i, 'trade'] != 0:
        df.loc[i, 'pnl'] = -df.loc[i, 'trade'] * df.loc[i, 'price']
    df.loc[i, 'pnl'] += df.loc[i, 'position'] * df.loc[i, 'price_change']

total_pnl = df['pnl'].sum()
print(f"Total PnL: {total_pnl}")

df.to_csv('asset_data_with_pnl.csv', index=False)
df.head()


# In[7]:


def calculate_pnl(build_threshold, liquidate_threshold, df):
    df['position'] = 0
    current_position = 0
    for i in range(1, len(df)):
        if current_position == 0:
            if df.loc[i, 'alpha'] >= build_threshold:
                current_position = 1
            elif df.loc[i, 'alpha'] <= -build_threshold:
                current_position = -1
        elif current_position == 1:
            if df.loc[i, 'alpha'] <= liquidate_threshold:
                current_position = 0
        elif current_position == -1:
            if df.loc[i, 'alpha'] >= -liquidate_threshold:
                current_position = 0
        df.loc[i, 'position'] = current_position
    df.loc[len(df)-1, 'position'] = 0
    df['trade'] = df['position'].diff().fillna(0)
    df['price_change'] = df['price'].diff().fillna(0)
    df['pnl'] = 0
    for i in range(1, len(df)):
        if df.loc[i, 'trade'] != 0:
            df.loc[i, 'pnl'] = -df.loc[i, 'trade'] * df.loc[i, 'price']
        df.loc[i, 'pnl'] += df.loc[i, 'position'] * df.loc[i, 'price_change']
    return df['pnl'].sum()
build_thresholds = np.arange(0.1, 1.0, 0.1)
liquidate_thresholds = np.arange(0.1, 1.0, 0.1)

best_pnl = float('-inf')
best_thresholds = (0, 0)
for build_threshold in build_thresholds:
    for liquidate_threshold in liquidate_thresholds:
        pnl = calculate_pnl(build_threshold, liquidate_threshold, df.copy())
        if pnl > best_pnl:
            best_pnl = pnl
            best_thresholds = (build_threshold, liquidate_threshold)

print(f"Optimal Build Threshold: {best_thresholds[0]}")
print(f"Optimal Liquidate Threshold: {best_thresholds[1]}")
print(f"Best PnL: {best_pnl}")


# In[ ]:




