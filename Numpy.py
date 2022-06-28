#!/usr/bin/env python
# coding: utf-8

# # Introduction: 
# ##### Numpy is simple yet powerful library. It is used for scientific and numerical computing.
# ##### The term 'Numpy' is made of two words i.e, 'Numerical' and 'Python'. 
# # Why:
# ##### 1) Uses much less memory
# ##### 2)To perform wide variety of mathematical operations on array.
# ##### 3) Compact data storage.
# ##### 4) High speed processing of arrays.
# ##### 5) Data compatibility with lots of other libraries
# 

# # Array:
# ##### An array is a collection of homogeneous data. It has grid of elements and that elements can be can be indexed in various ways.
# 
# # Python vs Array
# #####  Python List is a collection of heterogeneous data elements.      ||                           An array is collection of homogeneous data.
# #####  Consumes larger memory to perferm a simple task as well.         ||                 Uses least memory which is why performs in high speed.
# 
# 

# ### Loading library:

# In[5]:


import sys
import numpy as np


# # Term: ndarray:
# 
# ##### ndarray is a shorthand for 'N-dimensional array'. There is 1D array, 2D array and so on.

# # 1-D array/ One-dimensional array/ Vector:
# ##### 1D/ Vector is a array with a single dimension. There are no rows and columns.

# ### Creating 1D array:

# ##### Can convert given list into 1d array:

# In[6]:


a = [1,2,3,4,5,6,7,8,9]

b = np.array(a)
b


# ### Creating 1-D array with 'arange' function in various way:

# # **Arange():
# ##### arange () gives a numerical range. This function works same as Range() in Python, its just that Range() is Python default function and Arange() comes under Numpy library.

# ### 1st way:

# In[7]:


a = np.arange(10)
a


# ### 2nd way:
# ##### passing start & end points:

# In[9]:


a = np.arange(10,20)
a


# ### 3rd way:
# ##### giving start, end & step size:

# In[10]:


a = np.arange(10,20,2)
a


# # 2-d array/ Two dimensional array/ Matrix:
# 
# ##### refers to an array with two dimesions and made up of rows and columns.

# In[15]:


a = np.array([[1,2,3,4],[5,6,7,8]])
a


# # **Reshape():
# ##### reshape() allows us to change the shape of an array. Reshaping allows us to add or remove dimensions in an array.

# In[18]:


a = np.arange(20)
b = np.arange(20).reshape(4,5)
b


# # 3-D array/ Three dimensional array/ Tensor:
# 
# ##### 3-D array is also known as tensor.

# ### Creating 3D array:

# In[19]:


a = np.array([[[1,2,3],[4,5,6]]])
a


# ### Creating 3D array with reshape():

# In[22]:


a = np.arange(20).reshape(5,2,2)
a


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




