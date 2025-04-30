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
    dcc.Graph(figure=fig),


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
    html.Img(src = '../static/method_2_2.png',
             style = {
                'maxWidth': '80%',
                'height': 'auto',
                'margin': '10px'
             }),


    html.H2("Seasonal Decomposition"),
    html.P("We applied seasonal decomposition to the time series of daily 911 call volumes and daily average temperature to identify long-term trends, seasonal patterns, and irregular fluctuations."),
    html.P("This method breaks each time series into three components: trend, seasonality, and residuals. By comparing the decomposed patterns of 911 calls and weather, we can better understand how external factors like temperature influence emergency call behavior over time."),
    html.P("This helps distinguish between temporary spikes (like a heatwave) versus consistent seasonal effects (e.g., higher call volumes in summer)."),
    html.P("This insight is useful for forecasting and resource planning."),
    # (Optional graph placeholder, if you have one)
    # html.Img(src='/assets/seasonal_decomposition_calls.png', style={'width': '80%', 'margin': 'auto', 'display': 'block'}),

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
])
