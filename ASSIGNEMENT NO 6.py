#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Write a Python Program to Find LCM?
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1


# In[10]:


# Write a Python Program to Find HCF?
num1 = 36
num2 = 60
hcf = 1

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
print("Hcf of", num1, "and", num2, "is", hcf)


# In[11]:


# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[14]:


# Write a Python Program To Find ASCII value of a character?
c = 'J'
print("The ASCII value of '" + c + "' is", ord(c))


# In[ ]:




