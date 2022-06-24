#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ans 1)
The empty list value, which is a list value that contains no items. This is similar to how '' is the empty string value.


# In[17]:


# ans 2)
spam=[2, 4, 6, 8, 10]
spam[2] = 'hello' 
#(Notice that the third value in a list is at index 2 because the first index is 0.)


# In[3]:


# ans 3)
spam=['a','b','c','d']
spam[int(int(3*2)/11)]


# In[4]:


#ans 4)
spam[-1]


# In[5]:


#ans 5)
spam[:2]


# In[6]:


#ans 6)
bacon=[3.14,'cat',11,'cat',True]
bacon.index('cat')


# In[7]:


# ans 7)
bacon.append(99)
bacon
# it add 99 in last


# In[8]:


# ans 8)
bacon.remove('cat')
bacon
# it removes first appered cat in list


# In[ ]:


# ans 9)
list concatetion operator is +
list replication operator is *


# In[ ]:


# ans 10)
list insert method insert the value at specified index
list append method add value at the last index of list


# In[ ]:


# ans 11)
we can use pop(),remove() to remove items from list


# In[ ]:


# ans 12)
#The similarity between Lists and Strings in Python is that both are sequences. The differences between them are that firstly, Lists are mutable but Strings are immutable. Secondly, elements of a list can be of different types whereas a String only contains characters that are all of String type.


# In[ ]:


# ans 13)
# the tuples are immutable objects and the lists are mutable


# In[10]:


# and 14)
tup=(42)
tup


# In[13]:


# and 15)
The tuple() and list() functions, respectively


# In[ ]:


# ans 16)
They contain references to list values.


# In[ ]:


# ans 17)
The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.

