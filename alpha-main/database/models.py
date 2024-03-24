from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    portfolios = db.relationship('Portfolios', backref='users', lazy=True)

class Portfolios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    market = db.Column(db.String(255))
    currency = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    stocks = db.relationship('Stocks', backref='portfolios', lazy=True)
    cash = db.relationship('Cash', backref='portfolios', lazy=True)

class Stocks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker_symbol = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    current_price = db.Column(db.Numeric(10,2), nullable =True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'))

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_datetime = db.Column(db.DateTime,default=datetime.datetime.utcnow ,nullable=False)
    type = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    shares = db.Column(db.Integer, nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'))
    stock = db.relationship('Stocks', backref=db.backref('transactions', lazy=True))

class Dividends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    ex_dividend_date = db.Column(db.Date, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stocks.id'))
    stock = db.relationship('Stocks', backref=db.backref('dividends', lazy=True))

class Cash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    currency = db.Column(db.String(255), nullable=False)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'))
