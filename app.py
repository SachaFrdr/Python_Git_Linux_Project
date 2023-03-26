import dash
from dash import dcc
from dash import html
import datetime


magic_ticker = "MAGIC"
dogecoin_ticker = "DOGECOIN"

# Convert to dataframe
import pandas as pd
data_magic = pd.read_csv("data_magic.csv", sep= " ", skipinitialspace=True)
data_dogecoin = pd.read_csv("data_dogecoin.csv", sep= " ", skipinitialspace=True)


# Open Dash application
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Manage drop down menu
@app.callback(
    dash.dependencies.Output("ticker-graph", "figure"),
    [dash.dependencies.Input("ticker-dropdown", "value"), dash.dependencies.Input("interval-component", "n_intervals")]
)

def update_ticker_graph(ticker, n):

    if ticker == magic_ticker:
        data = data_magic
    else:
        data = data_dogecoin
    
    fig = {
        "data": [{"x": data["Date"], "y": data["Close"], "type": "line", "line": {"color": "red"}}],
        "layout": {"title": f"Graphic for ({ticker})", "fontSize" : 20}
    }
    
    return fig

# Manage time interval between updates
@app.callback(
    dash.dependencies.Output("update-time", "children"),
    [dash.dependencies.Input("interval-component", "n_intervals")]
)

def update_time(n):
    return f"Mis à jour à: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Manage automatic updates
app.layout = html.Div([
    dcc.Interval(id="interval-component", interval= 5 * 60 * 1000, n_intervals=0),
    html.Div([
        html.H1("Financial Dashboard : MAGIC et DOGECOIN (Sacha FIEREDER)", style={'textAlign': 'center', 'color' : 'black', 'fontSize' : 30}),
        
        dcc.Dropdown(
            id="ticker-dropdown",
            options=[
                {"label": "MAGIC", "value": magic_ticker},
                {"label": "DOGECOIN", "value": dogecoin_ticker}
            ],
            value=magic_ticker,
            style={'color' : 'black'}
        ),
        
        dcc.Graph(
            id="ticker-graph"
        ),
        
        html.Div("Magic", style={'textAlign': 'justify', 'color' : 'black', 'fontSize': 20}
        ),

        html.Div("Dogecoin", style={'textAlign': 'justify', 'color' : 'black', 'fontSize': 20}
        ),
        
        html.Div(style={'textAlign': 'right', 'color' : 'red'},
            id="update-time")
    ])
])

# Launch dash application
if __name__ == '__main__':
    app.run_server(debug = True, host='0.0.0.0')

