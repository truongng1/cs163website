import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, name="Analytical Methods")
# ------------------
# Layout
# ------------------
layout = html.Div([

    #---------- moved under machine learning --------------
    # html.H1("Analytical Methods", style={"textAlign": "center", "marginBottom": "20px"}),
    # html.H2("Correlation Analysis: "),

    # html.Ul([
    #     html.Li("Input: Average Daily Temperature, Call Volume", style={"fontSize": "18px"}),
    #     html.Br(),
    #     html.Li("Output: Correlation Coefficient (~0.41)", style={"fontSize": "18px"}),
    #     html.Br(),
    #     html.Li("Purpose: Determine if warmer weather increases 911 call volumes", style={"fontSize": "18px"}),
    #     html.Br(),
    #     html.Li(
    #         "Explanation: The correlation coefficient measures the linear relationship between average daily temperature and 911 call volume. A ~0.41 value indicates a moderate positive correlation, suggesting seasonal influences on emergency call patterns.",style={"fontSize": "18px"})
    # ]),
    # dcc.Graph(figure=fig),

    html.H1("Analytical Methods", style={"textAlign": "center", "marginBottom": "20px"}),
    html.H2("Z-score test: "),
    html.Li("To find out which months had unusually high or low 911 call activity, we used a z-score test on the average daily call volume for each month.", style={"fontSize": "18px"}),
    html.Br(),
    html.Li("A z-score tells us how far each month’s call volume is from the overall average, measured in standard deviations. This helps highlight months that stand out.", style={"fontSize": "18px"}),
    html.Br(),
    html.Li("Since Z-score assumes a roughly normal distribution, we first analyzed the distribution of 911 calls per day. The distribution was slightly right-skewed but overall bell-shaped, making it appropriate for Z-score analysis."),
    html.Br(),
    html.H4("Distribution of Daily 911 Calls (With outliers)", style={"marginTop": "20px"}),

    # Replace this with your actual bell curve figure
    html.Div([
        html.Img(src = '../static/method_2_1.png',
            style = {
            'maxWidth': '40%',
            'height': 'auto',
            'margin': '10px'
            }),

        html.Img(src = '../static/outliersFormula.png',
            style={
                    'maxWidth': '40%',  # Adjust width to fit side by side
                    'height': 'auto',
                    'margin': '10px'
            }),

    ], style={
        'display': 'flex',  # Enables side-by-side layout
        'justifyContent': 'center',  # Centers the images horizontally
        'alignItems': 'flex-start',  # Aligns the images vertically
        'marginTop': '20px'
    }),
    
    html.Li("To improve accuracy and reduce the impact of extreme values, we removed outliers using the Interquartile Range (IQR) method before analysis."),
    html.Br(),

    html.H4("Distribution of Daily 911 Calls (Outliers Removed)", style={"marginTop": "20px"}),
    # Replace this with your actual bell curve figure
    html.Div([
            html.Img(src='../static/method_2_2.png',
                     style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "50%", "padding": "10px", "margin": "0 auto"}),

    html.H2("Seasonal Decomposition"),
    html.P("We applied seasonal decomposition to the time series of daily 911 call volumes and daily average temperature to identify long-term trends, seasonal patterns, and irregular fluctuations."),
    html.P("This method shows three components: trend, seasonality, and residuals."),
    html.P("This helps distinguish between temporary spikes (like a heatwave) versus consistent seasonal effects (e.g., higher call volumes in summer)."),

    html.Div([
        html.Div([
            html.Img(src='../static/method_3_1.png',
                     style={
                         'maxWidth': '100%',  # Adjust width to fit side by side
                         'height': 'auto',
                         'margin': '10px'
                     }),
        ], style={'textAlign': 'center', 'margin': '10px'}),
        html.Div([
            html.Img(src='../static/method_3_2.png',
                     style={
                         'maxWidth': '100%',  # Adjust width to fit side by side
                         'height': 'auto',
                         'margin': '10px'
                     }),
        ], style={'textAlign': 'center', 'margin': '10px'}),
    ], style={
        'display': 'flex',  # Enables side-by-side layout
        'justifyContent': 'center',  # Centers the images horizontally
        'alignItems': 'flex-start',  # Aligns the images vertically
        'marginTop': '20px'
    }),


    html.H2("Correlation Analysis: "),

    html.Ul([
        html.Li("Input: Average Daily Temperature, Call Volume", style={"fontSize": "18px"}),
        html.Br(),
        html.Li("Output: Correlation Coefficient (~0.41)", style={"fontSize": "18px"}),
        html.Br(),
        html.Li("Purpose: Determine if warmer weather increases 911 call volumes", style={"fontSize": "18px"}),
        html.Br(),
        html.Li(
            "Explanation: The correlation coefficient measures the linear relationship between average daily temperature and 911 call volume. A ~0.41 value indicates a moderate positive correlation, suggesting seasonal influences on emergency call patterns.",style={"fontSize": "18px"})
    ]),
    html.Div([
            html.Img(src='../static/page3_correlation.png',
                     style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "70%", "padding": "10px", "margin": "0 auto"}),
    html.H2("Machine Learning Prediction"),
    html.P("We deployed machine learning models to predict daily 911 call volumes based temperature, holidays"),
    html.P("We started with linear regression but the models explained only a small portion of the variance in call volume."),

    html.Ul([
        html.Li("Linear Regression: R² = 0.1819"),
        html.Img(src = '../static/method_4_1.png',
                style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
        ], style={"width": "60%", "padding": "10px", "margin": "0 auto"}),

    html.P('Consider the correlation coefficnent and model result, we tried using non-linear models'),
    html.Ul([
        html.Li("Random Forest: R² = 0.1681"),
        html.Img(src='../static/method_4_2.png',
                 style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
    ], style={"width": "60%", "padding": "10px", "margin": "0 auto"}),


    html.P("The Random Forest model's performance is similar to the linear regression model... suggesting that the relationship might not be strongly non-linear"),

    html.P('We tried adding other features...'),
    html.Ul([
        html.Li('Month'),
        html.Li('Day of the week'),
        html.Li('Holidays'),
        html.Li('Average Daily Temperature'),
        html.Li('Weather: Heatwave, Storm'),
        html.Li('Unemployment Rate')
    ]),

    html.P('This time we used ensemble modeling, combining Random Forest and Gradient Boosting to make prediction...'),
    html.Ul([
        html.Li('Random Forest R²: 0.1780'),
        html.Li('Gradient Boosting R²: 0.1128'),
        html.Li('Ensemble R²: 0.1620'),
        html.Img(src='../static/method_4_3.png',
                 style={"width": "100%", "display": "flex", "justifyContent": "center", "alignItems": "center"})
    ], style={"width": "60%", "padding": "10px", "margin": "0 auto"}),
    
], style = {'fontSize': '18px'})
