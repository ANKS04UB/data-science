#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Write a Python Program to Check if a Number is Positive, Negative or Zero?
a=float(input("enter a num: "))
if a>=0:
    if a==0:
        print("number is zero")
    else:
        print("number is positive")
else:
    print("number is negative")


# In[28]:


# Write a Python Program to Check if a Number is Odd or Even?
a=float(input("enter your num: "))
if a%2==0:
    print("entered num is even")
else:
    print("entered num is odd")


# In[31]:


# Write a Python Program to Check Leap Year?
a=int(input("type a year: "))
if a %4==0:
    print("entered year is leap year")
else:
    print("entered year is not a leap year")


# In[35]:


# Write a Python Program to Check Prime Number?
num=int(input("entered preffered num: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime num")
            break
        else:
            print(num, "is a prime num")
else:
    print(num, "is not a prime num")


# In[45]:


# Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
lower_value = 1  
upper_value = 1000  
  
  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  


# In[ ]:





# In[ ]:





# In[20]:





# In[ ]:





# In[ ]:




