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


# # The Normal and Gamma Families #
# 

# 
# The family of normal distributions has a uniquely important place in probability theory and data science. You started working with normal distributions in Data 8 long before you understood much formal probability theory. So you have taken several basic facts for granted without proof. We will start by establishing those facts and then study sums of independent normal variables.
# 
# The gamma family of distributions, properties of which you have established in exercises, arises in numerous contexts. For example, you have seen that the exponential distribution is a member of the gamma family, as is the square of a standard normal variable. Later in this chapter we will collect what we know about the gamma family and see what we can say about sums of independent gamma variables.

# In[2]:




