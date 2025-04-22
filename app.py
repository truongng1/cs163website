import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)
server = app.server
app.layout = html.Div([
    html.Nav([
        html.Ul([
            html.Li(dcc.Link(f"{page['name']}", href=page["relative_path"]))
            for page in dash.page_registry.values()
        ])
    ]),
    dash.page_container
])

server = app.server  # Needed for GAE

if __name__ == '__main__':
    app.run_server(debug=True)
