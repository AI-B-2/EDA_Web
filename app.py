from flask import Flask, jsonify, request, render_template
import json
import plotly, chart_studio
import chart_studio.plotly as py
import plotly.graph_objs as go
import numpy as np
from confirmed_plot_map import plot_map, tree_map, confirmed_over_time
app = Flask(__name__)

# GET /
@app.route('/')
def eda():
    '''
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.arange(1, 100)
 
    # Create a trace
    trace = go.Scatter(
        x = xScale,
        y = yScale
    )
 
    data = [trace]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('eda.html', plot=graphJSON)
    '''
    map_graphJSON = plot_map()
    tree_graphJSON = tree_map()
    time_graphJSON = confirmed_over_time()
    return render_template('eda.html', plot={'mapgraph': map_graphJSON, 'treegraph':tree_graphJSON, 'timegraph':time_graphJSON})


if __name__ == '__main__':
    app.run(debug=True)
