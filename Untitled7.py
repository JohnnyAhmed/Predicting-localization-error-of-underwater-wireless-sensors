#!/usr/bin/env python
# coding: utf-8

# In[106]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[107]:


dataset = pd.read_csv("mcs_ds_edited_iter_shuffled.csv")


# In[108]:


dataset.head()


# In[109]:


dataset.describe()


# In[110]:


X = dataset.drop('ale', axis=1)
y = dataset['ale']
import pandas as pd
del X["sd_ale"]


# In[111]:


X.head()


# In[112]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[113]:


from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)


# In[114]:


y_pred = regressor.predict(X_test)


# In[115]:


df=pd.DataFrame({'Actual':y_test, 'Predicted':y_pred})
df


# In[116]:


from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# In[ ]:




