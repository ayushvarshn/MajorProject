#!/usr/bin/env python
# coding: utf-8

# In[263]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[264]:


df=pd.read_csv('2017-05-12_6C-40per_3_6C_CH34.csv')
df2=pd.read_csv('2017-05-12_6C-50per_3_6C_CH36.csv')


# In[265]:


df.columns


# In[266]:


plt.plot(df[['Charge_Capacity']])
plt.xlabel('Time')
plt.ylabel( 'Charge Capacity (Ah)')


# In[267]:


plt.plot(df[['Charge_Capacity']])
plt.xlabel('Time')
plt.ylabel( 'Charge Capacity (Ah)')
plt.xlim(4000,20000)


# In[293]:



maxcap=[]
meanV=[]
meanI=[]
cap_last=[]
cycle=[]
for i in range(1,700):
    a=np.array(df[df['Cycle_Index']==float(i)]['Charge_Capacity'])
    b=np.array(df[df['Cycle_Index']==float(i)]['Voltage'])
    c=np.absolute(np.array(df[df['Cycle_Index']==float(i)]['Current']))
    cycle.append(i)
    maxcap.append(max(a))
    meanV.append(np.mean(b))
    meanI.append(np.mean(c))
for i in range(1,700):
    a=np.array(df2[df2['Cycle_Index']==float(i)]['Charge_Capacity'])
    b=np.array(df2[df2['Cycle_Index']==float(i)]['Voltage'])
    c=np.absolute(np.array(df2[df2['Cycle_Index']==float(i)]['Current']))
    cycle.append(i)
    maxcap.append(max(a))
    meanV.append(np.mean(b))
    meanI.append(np.mean(c))


# In[ ]:





# In[294]:


#plt.plot(maxcap)
plt.scatter(cycle[:699],meanV[:699],s=3,)
#plt.plot(meanV,'r')
plt.xlabel('Number of Cycles')
plt.ylabel('Mean Voltage')


# In[295]:


#plt.plot(maxcap)
plt.scatter(cycle[:699],meanI[:699],s=3,)
#plt.plot(meanI,'r')
plt.xlabel('Number of Cycles')
plt.ylabel('Mean Current')


# # Predict max_cap using Cycle Index and MeanVoltage

# In[280]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.neural_network import MLPRegressor


# In[281]:


cycle=np.array(cycle)
meanV=np.array(meanV)
meanI=np.array(meanI)
x=np.array([cycle,meanV,meanI])
x=pd.DataFrame(x).transpose()


# In[282]:


model=RandomForestRegressor()


# In[283]:


model.fit(x[:699],maxcap[:699])
p=model.predict(x)


# In[313]:


maxcap_train_reg=(maxcap[:699]/max(maxcap[:699]))*100
p_train_reg=(p[:699]/max(p[:699]))*100
plt.plot(maxcap_train_reg)
plt.plot(p_train_reg)
plt.title('Training set')
plt.xlabel('Number of Cycles')
plt.ylabel('Maximum Capacity (Ah)')
plt.legend(['True Value','Prediction'])
plt.show()
plt.title('Test set')
maxcap_test_reg=(maxcap[700:]/max(maxcap[700:]))*100
p_test_reg=(p[700:]/max(p[700:]))*100
plt.plot(maxcap_test_reg)
plt.plot(p_test_reg)
plt.xlabel('Number of Cycles')
plt.ylabel('Maximum Capacity (Ah)')
plt.legend(['True Value','Prediction'])
plt.show()


# In[314]:


plt.plot(p[:699]-maxcap[:699])
plt.ylabel('Error in prediction')
plt.xlabel('Number of Cycle')
plt.show()
plt.plot(p[700:]-maxcap[700:])
plt.ylabel('Error in prediction')
plt.xlabel('Number of Cycle')
plt.show()


# In[316]:


np.sqrt(mse(maxcap_test_reg,p_test_reg))/0.07


# In[ ]:





# In[301]:


import joblib
joblib.dump(model,'max_cap_model')


# In[ ]:




