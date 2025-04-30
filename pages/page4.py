import dash
from dash import html, dcc

dash.register_page(__name__, name="Major Findings")

layout = html.Div([
    html.H1("Major Findings", style={"textAlign": "center", "marginBottom": "20px", "fontFamily": "Nunito"}),
    html.H2("Seasonal Patterns in 911 Call Volume, particularly the impact of Weather and Holidays", style={'textAlign': 'center',"fontFamily": "Nunito"}),
    # html.Div([
    #     html.Div([
    #         html.Img(src='../static/result_1_1.png',
    #                  style={
    #                      'maxWidth': '100%',  # Adjust width to fit side by side
    #                      'height': 'auto',
    #                      'margin': '10px'
    #                  }),
    #         html.Li('Clear Seasonal fluctuations, with recurring peaks and dips that align with the weather patterns.\n',
    #                 style={"fontFamily": "Nunito"})
    #     ], style={'margin': '10px'}),



    #     html.Div([
    #         html.Img(src='../static/result_1_2.png',
    #                  style={
    #                      'maxWidth': '100%',  # Adjust width to fit side by side
    #                      'height': 'auto',
    #                      'margin': '10px'
    #                  }),
    #         html.Li('Call volumes rise in mid-year but decline during the holiday season (November and December)',
    #                 style = {'fontFamily': 'Nunito'}),
    #         html.Br(),

    #         html.Li('Contrary to common expectations of increased holiday-related incidents.',
    #                 style = {'fontFamily': 'Nunito'}),
    #         html.Br(),

    #         html.Li('Warmer weather may lead to more outdoor activities, resulting in higher 911 call volumes.',
    #                 style = {'fontFamily': 'Nunito'}),

    #     ], style={'margin': '10px'})

    # ], style={
    #     'display': 'flex',  # Enables side-by-side layout
    #     'justifyContent': 'center',  # Centers the images horizontally
    #     'alignItems': 'flex-start',  # Aligns the images vertically
    #     'marginTop': '20px'
    # }),

    html.Img(src='../static/result_1_1.png',
            style={
                'maxWidth': '100%',  # Adjust width to fit side by side
                'height': 'auto',
                'margin': '10px'
            }),

    html.Li('Clear Seasonal fluctuations, with recurring peaks and dips that align with the weather patterns.\n',
        style={"fontFamily": "Nunito"}),


    html.Img(src='../static/result_1_2.png',
                style={
                    'maxWidth': '100%',  # Adjust width to fit side by side
                    'height': 'auto',
                    'margin': '10px'
                }),
    html.Li('Call volumes rise in mid-year but decline during the holiday season (November and December)',
            style = {'fontFamily': 'Nunito'}),
    html.Br(),

    html.Li('Contrary to common expectations of increased holiday-related incidents.',
            style = {'fontFamily': 'Nunito'}),
    html.Br(),

    html.Li('Warmer weather may lead to more outdoor activities, resulting in higher 911 call volumes.',
            style = {'fontFamily': 'Nunito'}),

    html.Div([
        html.Div([
            html.Img(src='../static/result_1_5.png',
                     style={
                         'maxWidth': '100%',  # Adjust width to fit side by side
                         'height': 'auto',
                         'margin': '10px'
                     }),
        ], style={'textAlign': 'center', 'margin': '10px'}),
        html.Div([
            html.Img(src='../static/result_1_5.png',
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
