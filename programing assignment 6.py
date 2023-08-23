#!/usr/bin/env python
# coding: utf-8

# In[1]:


# fibonaci series using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


# In[2]:


# factorial using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# In[5]:


# body mass index
weight = int(input("enter your weight in kg: "))
height = int(input("enter your height in meter: "))
BMI = weight/height**2
print(f'your BMI is {BMI}')


# In[4]:


# Write a Python Program to calculate the natural logarithm of any number
import math
x = int(input())
result = math.log(x)
print(result)


# In[1]:


# Write a Python Program for cube sum of first n natural numbers
n = int(input("enter a first n natural number till you want cube sum: "))
result = n**2*((n+1)**2)/4
print(result)


# In[ ]:




