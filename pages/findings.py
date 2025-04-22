import dash
from dash import html

dash.register_page(__name__, name="Major Findings")

layout = html.Div([
    html.H2("Major Findings")
])
