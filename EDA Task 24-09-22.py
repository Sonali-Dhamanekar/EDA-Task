#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install dataprep


# In[2]:


import pandas as pd


# In[3]:


from dataprep.eda import create_report


# In[4]:


df = pd.read_csv("C:\\Users\\sonal\\Downloads\\Dataset\\Dataset\\data0\\aug_test.csv")


# In[5]:


create_report(df)


# PANDA'S PROFILING

# In[11]:


#pip install pandas-profiling


# In[35]:


#!pip install -U pandas-profiling[notebook]


# In[29]:


import pandas as pd
df = pd.read_csv("C:\\Users\\sonal\\Downloads\\Dataset\\Dataset\\data0\\aug_test.csv")


# In[32]:


pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip


# In[33]:


from pandas_profiling import ProfileReport


# In[34]:


report = ProfileReport(df)
report


# SWWETVIZ

# In[19]:


#pip install sweetviz


# In[20]:


import sweetviz as sv                       


# In[21]:


df = pd.read_csv("C:\\Users\\sonal\\Downloads\\Dataset\\Dataset\\data0\\aug_test.csv")


# In[22]:


analyze_report = sv.analyze(df)
analyze_report.show_html('report.html', open_browser=True)


# AUTOVIZ

# In[23]:


pip install autoviz


# In[24]:


from autoviz.AutoViz_Class import AutoViz_Class


# In[37]:


AV = AutoViz_Class()
df_av = AV.AutoViz("C:\\Users\\sonal\\Downloads\\Dataset\\Dataset\\data0\\aug_test.csv")


# In[ ]:




