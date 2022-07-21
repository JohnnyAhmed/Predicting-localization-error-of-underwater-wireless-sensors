#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
dataset=pd.read_csv("mcs_ds_edited_iter_shuffled.csv")
dataset


# In[3]:


print(dataset.columns)


# In[4]:


dataset.describe()


# In[6]:


from matplotlib import pyplot as plt
plt.scatter(dataset["anchor_ratio"], dataset["ale"])
plt.xlabel("Anchor ratio")
plt.ylabel("Average localization error")
plt.show()
plt.scatter(dataset["trans_range"], dataset["ale"])
plt.xlabel("Transmission range")
plt.ylabel("Average localization error")
plt.show()
plt.scatter(dataset["node_density"], dataset["ale"])
plt.xlabel("Node density")
plt.ylabel("Average localization error")
plt.show()
plt.scatter(dataset["iterations"], dataset["ale"])
plt.xlabel("Iterations")
plt.ylabel("Average localization error")
plt.show()


# In[5]:


from collections import Counter
counter=Counter(dataset["node_density"])
print(counter)


# In[6]:


from collections import Counter
counter=Counter(dataset["iterations"])
print(counter)


# In[7]:


from collections import Counter
counter=Counter(dataset["anchor_ratio"])
print(counter)


# In[8]:


from collections import Counter
counter=Counter(dataset["trans_range"])
print(counter)


# In[9]:


l=0
q=0
w=0
for i in range(0, len(dataset)):
    if( dataset["node_density"][i]==100):
        l=l+dataset["ale"][i]
    if( dataset["node_density"][i]==200):
        q=q+dataset["ale"][i]
    if( dataset["node_density"][i]==300):
        w=w+dataset["ale"][i]
print(l/57)
print(q/36)
print(w/14)


# In[15]:


a1=[]
b1=[]
a2=[]
b2=[]
a3=[]
b3=[]
for i in range(0, len(dataset)):
    if(dataset["node_density"][i]==100):
        a1.append(dataset["anchor_ratio"][i])
        b1.append(dataset["ale"][i])
    if(dataset["node_density"][i]==200):
        a2.append(dataset["anchor_ratio"][i])
        b2.append(dataset["ale"][i])
    if(dataset["node_density"][i]==300):
        a3.append(dataset["anchor_ratio"][i])
        b3.append(dataset["ale"][i])
print(a1)
print(b1)
print(a2)
print(b2)
print(a3)
print(b3)


# In[16]:


import statistics
avg1=statistics.mean(b1)
print(avg1)
avg2=statistics.mean(b2)
print(avg2)
avg3=statistics.mean(b3)
print(avg3)


# In[17]:


from matplotlib import pyplot as plt
plt.scatter(a1, b1)
plt.show()
plt.scatter(a2, b2)
plt.show()
plt.scatter(a3, b3)
plt.show()


# In[20]:


g1=[]
h1=[]
g2=[]
h2=[]
g3=[]
h3=[]
for i in range(0, len(dataset)):
    if(dataset["node_density"][i]==100):
        g1.append(dataset["iterations"][i])
        h1.append(dataset["ale"][i])
    if(dataset["node_density"][i]==200):
        g2.append(dataset["iterations"][i])
        h2.append(dataset["ale"][i])
    if(dataset["node_density"][i]==300):
        g3.append(dataset["iterations"][i])
        h3.append(dataset["ale"][i])
print(g1)
print(h1)
print(g2)
print(h2)
print(g3)
print(h3)


# In[21]:


from matplotlib import pyplot as plt
plt.scatter(g1, h1)
plt.show()
plt.scatter(g2, h2)
plt.show()
plt.scatter(g3, h3)
plt.show()


# In[22]:


import seaborn as sns
#data=sns.load_dataset("mcs_ds_edited_iter_shuffled")
sns.relplot(x="node_density", y="ale", hue="iterations", data=dataset)


# In[23]:


dataset.columns


# In[24]:


for i,v in dataset.iteritems():
    print(i)
    print(v)


# In[25]:


print(dataset.iteritems())


# In[26]:


dataset.corr(method="pearson")


# In[27]:


dataset.cov()


# In[28]:


print(type(dataset))


# In[ ]:




