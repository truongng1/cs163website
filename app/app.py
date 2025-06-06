import dash
from dash import Dash, html, dcc

app = Dash(__name__,use_pages=True)

app.layout = html.Div([
    html.Nav([
        html.Div("Group 5", style={
            "color": "white",
            "fontWeight": "bold",
            "fontSize": "20px",
            "marginLeft": "20px"
        }),
        html.Ul([
            html.Li(
                dcc.Link(
                    page["name"],

                    href=page["relative_path"],
                    style={"color": "white", "textDecoration": "none", "padding": "0 15px"}
                )
            )
            for page in dash.page_registry.values()
        ],
            style={
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
                "listStyleType": "none",
                "margin": "0",
                "padding": "0",
                "flexGrow": "1"
            })
    ], style={
        "display": "flex",
        "alignItems": "center",
        "backgroundColor": "#111",
        "padding": "10px"
    }),

    html.Div(dash.page_container, style={"padding": "20px"})
])
server = app.server
if __name__ == '__main__':
    app.run(debug=True)
