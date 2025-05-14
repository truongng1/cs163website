from dash import dcc, html, Input, Output
import dash
import pandas as pd
import plotly.express as px

# Load datasets
calls_df = pd.read_csv("https://storage.googleapis.com/cs163-seniorproject.appspot.com/dataset/911_calls/911_calls_clean.csv")
weather_df = pd.read_csv("https://storage.googleapis.com/cs163-seniorproject.appspot.com/dataset/weather/weather_clean.csv")

# Prepare calls dataset
calls_df['OFFENSE_DATE'] = pd.to_datetime(calls_df['OFFENSE_DATE'])
calls_df['Year'] = calls_df['OFFENSE_DATE'].dt.year
calls_df['Month'] = calls_df['OFFENSE_DATE'].dt.month

calls_per_year = calls_df.groupby('Year').size().reset_index(name='Call Volume')

# Prepare weather dataset
weather_df['DATE'] = pd.to_datetime(weather_df['DATE'])
weather_df['Year'] = weather_df['DATE'].dt.year
weather_df['Month'] = weather_df['DATE'].dt.month

# Layout for the page
layout = html.Div([
    html.H1("911 Call Analysis (2013–2024)", style={'textAlign': 'center', 'marginTop': '20px'}),

    html.P(
        "This project analyzes 911 calls in San Jose from 2013 to 2024, comparing call patterns with weather conditions and economic factors. "
        "Insights uncover peak times and high-risk areas, helping dispatchers better prepare for future demands.",
        style={'textAlign': 'center', 'width': '80%', 'margin': 'auto', 'marginTop': '10px', 'fontSize': '20px'}
    ),
    html.Div([
        html.Img(
            src="../static/banner.png",
            style={'width': '50%', 'height': 'auto', 'marginBottom': '20px', 'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto'}
        )
    ]),

    html.H1(
        '3,000,000+ calls in 11 years',
        style={
            'textAlign': 'center',
            'fontSize': '50px',  
            'fontWeight': 'bold',
            'color': '#FF5733',
            'marginTop': '20px'
        }
    ),
    html.H1(
        '830+ calls per day',
        style={
            'textAlign': 'center',
            'fontSize': '40px',  
            'fontWeight': 'bold',  
            'color': '#3498DB',  
            'marginTop': '10px'
        }
    ),

    html.Div([
    html.Div([
        html.Img(
            src='../static/main_1.png',
            style={
                'width': '45%',  
                'height': 'auto',
                'margin': '10px'
            }
        ),
        html.Img(
            src='../static/main_2.png',
            style={
                'width': '45%', 
                'height': 'auto',
                'margin': '10px'
            }
        ),
    ], style={
        'display': 'flex',  
        'justifyContent': 'center',  
        'alignItems': 'center',  
        'marginTop': '20px'
    }),
    ]),

    
    html.Div([
        html.Div([
            dcc.Graph(id='monthly-call-graph', style={'height': '45vh'}),
            dcc.Graph(id='monthly-temp-graph', style={'height': '45vh'}),
        ], style={'width': '40%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            dcc.Graph(id='yearly-call-graph', style={'height': '92vh'}),
        ], style={'width': '59%', 'display': 'inline-block', 'marginLeft': '1%'})
    ], style={'marginTop': '40px'})
])

dash.register_page(
    __name__,
    path="/",
    name="Main Page"
)


# Callback
@dash.callback(
    Output('yearly-call-graph', 'figure'),
    Output('monthly-call-graph', 'figure'),
    Output('monthly-temp-graph', 'figure'),
    Input('yearly-call-graph', 'hoverData')
)
def update_graphs(hoverData):
    # Yearly graph
    fig_year = px.line(
        calls_per_year,
        x='Year',
        y='Call Volume',
        markers=True,
        title="911 Call Volume by Year",
        labels={'Year': 'Year', 'Call Volume': 'Number of 911 Calls'}
    )
    fig_year.update_traces(marker=dict(size=10))
    fig_year.update_layout(
        plot_bgcolor='white',
        title_x=0.5,
        font=dict(size=16)
    )

    # Which year?
    if hoverData is not None:
        selected_year = hoverData['points'][0]['x']
    else:
        selected_year = 2020  # default

    # Monthly calls for that year
    filtered_calls = calls_df[calls_df['Year'] == selected_year]
    monthly_calls = filtered_calls.groupby('Month').size().reset_index(name='Call Volume')

    fig_month_calls = px.bar(
        monthly_calls,
        x='Month',
        y='Call Volume',
        title=f"Monthly 911 Calls in {selected_year}",
        labels={'Month': 'Month', 'Call Volume': 'Number of 911 Calls'}
    )
    fig_month_calls.update_layout(
        plot_bgcolor='white',
        title_x=0.5,
        font=dict(size=16),
        xaxis=dict(tickmode='linear')
    )

    # Monthly temperature for that year
    filtered_weather = weather_df[weather_df['Year'] == selected_year]
    monthly_temp = filtered_weather.groupby('Month')['TAVG'].mean().reset_index()

    fig_month_temp = px.bar(
        monthly_temp,
        x='Month',
        y='TAVG',
        title=f"Average Monthly Temperature in {selected_year}",
        labels={'Month': 'Month', 'TAVG': 'Avg Temp (°F)'}
    )
    fig_month_temp.update_layout(
        plot_bgcolor='white',
        title_x=0.5,
        font=dict(size=16),
        xaxis=dict(tickmode='linear')
    )

    return fig_year, fig_month_calls, fig_month_temp
