#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Write a Python Program to Find the Factorial of a Number
num = int(input("Enter a number: "))
factorial=1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[14]:


# Write a Python Program to Display the multiplication Table?
num = int(input("Display multiplication table of "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)


# In[15]:


# Write a Python Program to Print the Fibonacci sequence?
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b


# In[16]:


# Python program to check if the number is an Armstrong number or not
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# In[26]:


# Write a Python Program to Find Armstrong Number in an Interval?
lower = 100
upper = 2000
for num in range(lower, upper + 1):
    order = len(str(num))
    sum = 0
    temp = num
while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
        
if num == sum:
       print(num)


# In[33]:


# Write a Python Program to Find the Sum of Natural Numbers?
num = 16
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
while(num > 0):
       sum += num
       num -= 1
       print("The sum is", sum)


# In[ ]:




