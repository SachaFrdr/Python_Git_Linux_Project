import dash
from dash import dcc
from dash import html
import datetime
import pandas as pd


#Sur le dashboard, on utilise les cryptomonnaies Magic et Dogecoin.
magic_ticker = "MAGIC"
dogecoin_ticker = "DOGECOIN"


#On importe les données contenues dans les fichiers csv
data_magic = pd.read_csv("data_magic.csv", sep= " ", skipinitialspace=True)
data_dogecoin = pd.read_csv("data_dogecoin.csv", sep= " ", skipinitialspace=True)


#On ouvre une application Dash
app = dash.Dash(__name__, suppress_callback_exceptions=True)


#On utilise un callback pour changer de crypto
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
        "data": [{"x": data["Date"], "y": data["Close"], "type": "line", "line": {"color": "blue"}}],
        "layout": {"title": f"Graphic for ({ticker})", "fontSize" : 18}
    }
    
    return fig


#On utilise un callback pour les mises à jour automatiques
@app.callback(
    dash.dependencies.Output("update-time", "children"),
    [dash.dependencies.Input("interval-component", "n_intervals")]
)


#On affiche la date de la dernière mise à jour
def update_time(n):
    return f"Dernière mise à jour : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"


app.layout = html.Div([
    dcc.Interval(id="interval-component", interval= 5 * 60 * 1000, n_intervals=0),
    html.Div([
        html.H1("Financial Dashboard : MAGIC and DOGECOIN (Sacha FIEREDER)", style={'textAlign': 'center', 'color' : 'black', 'fontSize' : 28}),
        
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
        
        html.Div("MAGIC is the native token of Treasure. Treasure is the decentralized video game console connecting games and communities together through imagination, MAGIC, and NFTs. Dogecoin is a cryptocurrency that was created on December 6th, 2013 based on the popular Doge Internet meme and features a Shiba Inu on its logo. The codebase of the project was a fork of Litecoin, in which most of the same features such hash hashing algorithm were inherited, with the only difference of branding and large inflationary supply. You may buy Dogecoin on centralized exchanges such as Binance, Crypto.com, Coinbase, Bitfinex, and more.", style={'textAlign': 'justify', 'color' : 'black', 'fontSize': 18}
        ),
        
        html.Div(style={'textAlign': 'right', 'color' : 'blue'},
            id="update-time")
    ])
])


#On lance l'application
if __name__ == '__main__':
    app.run_server(debug = True, host='0.0.0.0')

