import dash
from dash import Dash, html, dcc
import flask

server = flask.Flask(__name__)

app = Dash(__name__, server = server,use_pages=True)

@server.route('/static/<path:path>')
def serve_static(path):
    return flask.send_from_directory('static', path)

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

if __name__ == '__main__':
    app.run(debug=True)
