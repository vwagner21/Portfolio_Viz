# PARALLEL PLOT VISUALIZATION
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from itertools import repeat

pd.set_option('display.max_colwidth', None)
theme_set = pd.read_excel('SWS+Portfolio+Themes_May+26,+2020_14.11 (1).xlsx','Sheet1',index_col=None,na_value=['NA'])
# 55 Projects with 20 themes.
theme_set = theme_set.fillna(0)
theme_set = theme_set.replace('X',1)
theme_set = theme_set.drop(labels='Unnamed: 21',axis = 1)

 
# 1) Iterate through columns, add up the total for each theme.
# 2) Create a list with theme anmes repeated the above number of times per corresponding theme.
# 3) Create an empty list. Iterate thorugh the elements in each column, if 1: add project to list, otherwise proceed.
theme_set.iloc[:,1:].apply(pd.to_numeric)
theme_set['Networks & Coalitions'].sum()
theme_list = []
for colName, colData in theme_set.iloc[:,1:].iteritems():
    sumCol = theme_set[colName].sum()
    theme_list.extend(repeat(colName, sumCol))

theme_list


project_list = []
for colName, colData in theme_set.iloc[:,1:].iteritems():
    counter = 0
    for num in colData:
        if num == 1:
            project_list.append(theme_set['Project Names'][counter])
        counter += 1


project_list

fig = go.Figure(go.Parcats(
    dimensions=[
        {'label': 'Theme',
         'values': theme_list},
        {'label': 'Project',
         'values': project_list},
        ]
))

fig.show()
