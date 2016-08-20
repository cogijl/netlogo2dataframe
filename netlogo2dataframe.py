# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:49:19 2016

@author: jelane
"""

import pandas as pd

# add your own path to the file
targettable = 'C:\Users\foobar.csv'

# now upload the data as a dataframe but strip all th heder information so that
# we are only left with the variable names in the header and the data below
tabledf = pd.DataFrame.from_csv(targettable, header=6, sep=',')

# from here you can add script to analyze the code, or export it into a different
# format with the new headers. 
# or you can export it for analysis in a different program if you really really
# want to