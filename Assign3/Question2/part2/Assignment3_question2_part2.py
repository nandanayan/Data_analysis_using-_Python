
# coding: utf-8

# In[9]:

from pandas import Series, DataFrame
import pandas as pd
import numpy as np


# In[10]:

data=pd.read_csv(r"Assignment 3\Data\employee_compensation.csv")#calling .csv file from relative path


# In[16]:

cal=DataFrame(data,columns=['Year Type','Employee Identifier','Salaries','Overtime','Other Salaries','Total Salary','Total Benefits','Total Compensation'])
cal=cal[cal['Year Type']=='Calendar']#alligning the column csv files in data frame
cal=cal.groupby(by=['Employee Identifier']).mean()#for grouping employees on subdivision


# In[17]:


cal['5p_salary']=cal['Salaries']*0.05#calculating the 5% salary
cal['overtimenet']=np.where(cal['Overtime']>cal['5p_salary'],'YES','NO')
cal=cal[cal['overtimenet']=='YES']#comparing the overtime values with 5% salarys


# In[21]:


employee_data = DataFrame(cal.index.get_level_values('Employee Identifier'))


# In[26]:

familydata = employee_data.merge(data, on = 'Employee Identifier')['Job Family'].unique()#for distinct job family sub division
final = data[data['Job Family'].isin(familydata)]#grouping for agregating total benfits and compensations
final = final.groupby('Job Family')['Total Benefits', 'Total Compensation'].mean()


# In[27]:

final['BenefitPercentage'] = final['Total Benefits'] * 100 / final['Total Compensation']
final=final.sort_values(by='BenefitPercentage', ascending=False).head(n=5)
final.to_csv('Benfits.csv', sep=',', encoding='utf-8')
final.head()


# In[ ]:



