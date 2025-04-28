import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load and prepare the data
calls_df = pd.read_csv("https://storage.googleapis.com/cs163-seniorproject.appspot.com/911_calls_clean.csv")
calls_df['OFFENSE_DATE'] = pd.to_datetime(calls_df['OFFENSE_DATE'])
calls_df['YearMonth'] = calls_df['OFFENSE_DATE'].dt.to_period('M').astype(str)

# Group by Year-Month
calls_per_month = calls_df.groupby('YearMonth').size().reset_index(name='Call Volume')

# Create the figure
fig = px.line(
    calls_per_month,
    x='YearMonth',
    y='Call Volume',
    title="911 Call Volume Over Time (2013–2024)",
    labels={'YearMonth': 'Month', 'Call Volume': 'Number of 911 Calls'},
)

# Add big event markers
fig.add_shape(
    type="line",
    x0="2020-03",
    x1="2020-03",
    y0=0, y1=1,
    xref='x', yref='paper',
    line=dict(color="red", width=2, dash="dash"),
)
fig.add_annotation(
    x="2020-03",
    y=1, yref='paper',
    showarrow=False,
    text="COVID Lockdown",
    font=dict(color="red", size=12),
)

fig.add_shape(
    type="line",
    x0="2023-01",
    x1="2023-01",
    y0=0, y1=1,
    xref='x', yref='paper',
    line=dict(color="blue", width=2, dash="dot"),
)
fig.add_annotation(
    x="2023-01",
    y=0.95, yref='paper',
    showarrow=False,
    text="Winter Storm",
    font=dict(color="blue", size=12),
)

fig.add_shape(
    type="line",
    x0="2020-09",
    x1="2020-09",
    y0=0, y1=1,
    xref='x', yref='paper',
    line=dict(color="orange", width=2, dash="dot"),
)
fig.add_annotation(
    x="2020-09",
    y=0.9, yref='paper',
    showarrow=False,
    text="Heat Wave",
    font=dict(color="orange", size=12),
)

fig.update_layout(
    title_font_size=28,
    xaxis_title_font_size=20,
    yaxis_title_font_size=20,
    plot_bgcolor='white',
    title_x=0.5,
    font=dict(size=16),
)

layout = html.Div([
    html.H2("911 Call Analysis (2013–2024)", style={'textAlign': 'center', 'marginTop': '20px'}),
    html.P(
        "This project analyzes 911 calls in San Jose from 2013 to 2024, comparing call patterns with weather conditions and economic factors. "
        "By identifying how these elements influence call volume and location, we uncover peak times and high-risk areas. "
        "These insights can help dispatchers better prepare for future demands, improving response efficiency across the city.",
        style={'textAlign': 'center', 'width': '80%', 'margin': 'auto', 'marginTop': '10px'}
    ),
    dcc.Graph(figure=fig, style={'marginTop': '40px'}),
])

# Register the page
dash.register_page(
    __name__,
    path="/",
    name="Main Page"
)
