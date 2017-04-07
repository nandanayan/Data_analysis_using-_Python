
# coding: utf-8

# In[43]:

import pandas as pd #importing pandas
import numpy as np #importing numpy
from pandas import DataFrame as df #importing dataframe


# In[44]:

collisions=pd.read_csv(r"Assignment 3\Data\vehicle_collisions.csv",sep=",") #calling a file from a relative path


# In[45]:


collisions['DATE']=pd.to_datetime(vehicle_collisions['DATE'])  # type conversion and range setting for date time intervals
month_year_range=collisions[collisions['DATE'].isin(pd.date_range("01/01/16","12/31/16"))] 


# In[46]:


month_year_range['YEAR']=month_year_range['DATE'].dt.strftime('%Y/%b/%d').str.slice(0,4)
month_year_range['MONTH']=month_year_range['DATE'].dt.strftime('%Y/%b/%d').str.slice(5,8) 


# In[47]:

manhattan_data=month_year_range[month_year_range.BOROUGH=='MANHATTAN']
manhattan_count=manhattan_data['BOROUGH'].value_counts().reset_index(drop=True)


# In[48]:


manhattan_df=pd.DataFrame(manhattan_data.groupby(['MONTH'],sort=False).size().reset_index())#group by function for finding the count month wise


# In[49]:

manhattan_df.columns=['MONTH','MANHATTAN_ACCIDENT_COUNT']#assigning column names to frame
manhattan_df


# In[50]:

count_nyc=month_year_range['BOROUGH'].value_counts().reset_index(drop=True)
nyc_accident_count=pd.DataFrame(month_year_range.groupby(['MONTH'],sort=False).size().reset_index())#group by function for finding the count month wise


# In[51]:


nyc_accident_count.columns=['MONTH','NYC_ACCIDENT_COUNT'] #assigning column names to frame
nyc_accident_count


# In[52]:

main_frame=pd.merge(manhattan_df,nyc_accident_count)
#frame
main_frame['PERCENTAGE']=(main_frame['MANHATTAN_ACCIDENT_COUNT']/main_frame['NYC_ACCIDENT_COUNT'])*100#calculating the percentage from above output result set
main_frame


# In[54]:

main_frame.to_csv(r'Assignment 3\Data\accidentToatal_count.csv',index=False)#passing the output value to the .csv file


# In[ ]:



