from flask import Flask, render_template  # jsonify, request,
from confirmed_plot_map import plot_map, tree_map, confirmed_over_time
# import json
# import numpy as np
# import plotly, chart_studio
# import chart_studio.plotly as py
# import plotly.graph_objs as go

app = Flask(__name__)

# GET /
@app.route('/')
def eda():
    map_graphJSON  = plot_map()
    tree_graphJSON = None #tree_map()
    time_graphJSON = confirmed_over_time()
    return render_template('eda.html', plot={'mapgraph': map_graphJSON, 'treegraph':tree_graphJSON, 'timegraph':time_graphJSON})

@app.route('/homepage')
def homepage(): #{
    return render_template('homepage.html')
#}

@app.route('/data')
def data() : #{
    return render_template('data.html')
#}

if __name__ == '__main__':
    app.run()
