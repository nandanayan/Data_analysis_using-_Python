
# coding: utf-8

# In[50]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[51]:

data=pd.read_csv(r"Assignment 3\Data\vehicle_collisions.csv")#calling .csv file from relative path and data frame columns assignment to the vehicle collissions csv file.
daF=DataFrame(data, columns=['BOROUGH', 'VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE'])


# In[52]:

daF['VEHICLE 1 TYPE'] = daF['VEHICLE 1 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)#iterating through VEHICLE 1 TYPE column to find the relative count of collisions involved


# In[53]:

daF['VEHICLE 2 TYPE'] = daF['VEHICLE 2 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)#iterating through VEHICLE 2 TYPE column to find the relative count of collisions involved


# In[54]:

daF['VEHICLE 3 TYPE'] = daF['VEHICLE 3 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)#iterating through VEHICLE 3 TYPE column to find the relative count of collisions involved


# In[55]:

daF['VEHICLE 4 TYPE'] = daF['VEHICLE 4 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)#iterating through VEHICLE 4 TYPE column to find the relative count of collisions involved


# In[56]:

daF['VEHICLE 5 TYPE'] = daF['VEHICLE 5 TYPE'].apply(lambda x: 0 if pd.isnull(x) else 1)#iterating through VEHICLE 5 TYPE column to find the relative count of collisions involved


# In[57]:

daF['COMBINE']=daF['VEHICLE 1 TYPE']+daF['VEHICLE 2 TYPE']+daF['VEHICLE 3 TYPE']+daF['VEHICLE 4 TYPE']+    daF['VEHICLE 5 TYPE']
daF['COMBINE']=daF['COMBINE'].apply(lambda x: 4 if x>3 else x)#many vehicles involved if?


# In[58]:

daF['1VEHICLE INVOLVED']= np.where(daF['COMBINE']== 1, 1,0)
daF['2VEHICLE INVOLVED']= np.where(daF['COMBINE']== 2, 1,0)
daF['3VEHICLE INVOLVED']= np.where(daF['COMBINE']== 3, 1,0)
daF['ManyVEHICLES INVOLVED']= np.where(daF['COMBINE']== 4, 1,0)
daF=daF.groupby('BOROUGH').sum() #agregating the net counts


# In[59]:

outputpdf=DataFrame(daF,columns=['1VEHICLE INVOLVED','2VEHICLE INVOLVED','3VEHICLE INVOLVED','ManyVEHICLES INVOLVED'])


outputpdf.to_csv(r'Assignment 3\Data\VehicleDetails_count.csv',index=False)
outputpdf.head()


# In[ ]:




# In[ ]:




# In[ ]:



