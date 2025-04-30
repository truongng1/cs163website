import dash
from dash import html, dcc, Input, Output, State, ctx
import pandas as pd
import plotly.express as px
from scipy.stats import zscore

dash.register_page(__name__, name="Major Findings")


# ======================
# Layout
# ======================
layout = html.Div([
    html.H1("Major Findings", style={"textAlign": "center"}),

    html.H2("Seasonal Patterns in 911 Call Volume, particularly the impact of Weather and Holidays",
            style={"textAlign": "left", "marginLeft": "40px"}),

    html.Ul([
        html.Li("Call volume displays clear seasonal fluctuations, with recurring peaks and dips that align with weather patterns.",
                style={"fontSize": "18px"}),
        html.Br(),
        html.Li("Surge days, marked by red dots, often appear during the hottest days of the year.",
                style={"fontSize": "18px"}),
    ], style={"paddingLeft": "30px"}),

    dcc.Store(id='shared-hover-date'),

    html.Div([
        html.Div([
            html.Img(src='../static/result_1_1.png',
                     style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "50%", "padding": "10px", "display": "flex", "justifyContent": "center",
                  "alignItems": "center"}),
    ], style={'display': 'flex', 'justifyContent': 'flex-start'}),

    html.Div([
        html.Ul([
            html.Li("Clear seasonal fluctuations are visible, with recurring peaks and dips that align with weather trends.",
                    style={"fontSize": "18px"}),
        ], style={"paddingLeft": "30px"}),

        html.Div([
            html.Img(src='../static/result_1_2.png',
                     style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "50%", "padding": "10px", "display": "flex", "justifyContent": "center", "alignItems": "center"}),
    ]),

    html.Ul([
        html.Li("Call volumes rise in mid-year but decline during the holiday season (November and December).",
                style={"fontSize": "18px"}),
        html.Br(),
        html.Li("This is contrary to common expectations of increased holiday-related incidents.",
                style={"fontSize": "18px"}),
        html.Br(),
        html.Li("Warmer weather may lead to more outdoor activities, resulting in higher 911 call volumes.",
                style={"fontSize": "18px"}),
    ], style={"paddingLeft": "30px"}),

    html.Div([
        html.Div([
            html.Img(src='../static/result_1_5.png', style={"width": "100%"})
        ], style={"width": "50%", "padding": "10px"}),

        html.Div([
            html.Img(src='../static/result_1_6.png', style={"width": "100%"})
        ], style={"width": "50%", "padding": "10px"})
    ], style={'display': 'flex', 'justifyContent': 'center'}),

    html.Br(),

    html.H2("Correlation between Unemployment, Poverty, Inflation Rate, Income, GDP, and 911 Call Volume",
            style={"textAlign": "left", "marginLeft": "40px"}),
])