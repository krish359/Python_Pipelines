#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load dataset
file_path = "C:\\Users\\DELL\\Downloads\\transaction_data.csv"
transactions = pd.read_csv(file_path)


# In[2]:


transactions.head(10)


# In[3]:


# --- Cleaning ---
# Remove rows with missing or non-numeric amounts
transactions = transactions.dropna(subset=["amount"])
transactions["amount"] = pd.to_numeric(transactions["amount"], errors="coerce")


# In[4]:


transactions.head(10)


# In[5]:


# Drop rows where amount is still NaN after conversion
transactions = transactions.dropna(subset=["amount"])


# In[6]:


transactions.head(10)


# In[7]:


# --- Filtering ---
# Calculate mean transaction value
mean_value = transactions["amount"].mean()

# Filter transactions above $1000 or above mean value
high_value_txns = transactions[
    (transactions["amount"] > 1000) | (transactions["amount"] > mean_value)
]


# In[8]:


transactions.head(10)


# In[10]:


# Save cleaned & filtered transactions
output_file = "C:\\Users\\DELL\\Downloads\\transaction_data.csv"
high_value_txns.to_csv(output_file, index=False)

# Show preview
high_value_txns.head(10), mean_value


# In[ ]:




