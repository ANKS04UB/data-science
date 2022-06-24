#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Write a Python program to convert kilometers to miles?
km=float(input())
miles=km*0.62137
print(round(miles,2))


# In[8]:


# ans 2) Write a Python program to convert Celsius to Fahrenheit?
cel=float(input())
fehren=(cel*18)+32
print(round(fehren,2))


# In[11]:


# ans 3) Write a Python program to display calendar?
import calendar
yr=int(input("enter a year: "))
mm=int(input("enter a month: "))
print(calendar.month(yr,mm))


# In[12]:


# ans 4) Write a Python program to solve quadratic equation?
import cmath as cm
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
d=(b**2)-(4*a*c)
neg_ans=(-b-cm.sqrt(d))/2*a
pos_ans=(-b+cm.sqrt(d))/2*a
print("the roots are")
print(neg_ans)
print(pos_ans)


# In[13]:


# ans 5) Write a Python program to swap two variables without temp variable?
a=87
b=98
a,b=b,a
print(a)
print(b)


# In[ ]:




