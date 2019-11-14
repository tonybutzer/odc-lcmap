#!/usr/bin/env python
# coding: utf-8

# # Load ARD Product definitions for
# 
# ## USARD
# 
# ## Landsat 5,7,8 (Surface Reflectance)
# 
# 
# ## Index this metadata into a relational database
# ### POSTGRESQL
# 
# 
# ### References
# 
# https://landsat.usgs.gov/sites/default/files/documents/LSDS-1873_US_Landsat_ARD_DFCB.pdf
# 
# 

# In[1]:


# !ls


# In[2]:


get_ipython().system(' cp ../datacube.conf .')


# In[3]:


get_ipython().system('datacube --help')


# In[4]:


get_ipython().system('datacube --version')


# In[5]:


get_ipython().system('datacube system init')


# In[ ]:


get_ipython().system(' echo hi')


# In[ ]:


get_ipython().system(' (cd ../pkg; ./dropDatabaseTables.sh )')


# # How to dump/clear the database (datacube)
# 
# ## What tables do I drop and how
# 
# ```
# psql -U dc_user datacube
# # localuser1234
# 
# \dt agdc.*
# 
# 
# Truncate agdc.dataset, agdc.dataset_location, agdc.dataset_source, agdc.dataset_type ;
# 
# ```

# In[ ]:


get_ipython().system('datacube product add ../product_definition/wip-product_definition_USARD_L5.yaml  ## L5')


# In[ ]:


get_ipython().system('datacube product list')


# In[ ]:


get_ipython().system('echo "Now run the prepare script you have\'nt written yet"')


# In[ ]:


get_ipython().system('python3 ../bin/prepare_L7.py ga-odc-eros-ard-west --prefix=usard/LT05   # L5')


# In[ ]:


get_ipython().system("datacube dataset search product ='landsat_5_USARD' |grep id |wc -l")


# In[ ]:


# !datacube dataset search product ='landsat_5_USARD' 


# In[ ]:


# !datacube dataset search product ='landsat_5_USARD' |grep s3


# In[ ]:


get_ipython().system('datacube product add ../product_definition/wip-product_definition_USARD_L7.yaml  ## L7')


# In[ ]:


get_ipython().system('python3 ../bin/prepare_L7.py ga-odc-eros-ard-west --prefix=usard/LE07   # L7')


# In[ ]:


get_ipython().system('datacube product add ../product_definition/product_definition_USARD_L8_V2.yaml')


# In[ ]:


get_ipython().system('python3 ../bin/prepare_L8.py ga-odc-eros-ard-west --prefix=usard/LC08')


# In[ ]:


get_ipython().system('datacube product list')


# In[ ]:


get_ipython().system("datacube dataset search product ='landsat_5_USARD' |grep id |wc -l")
get_ipython().system("datacube dataset search product ='landsat_7_USARD' |grep id |wc -l")
get_ipython().system("datacube dataset search product ='landsat_8_USARD' |grep id |wc -l")


# ## The END
