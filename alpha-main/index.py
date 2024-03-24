from dash.dependencies import Input, Output
from dash import html, dcc
from app import app
import layouts
import callbacks
import dash

server = app.server  # create the application instance

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Store(id='store', storage_type='local')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/transactions':
        return layouts.page_2_layout
    elif pathname == '/register':
        return layouts.registration_layout
    else:
        return layouts.login_layout

if __name__ == "__main__":
    app.run_server(debug=True)