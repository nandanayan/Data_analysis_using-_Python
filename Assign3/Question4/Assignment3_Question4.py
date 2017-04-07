
# coding: utf-8

# In[109]:

import pandas as pd
from pandas import DataFrame
import numpy as np
import calendar


# In[110]:

init=pd.read_csv(r'Assignment 3\Data\movies_awards.csv')

#calling .csv file with relative paths


# In[111]:

init['Awards_Won'] = init['Awards'].str.extract('(\d+) win', expand=True)
init['Awards_Nominated'] = init['Awards'].str.extract('(\d+) nomination', expand=True)
init['PrimeAwards_Won']= init['Awards'].str.extract('Won (\d+) Primetime', expand=True)
#caluculating the award counts seperately for nominations and wins for each of column specified iterated value


# In[112]:

init['OscarAwards_Won']= init['Awards'].str.extract('Won (\d+) Oscar', expand=True)
init['OscarAwards_Nominations']= init['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True)
init['GoldenGlobeAwards_Won']= init['Awards'].str.extract('Won (\d+) Golden Globe', expand=True)
#caluculating the award counts seperately for nominations and wins for each of column specified iterated value


# In[113]:


init['GoldenGlobeAwards_Nominations']= init['Awards'].str.extract('Nominated for (\d+) Golden Globe', expand=True)
init['PrimeAwards_Nominations']= init['Awards'].str.extract('Nominated for (\d+) Primetime', expand=True)
init['BaftaAwards_Won']= init['Awards'].str.extract('Won (\d+) BAFTA', expand=True)
init['BaftaAwards_Nominations']= init['Awards'].str.extract('Nominated for (\d+) BAFTA', expand=True)

#caluculating the award counts seperately for nominations and wins for each of column specified iterated value


# In[114]:

para = init[init.columns[15:30]] #truncating the remaining output columns
output = para.fillna(0)


# In[115]:

output


# In[116]:

output['Awards_Won'] = output['Awards_Won'].astype(str).astype(int)
output['PrimeAwards_Won'] = output['PrimeAwards_Won'].astype(str).astype(int)
output['BaftaAwards_Won']=output['BaftaAwards_Won'].astype(str).astype(int) 
output['OscarAwards_Won']=output['OscarAwards_Won'].astype(str).astype(int) 
output['GoldenGlobeAwards_Won']=output['GoldenGlobeAwards_Won'].astype(str).astype(int)
#type conversion object---->pandas to integer


# In[118]:

output['Awards_Nominated'] =output['Awards_Nominated'].astype(str).astype(int) 
output['PrimeAwards_Nominations']=output['PrimeAwards_Nominations'].astype(str).astype(int)
#type conversion object---->pandas to integer
output['OscarAwards_Nominations']=output['OscarAwards_Nominations'].astype(str).astype(int)


# In[124]:

output['BaftaAwards_Nominations']=output['BaftaAwards_Nominations'].astype(str).astype(int)
#type conversion object---->pandas to integer


# In[127]:

output['GoldenGlobeAwards_Nominations']=output['GoldenGlobeAwards_Nominations'].astype(str).astype(int)
#type conversion object---->pandas to integer


# In[128]:

output['Awards Won Or Nominated'] = output['Awards_Won']+output['Awards_Nominated']


# In[129]:

output.head()


# In[130]:

output.to_csv('MovieAwaNom.csv')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



