import pandas as pd
import numpy as np
# to load json files
import json
# datetime oprations
from datetime import timedelta
import datetime as dt
import plotly#, chart_studio
# import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
# import plotly.figure_factory as ff
from plotly.subplots import make_subplots
# for offline ploting
from plotly.offline import plot, init_notebook_mode
# init_notebook_mode(connected=True)
import json


full_grouped = pd.read_csv('full_grouped.csv')

def plot_map():
    df=pd.read_csv('country_wise_latest.csv')
    col = 'Confirmed'
    pal = 'matter'
    
    df = df[df[col]>0]
    fig = px.choropleth(df, locations="Country/Region", locationmode='country names', 
                  color=col, hover_name="Country/Region", 
                  title=col, hover_data=[col], color_continuous_scale=pal)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def tree_map():
    df=pd.read_csv('country_wise_latest.csv')
    val_list = ['Country/Region','Deaths', 'Recovered', 'Active']
 
    temp = df[val_list]
    temp = temp.melt(id_vars=val_list[0], value_vars=val_list[1:])
    fig = px.treemap(temp, path=["variable"], values="value", height=225, 
                     color_discrete_sequence=['#FE9801', '#21BF73', '#FF2E63'])
    fig.data[0].textinfo = 'label+text+value'

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def confirmed_over_time():
    df= pd.read_csv('full_grouped.csv')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df["Date"].dt.strftime('%Y-%m-%D')
    frame = df["Date"].dt.strftime('%Y-%m-%D')
    
    fig = px.choropleth(df, locations="Country/Region", color=np.log(df["Confirmed"]), locationmode='country names', hover_name="Country/Region", animation_frame=frame, title='Cases over time', color_continuous_scale=px.colors.sequential.matter)
    fig.update(layout_coloraxis_showscale=False)
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON