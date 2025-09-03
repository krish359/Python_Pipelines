#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import re


# In[10]:


# Load the data
file_path = "C:\\Users\\DELL\\Downloads\\us_customer_data.csv"
df = pd.read_csv(file_path)

print("Original Data Shape:", df.shape)


# In[11]:


df.head(10)


# In[12]:


# Step 1: Remove duplicates based on 'customer_id'
if 'customer_id' in df.columns:
    df = df.drop_duplicates(subset=['customer_id'], keep='first')
else:
    print("⚠️ 'customer_id' column not found. Skipping deduplication.")

print("After Deduplication Shape:", df.shape)


# In[13]:


df.head(10)


# In[15]:


# Strip whitespace only from string columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()


# In[16]:


df.head(10)


# In[17]:


# Step 3: Standardize phone numbers (keep only digits, format as (XXX) XXX-XXXX if 10 digits)
def clean_phone(phone):
    if pd.isnull(phone):
        return np.nan
    digits = re.sub(r"\D", "", str(phone))
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return digits  # return raw if not standard length

if 'phone' in df.columns:
    df['phone'] = df['phone'].apply(clean_phone)


# In[18]:


df.head(10)


# In[19]:


# Step 4: Standardize email (lowercase)
if 'email' in df.columns:
    df['email'] = df['email'].str.lower()


# In[20]:


df.head(10)


# In[21]:


# Step 5: Standardize date formats (e.g., 'YYYY-MM-DD')
date_cols = [col for col in df.columns if 'date' in col.lower()]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce').dt.strftime('%Y-%m-%d')


# In[22]:


df.head(10)


# In[23]:


# Step 6: Handle missing values
# Example: fill missing phone with 'Unknown', drop rows with no email
if 'phone' in df.columns:
    df['phone'] = df['phone'].fillna("Unknown")
if 'email' in df.columns:
    df = df.dropna(subset=['email'])  # drop if email is missing

print("Final Cleaned Data Shape:", df.shape)


# In[31]:


# Save cleaned file
output_file = "C:\\Users\\DELL\\Downloads\\cleaned_customer_data.csv"
df.to_csv(output_file, index=False)
print(f"✅ Cleaned data saved to {output_file}")


# In[32]:


df.head(10)


# In[ ]:




