# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:14:36 2022
Project: UkraineRussiaWarDataVisualization
@author: MehmetCanDuru
"""


import numpy as np 
import pandas as pd 

import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import plot
from plotly.subplots import make_subplots
import seaborn as sns


# Load human losses
# First day(26 of February) accumulates data for three days (24-26 February)
ru_losses_per = pd.read_csv('C:/Users/MehmetCanDuru\Desktop/KaggleDataSetExample/KaggleDatasetExample/russia_losses_personnel.csv')

# Load equipment losses
ru_losses_eq = pd.read_csv('C:/Users/MehmetCanDuru/Desktop/KaggleDataSetExample/KaggleDatasetExample/russia_losses_equipment.csv')



x, y = ru_losses_per['date'], ru_losses_per['personnel']
# Create plot
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=x, y=y,
                    mode='lines+markers',
                    name='lines+markers'))
plot(fig)
fig.show()



# Create data
x = ru_losses_eq['date']
y0 = ru_losses_eq['aircraft']
y1 = ru_losses_eq['helicopter']
y2 = ru_losses_eq['anti-aircraft warfare']
y3 = ru_losses_eq['drone']

# Create plot
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=x, y=y0,
                    mode='lines+markers',
                    name='Aircraft'))
fig.add_trace(go.Scatter(x=x, y=y1,
                    mode='lines+markers',
                    name='Helicopter'))
fig.add_trace(go.Scatter(x=x, y=y2,
                    mode='lines+markers',
                    name='Anti-aircraft warfare'))
fig.add_trace(go.Scatter(x=x, y=y3,
                    mode='lines+markers',
                    name='Drone'))
fig.update_layout(legend_orientation="h",
                  legend=dict(x=0, y=1, traceorder="normal"),
                  title="Weapons: Air",
                  xaxis_title="Date",
                  yaxis_title="Weapons ",
                  margin=dict(l=0, r=0, t=30, b=0))
plot(fig)
fig.show()


# Create data
x = ru_losses_eq['date']
y0 = ru_losses_eq['tank']
y1 = ru_losses_eq['field artillery']
y2 = ru_losses_eq['APC']
y3 = ru_losses_eq['military auto']

# Create plot
fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=x, y=y0,
                    mode='lines+markers',
                    name='Tank'))
fig.add_trace(go.Scatter(x=x, y=y1,
                    mode='lines+markers',
                    name='Field artillery'))
fig.add_trace(go.Scatter(x=x, y=y2,
                    mode='lines+markers',
                    name='APC'))
fig.add_trace(go.Scatter(x=x, y=y3,
                    mode='lines+markers',
                    name='Military auto'))
fig.update_layout(legend_orientation="h",
                  legend=dict(x=0, y=1, traceorder="normal"),
                  title="Weapons: Ground, Other",
                  xaxis_title="Date",
                  yaxis_title="Weapons ",
                  margin=dict(l=0, r=0, t=30, b=0))
plot(fig)
fig.show()