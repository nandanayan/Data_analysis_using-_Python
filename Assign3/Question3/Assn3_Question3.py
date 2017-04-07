
# coding: utf-8

# In[ ]:




# In[6]:

import pandas as pd
import numpy as np


# In[7]:


r1=pd.read_csv(r"Assignment 3\Data\cricket_matches.csv")[['home','result','winner','innings1','innings1_runs','innings2','innings2_runs']]
r1['home_win']=np.where(r1['home']==r1['winner'],'YES','NO')#calling .csv file from relative path and assigning my column values


# In[8]:

r1=r1[r1['home_win']=='YES']
r1['winner_score']=np.where(r1['winner']==r1['innings1'],r1['innings1_runs'],r1['innings2_runs'])
team_average=r1[['home','winner_score']]#checking for the first or second innings for a winning team


# In[9]:

#group and average the scores of winning teams

team_average=team_average.groupby('home').mean().sort_values(by =['winner_score'],ascending = False)


# In[10]:

team_average.to_csv('cricket.csv', sep=',', encoding='utf-8')
team_average.head()


# In[ ]:



