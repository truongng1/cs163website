import dash
from dash import html, dcc, Input, Output, State, ctx
import pandas as pd
import plotly.express as px
from scipy.stats import zscore

dash.register_page(__name__, name="Major Findings")

# ======================
# Load and Preprocess Data
# ======================
df = pd.read_csv('https://storage.googleapis.com/cs163-seniorproject.appspot.com/911_calls_clean.csv')
weather = pd.read_csv('https://storage.googleapis.com/cs163-seniorproject.appspot.com/weather_clean.csv')

df = pd.merge(df, weather, left_on='OFFENSE_DATE', right_on='DATE', how='left')
df.drop(columns=['DATE', 'STATION'], inplace=True)
df['OFFENSE_DATE'] = pd.to_datetime(df['OFFENSE_DATE'])
df.set_index('OFFENSE_DATE', inplace=True)

# Daily aggregation and smoothing
daily_calls = df.resample('D').size().rename('CALL_COUNT').to_frame()
mean_call_count = daily_calls[daily_calls['CALL_COUNT'] >= 400]['CALL_COUNT'].mean()
daily_calls['CALL_COUNT'] = daily_calls['CALL_COUNT'].apply(lambda x: mean_call_count if x < 400 else x)
daily_calls['ROLLING_MEAN'] = daily_calls['CALL_COUNT'].rolling(window=7).mean()
daily_calls['ROLLING_STD'] = daily_calls['CALL_COUNT'].rolling(window=7).std()
daily_calls['TAVG'] = df['TAVG'].resample('D').mean()
daily_calls['SURGE'] = daily_calls['CALL_COUNT'] > (daily_calls['ROLLING_MEAN'] + 2 * daily_calls['ROLLING_STD'])
daily_calls = daily_calls.reset_index()

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
        dcc.Graph(id='calls-graph', style={"width": "48%", "marginLeft": "2%"}),
        dcc.Graph(id='temp-graph', style={"width": "48%", "marginLeft": "1%"})
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

# ======================
# Callbacks
# ======================

# Persist last hover date
@dash.callback(
    Output('shared-hover-date', 'data'),
    Input('calls-graph', 'hoverData'),
    Input('temp-graph', 'hoverData'),
    State('shared-hover-date', 'data')
)
def store_hover_date(calls_hover, temp_hover, last_date):
    trigger = ctx.triggered_id
    if trigger == 'calls-graph' and calls_hover:
        return calls_hover['points'][0]['x']
    elif trigger == 'temp-graph' and temp_hover:
        return temp_hover['points'][0]['x']
    return last_date

# Update graphs on hover
@dash.callback(
    Output('calls-graph', 'figure'),
    Output('temp-graph', 'figure'),
    Input('shared-hover-date', 'data')
)
def update_figs(hover_date):
    fig_calls = px.line(daily_calls, x='OFFENSE_DATE', y='CALL_COUNT', title='911 Calls')
    fig_calls.add_scatter(
        x=daily_calls[daily_calls['SURGE']]['OFFENSE_DATE'],
        y=daily_calls[daily_calls['SURGE']]['CALL_COUNT'],
        mode='markers',
        marker=dict(color='red', size=6),
        name='Surge Days'
    )

    fig_temp = px.line(daily_calls, x='OFFENSE_DATE', y='TAVG', title='Avg Temperature (°F)')
    fig_temp.update_layout(yaxis_range=[30, 100])

    if hover_date:
        for fig in [fig_calls, fig_temp]:
            fig.add_vline(x=hover_date, line_dash="dot", line_color="black")

    return fig_calls, fig_temp
