#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


vector = np.zeros(10)


# In[5]:


v = np.arange(10, 49)


# In[6]:


v.shape


# In[7]:


v.dtype


# In[10]:


print(np.__version__)
print(np.show_config())


# In[11]:


v.ndim


# In[12]:


v = np.ones(5)


# In[13]:


v


# In[17]:


bool_arr = np.array([True, True, True], dtype=bool)
print(bool_arr)


# In[8]:


a = np.random.randn(5)
a


# In[9]:


a = np.random.randn(5, 5)
a


# In[14]:


x = np.array([2, 3, 4, 5, 6])
y = np.flip(x)
y


# In[16]:


x = np.zeros(10)
x[4] = 1
x


# In[17]:


a = np.identity(3)
a


# In[18]:


arr = np.array([1, 2, 3, 4, 5])
arr = arr.astype(dtype = float)
arr


# In[20]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
arr1 * arr2


# In[22]:


arr3 = arr1 == arr2
arr3


# In[24]:


a = np.array([1,2,3,4,5,6,6,7,7,8,9])
a[a % 2 == 1]


# In[52]:


a[a % 2 == 1] = -1
a


# In[56]:


arr = np.arange(10)
arr[4 : 9] =12
arr


# In[13]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0][0]=64
arr3d


# In[ ]:




