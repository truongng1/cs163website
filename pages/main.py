import dash
from dash import html

dash.register_page(__name__, path="/", name="Main Page")

layout = html.Div([
    html.H2("This is Main Page")
])
