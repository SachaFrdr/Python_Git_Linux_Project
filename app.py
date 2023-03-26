import dash
from dash import dcc
from dash import html
import datetime


btc_ticker = "BTC"
xrp_ticker = "XRP"

# Convert to dataframe
import pandas as pd
data_btc = pd.read_csv("data_btc.csv", sep= " ", skipinitialspace=True)
data_xrp = pd.read_csv("data_xrp.csv", sep= " ", skipinitialspace=True)


# Open Dash application
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Manage drop down menu
@app.callback(
    dash.dependencies.Output("ticker-graph", "figure"),
    [dash.dependencies.Input("ticker-dropdown", "value"), dash.dependencies.Input("interval-component", "n_intervals")]
)

def update_ticker_graph(ticker, n):

    if ticker == btc_ticker:
        data = data_btc
    else:
        data = data_xrp
    
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
    dcc.Interval(id="interval-component", interval=300 * 1000, n_intervals=0),
    html.Div([
        html.H1("Financial Dashboard : BTC et XRP (Lina FAIROUD)", style={'textAlign': 'center', 'color' : 'black', 'fontSize' : 30}),
        
        dcc.Dropdown(
            id="ticker-dropdown",
            options=[
                {"label": "BTC", "value": btc_ticker},
                {"label": "XRP", "value": xrp_ticker}
            ],
            value=btc_ticker,
            style={'color' : 'black'}
        ),
        
        dcc.Graph(
            id="ticker-graph"
        ),
        
        html.Div("Bitcoin (BTC) is a cryptocurrency, a virtual currency designed to act as money and a form of payment outside the control of any one person, group, or entity, thus removing the need for third-party involvement in financial transactions. It is rewarded to blockchain miners for the work done to verify transactions and can be purchased on several exchanges.", style={'textAlign': 'justify', 'color' : 'black', 'fontSize': 20}
        ),

        html.Div("Ripple is a real-time, cryptocurrency gross-settlement system, currency exchange and remittance network created by Ripple Labs Inc, a US-based technology company. The company then created the XRP cryptocurrency, which it describes as a “digital asset built for global payments”.", style={'textAlign': 'justify', 'color' : 'black', 'fontSize': 20}
        ),
        
        html.Div(style={'textAlign': 'right', 'color' : 'red'},
            id="update-time")
    ])
])

# Launch dash application
if __name__ == '__main__':
    app.run_server(debug = True, host='0.0.0.0')

