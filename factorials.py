#!/usr/bin/env python
# coding: utf-8

# In[15]:


# Returns the value of the factorial of num if it is defined, otherwise, returns None 


def factorial(num):
    if isinstance(num, int) and num >= 0: 
        result = 1  
        i = num
        while i > 0:
            result *= i
            i -= 1
        return result
    else:
        return None

print(factorial(5))
print(factorial("a"))
print(factorial(0))

   


# In[ ]:


type(1)


# In[14]:





# In[ ]:




