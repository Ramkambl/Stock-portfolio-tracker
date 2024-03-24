import dash
from database.models import db
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,title='alpha', external_stylesheets=[dbc.themes.SLATE],suppress_callback_exceptions=True)
with app.server.app_context():
    app.server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alpha.db'
    db.init_app(app.server)
    
    # Define the auth object
