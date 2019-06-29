#!/usr/bin/env python
# coding: utf-8

# In[5]:


def linearsearch(a,x):
    flag=0
    for i in range(len(a)):
        if a[i] == x:
            flag=1
            break
    if(flag!=0):
        print("number is found")
    else:
        print("Number not found")
a=[18,7,45,77,29,10]
linearsearch(a,97)


# In[1]:


def linearsearchduplicate(a,x):
    flag=0
    for i in range(len(a)):
        if a[i]==x:
            flag=flag+1
    print(flag)
    if(flag!=0):
        print("Number is found")
    else:
        print("Number is not found")
a=[19,88,7,56,3,4,3,5,3,3]
linearsearchduplicate(a,3)


# In[6]:


def linear(a,x):
    flag=0
    for i in range(len(a)):
        if a[i]==x:
            flag=flag+1
            print(i)
    if(flag!=0):
        print("found")
    else:
        print("not found")
a=[1,3,5,2,3]
linear(a,3)


# In[17]:


def l(a,x):
    flag=0
    for i in range(len(a)):
        if a[i]==x:
            flag=flag+1
            print(i)
            j=0
            while(j!=i+1):
                print("!",end="")
                j=j+1
                    
    if(flag!=0):
        print("found")
    else:
        print("not found")
a=[1,3,5,2,3]
l(a,3)


# In[24]:


def l(a):
    sum=0
    for i in range(len(a)):
        if((a[i]%3==0) and (a[i]%5==0)):
            sum=sum+a[i]
    print(sum)
a=[15,20,1,22,45]
l(a)


# In[29]:


def l(a): 
    for i in range(len(a)):
        if i==0 or i==(len(a)-1):
            print(a[i],end="  ")
        else:
            print(a[i-1]*a[i+1],end="  ")
a=[1,2,3,4,5]
l(a)
        
    


# In[31]:


def l(a): 
    for i in range(len(a)):
        if i==0 or i==(len(a)-1):
            print(a[i],end="  ")
        elif((a[i-1]%2==0) and (a[i+1]%2==0)):
            print(a[i],end="  ")
a=[1,6,9,4,16,19,22]
l(a)


# In[34]:


def lm(n):
    l=[]
    while(n!=0):
     r=n%10
     l.append(r)
     n=n//10
    print(l[::-1])
n=int(input("enter the number"))
lm(n)
    


# In[36]:


def l(a): 
    for i in range(len(a)):
        print(a[i],end="")
a=[1,2,3,4,5]
l(a)


# In[40]:


def l(a): 
    for i in range(len(a)):
        if(a[i]%2==0):
            print(a[i],end="")
a=[1,2,3,4,5,6]
l(a)


# In[44]:


def lm(n):
    l=[]
    while(n!=0):
     r=n%10
     if r%2==0:
      l.append(r)
     n=n//10
    print(l[::-1])
n=int(input("enter the number"))
lm(n)


# In[49]:


def l(a): 
    for i in range(len(a)):
        if i==0 or i==(len(a)-1):
            print(a[i],end="  ")
        else:
            print(a[i]+a[i-1],end="  ")
a=[15,19,12,16,4]
l(a)
        
    


# In[56]:


def l(a): 
    m=[]
    for i in range(len(a)):
        if i%2!=0:
           m.append(a[i]**2)
        else:
           m.append(a[i])
    return m
a=[1,2,3,4,5]
print(l(a))
        


# In[57]:


def l(a): 
    for i in range(len(a)):
        if i==0 or i==(len(a)-1) or i==(len(a)-3):
            print(a[i],end="  ")
        else:
            print(a[i]*a[i],end="  ")
a=[1,2,3,4,5]
l(a)

