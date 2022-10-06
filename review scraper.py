#!/usr/bin/env python
# coding: utf-8

# In[25]:


from flask import Flask , render_template , request , jsonify


# In[1]:


from bs4 import BeautifulSoup as bs 


# In[2]:


from urllib.request import urlopen as urReq


# In[3]:


flipcart_url = "https://www.flipkart.com/search?q="+"iphone11"


# In[4]:


flipcart_url


# In[5]:


response_website = urReq(flipcart_url)


# In[6]:


data_flipkart=response_website.read()


# In[7]:


beautifyed_html=bs(data_flipkart,"html.parser")


# In[8]:


bigbox=beautifyed_html.find_all("div",{"class":"_1AtVbE col-12-12"})


# In[9]:


product6="https://www.flipkart.com" + bigbox[6].div.div.div.a['href']


# In[10]:


import requests


# In[11]:


requests.get(product6)


# In[12]:


product66=requests.get(product6)


# In[13]:


product66.encoding='utf-8'


# In[14]:


product6_page=bs(product66.text,"html.parser")


# In[15]:


all_review=product6_page.find_all('div',{"class":"_16PBlm"})


# In[16]:


len(all_review)


# In[17]:


all_review[5].div.find_all('div' , {'class' : ""})[0].div.text


# In[18]:


rating = all_review[5].div.div.div.div.text


# In[19]:


rating


# In[20]:


name=all_review[5].div.div.find_all('p',{"class":"_2sc7ZR _2V5EHH"})[0].txt


# In[21]:


comment_header=all_review[5].div.div.div.p.text


# In[22]:


comment_header


# In[23]:


all_review[5].div.find_all('p' , {"class":"_2sc7ZR"})[1].text


# In[24]:


product6_page.find_all('div' , {"class":"_30jeq3 _16Jk6d"})[0].text


# In[25]:


for i in all_review:
    price = product6_page.find_all('div' , {"class":"_30jeq3 _16Jk6d"})[0].text
    long_review = i.div.find_all('p' , {"class":"_2sc7ZR"})[1].text
    comment_header = i.div.div.div.p.text
    name  = i.div.div.find_all('p',{"class":"_2sc7ZR _2V5EHH"})[0].text
    rating = i.div.div.div.div.text
    long = i.div.find_all('div' , {'class' : ""})[0].div.text
    print(name, rating, comment_header,long_review,price,long )
    print()


# In[75]:


pip install mysql-connector-python


# In[30]:


import mysql.connector as conn
mydb=conn.connect(host="localhost",user="root",passwd="ankush@123")
cursor=mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS review")
cursor.execute("create table if not exists review.storereview (price varchar(30) ,comment_header varchar(90), name varchar(90),rating varchar(90),bigcomment varchar(90))")


# In[ ]:




