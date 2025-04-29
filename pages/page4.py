import dash
from dash import html

dash.register_page(__name__, name="Major Findings")

layout = html.Div([
    html.H2("Major Findings", style={"textAlign": "center", "marginBottom": "20px", "fontFamily": "Courier New"}),
    html.H2("Seasonal Patterns in 911 Call Volume, particularly the impact of Weather and Holidays", style={"fontFamily": "Courier New"}),
    html.Div([
        html.Div([
            html.Img(src='../static/result_1_1.png',
                     style={
                         'maxWidth': '85%',  # Adjust width to fit side by side
                         'height': 'auto',
                         'margin': '10px'
                     }),
            html.H3('Clear Seasonal fluctuations, with recurring peaks and dips that align with the weather patterns.\n',
                    style={'textAlign': 'center', "fontFamily": "Courier New"})
        ], style={'textAlign': 'center', 'margin': '10px'}),

        html.Div([
            html.Img(src='../static/result_1_2.png',
                     style={
                         'maxWidth': '85%',  # Adjust width to fit side by side
                         'height': 'auto',
                         'margin': '10px'
                     }),
            html.H3([
                'Call volumes rise in mid-year but decline during the holiday season (November and December)', html.Br(),
                'Contrary to common expectations of increased holiday-related incidents.', html.Br(),
                'Warmer weather may lead to more outdoor activities, resulting in higher 911 call volumes.'
            ], style={'textAlign': 'center', "fontFamily": "Courier New"})
        ], style={'textAlign': 'center', 'margin': '10px'})

    ], style={
        'display': 'flex',  # Enables side-by-side layout
        'justifyContent': 'center',  # Centers the images horizontally
        'alignItems': 'flex-start',  # Aligns the images vertically
        'marginTop': '20px'
    }),


    html.Div([
        html.Div([
            html.Img(src='../static/result_1_3.png',
                     style={
                         'maxWidth': '85%',  # Adjust width to fit side by side
                         'height': 'auto',
                         'margin': '10px'
                     }),
        ], style={'textAlign': 'center', 'margin': '10px'}),
        html.Div([
            html.Img(src='../static/result_1_4.png',
                     style={
                         'maxWidth': '85%',  # Adjust width to fit side by side
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
