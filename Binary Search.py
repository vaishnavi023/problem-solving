#!/usr/bin/env python
# coding: utf-8

# In[17]:


def binary(a,l,r,x):
    while(l<=r):
        mid=l+(r-l)//2
        if a[mid]==x:
            return mid
        if a[mid]>x:
            r=mid-1
        else:
            l=mid+1
    return -1
list=[1,4,9,15,25,45,57,88,98]
res=binary(list,0,8,7)
if res!=-1:
    print("Item is found")
else:
    print("Item is not found")


# ## Binary search

# In[16]:


def bsort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if(a[j])>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    for i in range(len(a)):
        print(a[i],end="  ")
list=[19,1,25,6,18,3]
#bsort(list)
list.sort()
print(list)


# ## Bubble sort
