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


# # Expectation #

# The distribution of a random variable gives us detailed information about how probability is distributed over all the possible values of the variable. But often we would just like a sense of roughly where the distribution is situated on the number line. In other words, we would like some idea of where the center of the distribution is.
# 
# As any student who has taken multiple "midterm" exams in a class knows, words like "middle" and "center" don't have a unique meaning. This chapter is about a particular kind of "center" of the distribution of a random variable.
