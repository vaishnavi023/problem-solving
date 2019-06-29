#!/usr/bin/env python
# coding: utf-8

# In[2]:


def test():
    return
test()


# In[6]:


class Demo:
    def test(self):
        print("test() for the class and method")
        return
obj=Demo()
obj.test()


# In[10]:


def fact(n):
    fact=1
    while(n!=0):
        fact=fact*n
        n=n-1
    return fact
fact(5)


# In[14]:


class Demo1:
    def fact(self,n):
        fact=1
        while(n!=0):
            fact=fact*n
            n=n-1
        return fact
p1=Demo1()
p1.fact(5)


# In[16]:


class Demo2:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
        
    def add(self,p1,p2):
        return p1+p2

c1=Demo2(10,20)
print(c1.add(10,20))


# In[21]:


class person():
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(person):
    def isEmployee(self):
        return True
emp=person("Anil")
print(emp.getName(),emp.isEmployee())
emp1=Employee("Akhil")
print(emp1.getName(),emp1.isEmployee())


# In[23]:


lst=[1,2,3,4]
print(lst)


# In[4]:


import numpy as np
lst=[1,2,3,4]
array=np.array(lst)
print(array)


# In[28]:


lst=[1,2,3,4]
array=np.array(lst)
print(array.shape)
print(array.dtype)
print(array)


# In[30]:


lst=[1.2,5.3,7.5,8.5]
array=np.array(lst)
print(array.shape)
print(array.dtype)


# In[34]:


#Re shape
#numpy.reshape
a1=np.array([(1,2,3),(4,5,6)])
print(a1)
a1.reshape(3,2)
#a1.reshape(6,1)


# In[36]:


#append some data
#vstack(array1,array2)
a1=np.array([1,2,3])
a2=np.array([4,5,6])
print(np.vstack((a1,a2)))


# In[39]:


#generate random numbers from np
a1=np.random.normal(5,0,10)
print(a1)


# In[41]:


np.zeros((2,2),dtype=np.int64)


# In[43]:


np.ones((4,3),dtype=np.int64)


# In[47]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
print(A)


# In[50]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(A)[2]=5
print(A)


# In[5]:


A=np.matrix(np.ones((4,4),dtype=np.int64))
np.asarray(A)[1][3]=14
np.asarray(A)[3][3]=16
print(A)


# In[7]:


import numpy as np
np.arange(1,10)


# In[10]:


np.arange(1,100,9)


# In[13]:


np.arange(2,20,2)
#np.arange(1,25,2)


# In[15]:


#indexing and slicing of numpy
a1=np.array([(1,2,3),(4,5,6)])
print(a1)


# In[19]:


a1=np.array([(1,2,3),(4,5,6)])
print("Second Row: ",a1[1])


# In[20]:


a1=np.array([(1,2,3),(4,5,6)])
print("Slicing Last Coloumn : ",a1[:,2])


# In[22]:


a1=np.array([(1,2,3),(4,5,6)])
print("Row and coloumn",a1[1,:1])


# ##### some math operations on given random numbers
# ##### min     --least number
# ##### max     --largest number
# ##### mean    --mean
# ##### median  --median

# In[25]:


a1=np.random.normal(5,1,10)
print(a1)
print("Min value =",np.min(a1))
print("Max value =",np.max(a1))
print("Mean value =",np.mean(a1))
print("Median value =",np.median(a1))


# In[27]:


#multiplication 
c1=np.array([1,2])
c2=np.array([4,5])
np.dot(c1,c2)


# In[31]:


c1=np.array([(1,2),(3,4)])
c2=np.array([(3,4),(1,2)])
np.dot(c1,c2)


# In[33]:


b1=np.array([(1,5),(6,9)])
b2=np.array([(1,3),(1,6)])
np.matmul(b1,b2)

