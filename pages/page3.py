import dash
from dash import html

dash.register_page(__name__, name="Analytical Methods")

layout = html.Div([
    html.H2("Analytical Methods")
])
