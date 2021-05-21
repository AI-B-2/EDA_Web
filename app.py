from flask import Flask, jsonify, request, render_template
import json
import plotly, chart_studio
import chart_studio.plotly as py
import plotly.graph_objs as go
import numpy as np

app = Flask(__name__)

# GET /
@app.route('/')
def eda():
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
