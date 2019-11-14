
from setuptools import setup

setup(name='noteLib',
      maintainer='Tony Butzer',
      maintainer_email='tonybutzer@gmail.com',
      version='1.0.1',
      description='Jupyter Notebook helper functions packaged in a library for reuse',
      packages=[
          'noteLib',
      ],
      install_requires=[
          'folium',
      ],

      )
