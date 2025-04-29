import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

dash.register_page(__name__, name="Analytical Methods")

# ------------------
# Data preparation
# ------------------
# Read data
calls_df = pd.read_csv("https://storage.googleapis.com/cs163-seniorproject.appspot.com/911_calls_clean.csv")
weather_df = pd.read_csv("https://storage.googleapis.com/cs163-seniorproject.appspot.com/weather_clean.csv")

# Ensure date columns are datetime
weather_df['DATE'] = pd.to_datetime(weather_df['DATE'])
calls_df['OFFENSE_DATE'] = pd.to_datetime(calls_df['OFFENSE_DATE'])

# Group calls by date to get daily call counts
daily_calls = calls_df.groupby('OFFENSE_DATE').size().reset_index(name='CALL_VOLUME')

# Select relevant weather columns
weather_temp = weather_df[['DATE', 'TAVG']]

# Merge them
merged_df = pd.merge(daily_calls, weather_temp, left_on='OFFENSE_DATE', right_on='DATE')

# Drop missing TAVG values
merged_df = merged_df.dropna(subset=['TAVG'])


fig = px.scatter(
    merged_df,
    x='TAVG',
    y='CALL_VOLUME',
    trendline="ols",  # Ordinary Least Squares Trendline
    trendline_color_override="red",
    opacity=0.5,
    labels={'TAVG': 'Average Daily Temperature (°F)', 'CALL_VOLUME': 'Number of 911 Calls'},
    title='Relationship between Temperature and 911 Call Volume'
)
fig.update_layout(
    plot_bgcolor="white",
    xaxis=dict(gridcolor="lightgrey"),
    yaxis=dict(gridcolor="lightgrey")
)

# ------------------
# Layout
# ------------------
layout = html.Div([
    html.H1("Analytical Methods", style={"textAlign": "center", "marginBottom": "20px"}),
    html.H2("Method 1: Correlation Analysis"),

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
    dcc.Graph(figure=fig),


    html.H2("Method 2: Coming Soon..."),
])
