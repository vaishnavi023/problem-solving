#!/usr/bin/env python
# coding: utf-8

# In[9]:


str='Application'
print(str)
str2='''Application test
        Working
        Completed'''
print(str2)
print('str[-1]',str[-1])
print('str[5]',str[5])
print('str[-5]',str[-5])
print( 'str[1:7]',str[1:7])
print('str[:5]',str[:5])
print('str[2:-5]',str[2:-5])
print('str[::-1]',str[::-1])
print('str[::2]',str[::2])


# In[16]:


def ispalindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
print(ispalindrome("Applications"))
print(ispalindrome("aha"))


# In[21]:


#count the digits of a number
n=int(input("Enter a number"))
cnt=0
while(n!=0):
    cnt=cnt+1
    n=n//10
print(cnt)


# In[25]:


def countuppercase(str):
    cnt=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x]) >=65 and ord(lst[x]) <=90: 
            cnt=cnt+1
    
    return cnt
print(countuppercase("AppLication"))
print(countuppercase("TeST"))


# In[26]:


def count(str):
    lst=list(str)
    return len(lst)
count("App")


# In[45]:


def printdigits(str):
    #48-57
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x]) >=48 and ord(lst[x]) <=57:
            print(lst[x],end='')
    print()
    
printdigits("Application2544")
printdigits("ready3456h4")


# In[46]:


def sumofdigits(str):
    #48-57
    sum=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x]) >=48 and ord(lst[x]) <=57:
            #print(lst[x],end='')
            sum=sum+ord(lst[x])-48
    return sum
            
print(sumofdigits("app1541"))


# In[54]:


def sumofdigits(str):
   #48-57
   sum=0
   lst=list(str)
   for x in range(len(lst)):
       if ord(lst[x]) >=48 and ord(lst[x]) <=57:
           #print(lst[x],end='')
           #for x in range(len(lst)):
                if(ord(lst[x])%2==0):
                        sum=sum+ord(lst[x])-48
   return sum
           
print(sumofdigits("app154221"))


# In[55]:


def countuppercase(str):
    cnt=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x]) >=65 and ord(lst[x]) <=90: 
            
    
    return cnt
print(countuppercase("AppLication"))
print(countuppercase("TeST"))


# In[ ]:




