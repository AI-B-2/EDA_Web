import pandas as pd
import numpy as np
import os
import json
import plotly
import chart_studio.plotly as py
import plotly.express as px
import json
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

def plot_map():
    df=pd.read_csv(os.path.join(THIS_FOLDER, 'static/data/country_wise_latest.csv'))
    col = 'Confirmed'
    pal = 'matter'

    df = df[df[col]>0]
    fig = px.choropleth(df, locations="Country/Region", locationmode='country names', 
                  color=col, hover_name="Country/Region", hover_data=[col], color_continuous_scale=pal)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def tree_map():
    df=pd.read_csv(os.path.join(THIS_FOLDER, 'static/data/country_wise_latest.csv'))
    val_list = ['Country/Region','Deaths', 'Recovered', 'Active']

    temp = df[val_list]
    temp = temp.melt(id_vars=val_list[0], value_vars=val_list[1:])
    fig = px.treemap(temp, path=["variable"], values="value", height=225,
                     color_discrete_sequence=['#FE9801', '#21BF73', '#FF2E63'])
    fig.data[0].textinfo = 'label+text+value'

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def confirmed_over_time():
    df= pd.read_csv(os.path.join(THIS_FOLDER, 'static/data/full_grouped.csv'))
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df["Date"].dt.strftime('%Y-%m-%D')
    frame = df["Date"].dt.strftime('%Y-%m-%D')   
    fig = px.choropleth(df, locations="Country/Region", color=np.log(df["Confirmed"]), locationmode='country names', hover_name="Country/Region", animation_frame=frame, color_continuous_scale=px.colors.sequential.matter)
    fig.update(layout_coloraxis_showscale=False)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON