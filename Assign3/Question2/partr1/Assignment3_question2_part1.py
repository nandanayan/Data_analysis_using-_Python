
# coding: utf-8

# In[24]:

from pandas import Series, DataFrame
import pandas as pd


# In[25]:

align1=pd.read_csv(r"Assignment 3\Data\employee_compensation.csv",sep=",", skiprows=(1,1))


# In[26]:

align2=DataFrame(align1.groupby(["Organization Group", "Department"])['Total Compensation'].mean())


# In[28]:

align2=align2.sort_values('Total Compensation', ascending=False).sort_index(level=0, sort_remaining=False)
align2.to_csv('FinalCompensations.csv', sep=',', encoding='utf-8')
align2.head()



# In[ ]:



