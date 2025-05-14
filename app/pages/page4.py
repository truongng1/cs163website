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
        ], style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "50%", "padding": "10px", "margin": "0 auto"}),

    html.Div([
        html.Ul([
            html.Li("Clear seasonal fluctuations are visible, with recurring peaks and dips that align with weather trends.",
                    style={"fontSize": "18px"}),
        ], style={"paddingLeft": "30px"}),

        html.Div([
            html.Img(src='../static/result_1_2.png',
                     style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "50%", "padding": "10px", "margin": "0 auto"}),
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
    html.H2(" Correlation between Unemployment, Poverty, CPI and 911 Call Volume",
            style={"textAlign": "left", "marginLeft": "40px"}),
    html.Div([
            html.Img(src='../static/result_2_3.png',
                     style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "80%", "padding": "10px", "margin": "0 auto"}),
    html.Ul([
        html.Li("The analysis shows a very weak to no correlation between unemployment, poverty, CPI with 911 call volume. This suggests that these economic indicators alone do not strongly influence emergency call frequency. It's likely that other factors—such as time of year, weather, social events, or unpredictable incidents—play a more significant role, indicating that 911 call volume may be inherently difficult to predict due to its random and situational nature.",
                style={"fontSize": "18px"}),
        html.Br(),
    html.Div([
            html.Img(src='../static/result_2_1.png',
                     style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "80%", "padding": "10px", "margin": "0 auto"}),
        html.Li("The bar chart shows the coefficients from a linear regression model, which quantify the impact of each feature on 911 call volume.",
                style={"fontSize": "18px"}),
        html.Br(),
        html.Div([
            html.Img(src='../static/result_2_2.png',
                     style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "50%", "padding": "10px", "margin": "0 auto"}),
        html.Li("However, coefficient evaluation needs some more scaling",
                style={"fontSize": "18px"}),
    ], style={"paddingLeft": "30px"}),

])