
# coding: utf-8

# In[1]:

# HOMEWORK 1
# Ex 1
# Read NSFG respondent data with .ReadFemResp() function that provided by nsfg.py 
# and assign it a variable that called pres 

from __future__ import print_function, division

import nsfg


# In[2]:

pres = nsfg.ReadFemPreg()
pres


# In[13]:

# Ex 2
# Show the columns and then show the first 20 and last 30 rows of dataframe and lastly print a sentences that show the
# number of rows and columns in this dataframe. For example, "There are .. rows and .. columns" 

first_columns = pres.columns[0:20] 
first_columns



# In[11]:

last_rows = pres.tail(30)
last_rows



# In[17]:

rows = len(pres.index)
rows


# In[16]:

columns = len(pres.columns)
columns


# In[19]:

print ('There are '+str(rows)+' rows and '+str(columns)+' columns.')


# In[ ]:

# Ex 3
# Select the agescrn column from resp and print the value counts. How old are the youngest and oldest 
# respondents(column taht called "agescrn") ? 
x = resp.agescrn
x.counts


# In[ ]:

pres.agescrn.min()


# In[ ]:

max_age = pres.agescrn.max()
max_age


# In[ ]:

# Ex 4 
#What is the number of the Pregnancies in lifetime (column that called "numpregs") for the respondent with caseid 2298? 


# In[ ]:

pres.numpregs[caseid 2298]


# In[ ]:

# Ex 5
#What is the average of the Pregnancies in lifetime (column that called "numpregs") of who is 25 and under 25 years old
# (column taht called "agescrn") 
pres[pres.agesrn<26].numpres.mean()


# In[ ]:

# Ex 6
# What is the average of the Pregnancies in lifetime (column that called "numpregs") of who is at maximum age(column
# taht called "agescrn") ? that you found in 3. question
pres[pres.agescrn==pres.agescrn.max()].numpregs.mean()

