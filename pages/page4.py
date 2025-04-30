import dash
from dash import html, dcc, Input, Output, State, ctx
import pandas as pd
import plotly.express as px
from scipy.stats import zscore

dash.register_page(__name__, name="Major Findings")

# Load and preprocess
df = pd.read_csv('https://storage.googleapis.com/cs163-seniorproject.appspot.com/911_calls_clean.csv')
weather = pd.read_csv('https://storage.googleapis.com/cs163-seniorproject.appspot.com/weather_clean.csv')
df = pd.merge(df, weather, left_on='OFFENSE_DATE', right_on='DATE', how='left')
df.drop(columns=['DATE', 'STATION'], inplace=True)
df['OFFENSE_DATE'] = pd.to_datetime(df['OFFENSE_DATE'])
df.set_index('OFFENSE_DATE', inplace=True)

daily_calls = df.resample('D').size().rename('CALL_COUNT').to_frame()
mean_call_count = daily_calls[daily_calls['CALL_COUNT'] >= 400]['CALL_COUNT'].mean()
daily_calls['CALL_COUNT'] = daily_calls['CALL_COUNT'].apply(lambda x: mean_call_count if x < 400 else x)
daily_calls['ROLLING_MEAN'] = daily_calls['CALL_COUNT'].rolling(window=7).mean()
daily_calls['ROLLING_STD'] = daily_calls['CALL_COUNT'].rolling(window=7).std()
daily_calls['TAVG'] = df['TAVG'].resample('D').mean()
daily_calls['SURGE'] = daily_calls['CALL_COUNT'] > (daily_calls['ROLLING_MEAN'] + 2 * daily_calls['ROLLING_STD'])
daily_calls = daily_calls.reset_index()

# Prepare Z-score by month
df = df.reset_index()
df['Month'] = df['OFFENSE_DATE'].dt.month_name()
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

monthly_totals = df.groupby('Month').size().reindex(month_order)
monthly_z = zscore(monthly_totals)

monthly_z_df = pd.DataFrame({
    'Month': month_order,
    'Z_Score': monthly_z
})
monthly_z_df['Month'] = pd.Categorical(monthly_z_df['Month'], categories=month_order, ordered=True)
# Add color column based on Z_Score
monthly_z_df['Color'] = monthly_z_df['Z_Score'].apply(
    lambda z: 'red' if z > 0 else 'blue' if z < 0 else 'gray'
)
category_order = {'Month': month_order}

# --- Heatmap 1: Year x Month ---
daily_calls_heatmap1 = daily_calls.copy()
daily_calls_heatmap1['Year'] = pd.to_datetime(daily_calls_heatmap1['OFFENSE_DATE']).dt.year
daily_calls_heatmap1['Month'] = pd.to_datetime(daily_calls_heatmap1['OFFENSE_DATE']).dt.month_name()
daily_calls_heatmap1['Month_Num'] = pd.to_datetime(daily_calls_heatmap1['OFFENSE_DATE']).dt.month

pivot_year_month = daily_calls_heatmap1.pivot_table(
    index='Year',
    columns='Month_Num',
    values='CALL_COUNT',
    aggfunc='mean'
)
pivot_year_month.columns = month_order[:len(pivot_year_month.columns)]

heatmap1 = px.imshow(
    pivot_year_month,
    labels=dict(x="Month", y="Year", color="Avg Calls"),
    x=pivot_year_month.columns,
    y=pivot_year_month.index,
    color_continuous_scale="RdBu_r"
).update_layout(
    title="911 Calls Heatmap by Year and Month",
    height=400,
    margin=dict(l=40, r=40, t=60, b=40)
)

# --- Heatmap 2: Day of Week x Month ---
daily_calls_heatmap2 = daily_calls.copy()
daily_calls_heatmap2['Day'] = pd.to_datetime(daily_calls_heatmap2['OFFENSE_DATE']).dt.day_name()
daily_calls_heatmap2['Month'] = pd.to_datetime(daily_calls_heatmap2['OFFENSE_DATE']).dt.month_name()

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
heatmap2_df = daily_calls_heatmap2.pivot_table(
    index='Day',
    columns='Month',
    values='CALL_COUNT',
    aggfunc='mean'
).reindex(index=day_order, columns=month_order)

heatmap2 = px.imshow(
    heatmap2_df,
    labels=dict(x="Month", y="Day", color="Avg Calls"),
    x=heatmap2_df.columns,
    y=heatmap2_df.index,
    color_continuous_scale="RdBu_r"
).update_layout(
    title="911 Calls Heatmap (Day of Week × Month)",
    height=400,
    margin=dict(l=40, r=40, t=60, b=40)
)
# Updated layout with fix + new chart
layout = html.Div([
    html.H1("Major Findings", style={"textAlign": "center"}),

    html.H2(
        "Seasonal Patterns in 911 Call Volume, particularly the impact of Weather and Holidays",
        style={"textAlign": "left", "marginLeft": "40px"}
    ),

    html.Ul([
        html.Li("Call volume displays clear seasonal fluctuations, with recurring peaks and dips that align with the weather patterns",
                style={"fontSize": "18px"}),
        html.Br(),
        html.Li("Surge days, marked by red dots, often appear during the hottest days of the year",
                style={"fontSize": "18px"}),
    ], style={"paddingLeft": "30px"}),

    dcc.Store(id='shared-hover-date'),

    html.Div([
        dcc.Graph(id='calls-graph', style={"width": "48%", "marginLeft": "2%"}),
        dcc.Graph(id='temp-graph', style={"width": "48%", "marginLeft": "1%"})
    ], style={'display': 'flex', 'justifyContent': 'flex-start'}),  # ✅ COMMA FIXED HERE

    html.Div([
    html.Ul([
        html.Li("Clear Seasonal fluctuations, with recurring peaks and dips that align with the weather patterns.",
                style={"fontSize": "18px"}),
        ], style={"paddingLeft": "30px"}),
        dcc.Graph(
            figure=px.bar(
                monthly_z_df,
                x='Month',
                y='Z_Score',
                color='Color',
                category_orders=category_order,
                color_discrete_map={'red': 'crimson', 'blue': 'royalblue', 'gray': 'gray'},
                title='911 Calls by Month (Standardized Z-Score)',
                labels={'Z_Score': 'Z-Score (std deviations from mean)'},
            ).update_layout(
                xaxis_title="Month",
                yaxis_title="Z-Score",
                title_x=0.05,
                margin=dict(l=40, r=20, t=50, b=40),
                xaxis_tickangle=-45,
                height=400,
                showlegend=False
            ),
            style={"width": "90%", "margin": "auto"}
        )
    ]),
    html.Ul([
        html.Ul([
            html.Li(
                "Call volumes rise in mid-year but decline during the holiday season (November and December)",
                style={"fontSize": "18px"}),
            html.Br(),
            html.Li("Contrary to common expectations of increased holiday-related incidents.",
                    style={"fontSize": "18px"}),
            html.Br(),
            html.Li("Warmer weather may lead to more outdoor activities, resulting in higher 911 call volumes.",
                    style={"fontSize": "18px"}),
        ], style={"paddingLeft": "30px"}),
        html.Div([
        html.Div([
            dcc.Graph(figure=heatmap1)
        ], style={"width": "50%"}),

        html.Div([
            dcc.Graph(figure=heatmap2)
        ], style={"width": "50%"})
    ], style={'display': 'flex', 'justifyContent': 'center'}),
    ]),
    html.Br(),
    html.H2(
        "Correlation between Unemployment, Poverty, Inflation rate, Income, GDP and 911 Call Volume",
        style={"textAlign": "left", "marginLeft": "40px"}
    ),
])

# Callback to persist last hover date reliably
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
    return last_date  # retain last valid value

# Update both graphs
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
