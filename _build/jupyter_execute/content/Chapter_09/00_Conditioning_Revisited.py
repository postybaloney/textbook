#!/usr/bin/env python
# coding: utf-8

# In[1]:


# HIDDEN
from datascience import *
from prob140 import *
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')
import math
from scipy import stats
from scipy import misc


# # Conditioning, Revisited #

# In the next couple of chapters we are going to study random processes indexed by time. We have looked at some of these already – for example, a sequence of trials can be thought of as a random process indexed by time.
# 
# Naturally, we will be interested in what we can predict about a process in the future given that we know its present value. Techniques involving conditioning are going to be useful. We know some of these techniques already, and in this chapter we will develop them further. 

# In[2]:




