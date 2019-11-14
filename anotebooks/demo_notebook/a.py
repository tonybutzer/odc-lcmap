
# coding: utf-8

# # Open Data Cube Demos
# ## Intersection of these libraries/projects/concepts
# ### Open Data Cube (ODC)
# ### LCMAP (pyccd anyway)
# ### Visualization of Complex Data Structures
# 
# ## Expected Outcomes
# 1. Continue Refining the common context for
#     - leaders
#     - technologists
#     - developers
#     - architects
#     - etc.
# 2. Intro to one year roadmap for ODC Cloud Engineer == Tony
# 3. Explore components in common between ODC and LCMAP (constrained by cloud vision)
#     - also L8 first
#     - USARD tiles and chips
#     - unilateral approaches
#     - overhead and obstacles
#     - etc
# 4. Fulfils committment to monthly (regular cadence) status reports

# ![arch simple](../asset/app1.png)

# # ODC specific View
# 
# ![arch simple](../asset/appODC1.png)
# 
# > If We have time...
# 
# ## We will deep dive into the "metadata", "Dataset" list/array/time-series
# 
# ### Building a datacube is hard!
# 
# #### Once built it is a very powerful tool for data exploration and time series
# 

# # Demo Agenda

# In[42]:


import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.offline as py

py.init_notebook_mode(connected=True)


df = [
   
    
    dict(Task='Next Steps', Start='2018-11-05 10:50', Finish='2018-11-05 10:59', Resource='Overview'),
    dict(Task='pixel_qa', Start='2018-11-05 10:40', Finish='2018-11-05 10:50', Resource='ODC'),
    dict(Task='Water detect', Start='2018-11-05 10:30', Finish='2018-11-05 10:40', Resource='PYCCD'),
    dict(Task='NDVI Chip', Start='2018-11-05 10:20', Finish='2018-11-05 10:30', Resource='ODC'),
    dict(Task='Folium Tile', Start='2018-11-05 10:10', Finish='2018-11-05 10:20', Resource='Map'),
    dict(Task='Introduction', Start='2018-11-05 10:02', Finish='2018-11-05 10:10:00', Resource='Overview')
]

colors = dict(Strategy = 'rgb(46, 137, 205)',
              Overview = 'rgb(114, 44, 121)',
              Map = 'rgb(198, 47, 105)',
              PYCCD = 'rgb(58, 149, 136)',
              ODC = 'rgb(107, 127, 135)')

fig = ff.create_gantt(df, colors=colors, index_col='Resource', title='Demo Schedule',
                      show_colorbar=True, bar_width=0.8, showgrid_x=True, showgrid_y=True)
py.iplot(fig, show_link=False)


# # Time Permitting - deep dive into Dataset lists
