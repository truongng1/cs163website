import dash
from dash import html

# Register the page with a proper name
dash.register_page(__name__, name="Project Objective")

layout = html.Div([
    html.H1("Project Objective", style={"textAlign": "center", "marginBottom": "20px"}),

    html.P("This project analyzes patterns in 911 call volumes in San Jose from 2013 to 2024, focusing on how weather conditions and economic factors influence emergency call activity.", style={"fontSize": "18px", "textAlign": "justify"}),

    html.P("The focus is on understanding trends in overall call behavior and identifying external factors that contribute to changes in call volume, such as extreme weather events or shifts in economic conditions.", style={"fontSize": "18px", "textAlign": "justify"}),

    html.H2("Project Focus", style={"marginTop": "20px"}),
    html.Ul([
        html.Li("Analyze how seasonal weather patterns, including temperature extremes, impact 911 call activity.", style={"fontSize": "18px"}),
        html.Br(),
        html.Li("Explore the relationship between economic indicators (unemployment, poverty, inflation) and call volume.", style={"fontSize": "18px"}),
        html.Br(),
        html.Li("Identify peak periods of emergency call activity, especially during major weather events or economic downturns.", style={"fontSize": "18px"})
    ], style={"paddingLeft": "30px"}),

    html.P("Understanding these patterns can help police departments, emergency dispatchers, and city planners better allocate resources and prepare for fluctuations in emergency needs throughout the year.", style={"fontSize": "18px", "textAlign": "justify"}),

    html.H2("Data Sources", style={"marginTop": "30px"}),

    html.Ul([
        html.Li([
            html.Img(src="https://storage.googleapis.com/cs163-seniorproject.appspot.com/image/SJPD.png", style={"height": "50px", "marginRight": "10px"}),
            html.Span("911 Calls for Service (San Jose Police Department, 2013–2025)", style={"fontSize": "16px"})
        ], style={"display": "flex", "alignItems": "center", "marginBottom": "10px"}),

        html.Li([
            html.Img(src="https://storage.googleapis.com/cs163-seniorproject.appspot.com/image/uscensus.png", style={"height": "50px", "marginRight": "10px"}),
            html.Span("Economic Indicators (Unemployment rates, poverty levels, inflation, and income growth) — U.S. Census Bureau", style={"fontSize": "16px"})
        ], style={"display": "flex", "alignItems": "center", "marginBottom": "10px"}),

        html.Li([
            html.Img(src="https://storage.googleapis.com/cs163-seniorproject.appspot.com/image/noaa.svg", style={"height": "50px", "marginRight": "10px"}),
            html.Span("Weather Conditions (Daily average temperatures and major events) — NOAA National Centers for Environmental Information", style={"fontSize": "16px"})
        ], style={"display": "flex", "alignItems": "center"})
    ], style={"paddingLeft": "30px"})
])