#!/usr/bin/env python
# coding: utf-8

# In[24]:


def createfile(filename):
    f=open(filename,"w")
    f.write("Virtual Machine\n")
    f.write("In computing, a virtual machine (VM) is an emulation of a computer system. Virtual machines are based on computer architectures and provide functionality of a physical computer.\n Their implementations may involve specialized hardware, software, or a combination.There are different kinds of virtual machines, each with different functions:\nSystem virtual machines (also termed full virtualization VMs) provide a substitute for a real machine.\n They provide functionality needed to execute entire operating systems. A hypervisor uses native execution to share and manage hardware, allowing for multiple environments which are isolated from one another, yet exist on the same physical machine.\n Modern hypervisors use hardware-assisted virtualization, virtualization-specific hardware, primarily from the host CPUs.Process virtual machines are designed to execute computer programs in a platform-independent environment.\nSome virtual machines, such as QEMU, are designed to also emulate different architectures and allow execution of software applications and operating systems written for another CPU or architecture. \nOperating-system-level virtualization allows the resources of a computer to be partitioned via the kernel. The terms are not universally interchangeable. ")
    f.close()
    return
createfile("file.txt")


# In[25]:


def readfile(filename):
    f=open(filename,"r")
    if f.mode == "r":
        x=f.read()
        print(x)
    f.close()
    return
readfile("file.txt")


# In[26]:


def countlower(filename):
    cnt=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
        for i in lst:
            if i.islower():
                 cnt=cnt+1
    return cnt
print(countlower("file.txt"))


# In[27]:


def countdigits(filename):
    cnt=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
        for i in range(len(lst)):
            if ord(lst[i]) >=48 and ord(lst[i]) <=51: 
                 cnt=cnt+1
    return cnt
print(countdigits("file.txt"))


# In[28]:


def countSpecialCharacters(filename):
    cnt=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
        for i in range(len(lst)):
            if ord(lst[i]) >=33 and ord(lst[i]) <=47: 
                 cnt=cnt+1
    return cnt
print(countSpecialCharacters("file.txt"))


# In[41]:


def createfile(filename):
    f=open(filename,"w")
    f.write("Name:N Mahema Reddy\nEmailID:mahemareddy1@gmail.com\nMobile Number:6303662392\n")
    f.close()
    return
createfile("Details.txt")


# In[33]:


def readfile(filename):
    f=open(filename,"r")
    if f.mode == "r":
        x=f.read()
        print(x)
    f.close()
    return
readfile("Details.txt")


# In[35]:


import re
def PhoneNumberValidate(phone):
    pattern="^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$"
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
PhoneNumberValidate("6303662392")


# In[37]:


import re
def EmailIDValidate(email):
    pattern="^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    email=str(email)
    if re.match(pattern,email):
        return True
    return False
EmailIDValidate("mahemareddy1@gmail.com")


# In[46]:


import re
def namevalidate(name):
    pattern="^[a-zA-Z]{4,15}[ ][a-zA-Z]{4,15}$"
    name=str(name)
    if re.match(pattern,name):
        return True
    return False   
print(namevalidate("Mahema Reddy"))
print(namevalidate("sai"))

