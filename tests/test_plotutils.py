# Hamdi Kavak
# 
# MIT License
# Plotting wrapper functions.
import numpy as np
from pandas import Series, DataFrame
import datautils as du

# ---- test bar plot wrapper -----
rownames = ['row1', 'row2', 'row3', 'row4', 'row5']
colnames = ['col1', 'col2']
rowdata = np.random.randn(5, 2)*100
df_obj = DataFrame(rowdata, 
                   index=rownames,  
                   columns=colnames)

bar_prop = {'col1':{'color': 'r', 'label': 'Col 1 values'},
            'col2':{'color': 'g', 'label': 'Col 2 values'}}

du.makeBarPlot(df_obj, bar_prop, ylim=None)

# ---- test line plot wrapper ----
rownames = []

for x in range(100):
    rownames.append(x)
colnames = ['col1', 'col2']

rowdata = np.random.randn(100, 2)*100
df_obj = DataFrame(rowdata, 
                   index=rownames,  
                   columns=colnames)

line_prop = {'col1':{'color': 'r', 'label': 'Col 1 values'},
            'col2':{'color': 'g', 'label': 'Col 2 values'}}

du.makeLinePlot(df_obj, line_prop, ylim=None)