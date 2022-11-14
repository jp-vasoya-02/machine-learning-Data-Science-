#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[10]:


# arr=np.array([1,2,3])
arr=np.array([[1,2,3],[3,4,5],[5,6,7]])


# In[11]:


arr


# In[12]:


arr.shape


# In[14]:


arr.max()


# In[16]:


arr.dtype


# In[18]:


arr.min()


# In[24]:


arr.argmax()


# In[27]:


arr[2][2]


# In[29]:


arr.argmin()


# In[38]:


max=arr.reshape(1,9)[0][arr.argmax()]


# In[39]:


max


# In[93]:


rarr=np.random.randint(1,100,10).reshape(2,5)


# In[70]:


rarr.argsort()


# In[113]:


sortedarr=np.sort(rarr)


# In[108]:


rarr


# In[114]:


sortedarr


# In[117]:


sortedarr.max()


# In[120]:


arr.size


# In[122]:


def getMaxValue(arr):
    return arr.reshape(1,arr.size)[0][arr.argmax()]


# In[124]:


getMaxValue(sortedarr)


# In[126]:


randomArray=np.random.randint(1,1000,24).reshape(4,6)


# In[128]:


randomArray


# In[130]:


getMaxValue(randomArray)


# In[135]:


randomArray.sort()
randomArray


# In[230]:


# np.random.rand(5)
# np.random.rand(2,3)
# np.random.randn(10,3)
np.random.random(10)




# In[264]:


np.linspace(1,10,20,dtype="int")


# In[279]:


np.zeros([2,5])


# In[282]:


np.ones((4,4),dtype="int")


# In[306]:


np.eye(4)


# In[311]:


x=np.eye(4,k=2)


# In[330]:


x.flatten()


# In[331]:


x


# In[343]:


x.flat[2]


# In[345]:


x.astype("int")


# In[347]:


x.argsort()

