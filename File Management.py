#!/usr/bin/env python
# coding: utf-8

# In[4]:


#function for writing a file
def createfile(filename):
    f=open(filename,"w")
    for i in range(10):
        f.write("This is the %d line\n" % i)
    print("File is successfully created and Data is written")
    f.close()
    return
createfile("file.txt")


# In[13]:


#function for reading a file
def readfile(filename):
    f=open(filename,"r")
    if f.mode == "r":
        x=f.read()
        print(x)
    f.close()
    return
readfile("file.txt")


# In[16]:


#data to append
#function to append data
def appenddata(filename):
    f=open(filename,"a")
    f.write("new line 1\n")
    f.write("new line 2\n")
    f.close()
    return
appenddata("file.txt")


# In[18]:


def readfile(filename):
    f=open(filename,"r")
    if f.mode == "r":
        x=f.read()
        print(x)
    f.close()
    return
readfile("file.txt")


# In[22]:


def dataAnalysisWordCount(filename,word):
    f=open(filename,"r")
    if f.mode == "r":
        x=f.read()
        lst=x.split()
        cnt=lst.count(word)
    return cnt
print(dataAnalysisWordCount("file.txt","line"))
print(dataAnalysisWordCount("file.txt","1"))
print(dataAnalysisWordCount("file.txt","rest"))


# In[24]:


#function to count no. of characters in the file
def countcharacter(filename):
    f=open(filename,"r")
    if f.mode =="r":
        x=f.read()
        lst=list(x)
    return len(lst)
print(countcharacter("file.txt"))


# In[27]:


#function to count the uppr case charecters in the file
def countupper(filename):
    cnt=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
        for i in range(len(lst)):#for i in lst:
            if ord(lst[i]) >=65 and ord(lst[i]) <=90: #if i.isupper()
                 cnt=cnt+1
    return cnt
print(countupper("file.txt"))


# In[35]:


#function to count lines in a file
def countlines(filename):
    cnt=0
    f=open(filename,"r")
    if f.mode=="r":
        x=f.read()
        lst=list(x)
    for i in lst:
        if i=="\n":
            cnt=cnt+1
    return cnt
print(countlines("file.txt"))
    


# In[ ]:




