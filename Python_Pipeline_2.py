#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[2]:


# Load the data
file_path = "C:\\Users\\DELL\\Downloads\\us_customer_data.csv"
df = pd.read_csv(file_path)
print("Original Data Shape:", df.shape)


# In[3]:


df.head(10)


# In[5]:


# 1. Clean names (remove extra spaces, proper case)
df["name"] = df["name"].astype(str).str.strip().str.title()

# Split first and last names (handle missing last names)
df[["first_name", "last_name"]] = df["name"].str.split(n=1, expand=True)

# 2. Standardize emails (lowercase)
df["email"] = df["email"].astype(str).str.strip().str.lower()


# In[6]:


df.head(10)


# In[7]:


# If email missing or "nan", generate from first + last name
df["email"] = df.apply(
    lambda row: f"{row['first_name'].lower()}{(row['last_name'] or '').lower()}@example.com"
    if row["email"] in ["nan", "", None] or pd.isna(row["email"])
    else row["email"],
    axis=1,
)


# In[8]:


df.head(10)


# In[9]:


# 3. Standardize phone numbers to format: +1-XXX-XXX-XXXX
def clean_phone(phone):
    if pd.isna(phone) or str(phone).lower() == "nan":
        return None
    digits = re.sub(r"\D", "", str(phone))  # keep only digits
    if len(digits) >= 10:
        return f"+1-{digits[-10:-7]}-{digits[-7:-4]}-{digits[-4:]}"
    return None

df["phone"] = df["phone"].apply(clean_phone)


# In[10]:


df.head(10)


# In[11]:


# --- Mapping ---

# Extract country from address (assume US if address has state code)
df["country"] = df["address"].apply(lambda x: "US" if isinstance(x, str) and re.search(r"\b[A-Z]{2}\b", x) else None)

# Map to country code
country_mapping = {"United States": "US", "USA": "US", "US": "US"}
df["country_code"] = df["country"].map(country_mapping).fillna("US")


# In[12]:


df.head(10)


# In[13]:


# Final cleaned dataframe
cleaned_file = "C:\\Users\\DELL\\Downloads\\cleaned_customer_data.csv"
df.to_csv(cleaned_file, index=False)

# Show preview
df.head(10)


# In[ ]:




