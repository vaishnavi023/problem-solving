#!/usr/bin/env python
# coding: utf-8

# In[11]:


#PhoneNumberValidate
import re
def PhoneNumberValidate(phone):
    pattern="^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$"
    phone=str(phone)
    if re.match(pattern,phone):
        return True
    return False
print(PhoneNumberValidate(6303662392))
print(PhoneNumberValidate(912889345))
print(PhoneNumberValidate("06303662392"))
print(PhoneNumberValidate("+916303662392"))


# In[14]:


#Validation of rollnumber
#152U1A0501-152U1A0560
#^[1][5][2][U][1][A][0][5][0-6][0-9]$
import re
def Rollnumbervalidate(number):
    pattern="^[1][5][2][U][1][A][0][5][0-6][0-9]$"
    number=str(number)
    if re.match(pattern,number):
        return True
    return False
print(Rollnumbervalidate("152U1A0506"))
print(Rollnumbervalidate("152U1A0452"))


# ## EmailID validation: username@domainname.extension
# ### username: length [6-15] characters,no spl characters, should not end with _, digits,lower
# ### Domainname: [3-8],no spl,all digits and lower
# ### extension: [2-4],no spl,lower
# 

# In[17]:


#^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$
import re
def EmailIDValidate(email):
    pattern="^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{3,18}[.][a-z]{2,4}$"
    email=str(email)
    if re.match(pattern,email):
        return True
    return False
print(EmailIDValidate("mahemareddy1@gmail.com"))
print(EmailIDValidate("$anil_@gmail.com"))


# ### regular expression -- password
# ### parameters -- [6-15]
# ### lower,upper,spl(@,#,$)

# In[21]:


import re
def passwordValidate(password):
    pattern="^[a-zA-z0-9@$#!]{6,15}$"
    password=str(password)
    if re.match(pattern,password):
        return True
    return False
print(passwordValidate("gyfy$332"))
print(passwordValidate("f@#$hAD"))
print(passwordValidate("fhdgfh*45"))


# #### ^[a]...[z]$
# 
# ####^[a].*[z]$

# In[ ]:




