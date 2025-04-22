import dash
from dash import html

dash.register_page(__name__, name="Project Objective")

layout = html.Div([
    html.H2("Project Objectives")
])
