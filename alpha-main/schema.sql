CREATE TABLE Users (
  id          SERIAL PRIMARY KEY,
  username    VARCHAR(255) NOT NULL,
  password    VARCHAR(255) NOT NULL,
  name        VARCHAR(255) NOT NULL,
  email       VARCHAR(255) NOT NULL
);

CREATE TABLE Portfolios (
  id          SERIAL PRIMARY KEY,
  name        VARCHAR(255) NOT NULL,
  type        VARCHAR(255) NOT NULL,
  market      VARCHAR(255) DEFAULT NULL,
  currency    VARCHAR(255) NOT NULL,
  user_id     INTEGER,
  FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Stocks (
  id          SERIAL PRIMARY KEY,
  ticker_symbol   VARCHAR(10) NOT NULL,
  name        VARCHAR(255) NOT NULL,
  shares      INTEGER NOT NULL,
  portfolio_id    INTEGER,
  FOREIGN KEY (portfolio_id) REFERENCES Portfolios(id)
);

CREATE TABLE Transactions (
  id          SERIAL PRIMARY KEY,
  created_datetime TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  type        VARCHAR(255) NOT NULL,
  price       DECIMAL(10, 2) NOT NULL,
  shares      INTEGER NOT NULL,
  stock_id    INTEGER,
  FOREIGN KEY (stock_id) REFERENCES Stocks(id)
);

CREATE TABLE Dividends (
  id          SERIAL PRIMARY KEY,
  amount      DECIMAL(10, 2) NOT NULL,
  ex_dividend_date  DATE NOT NULL,
  payment_date  DATE NOT NULL,
  stock_id    INTEGER,
  FOREIGN KEY (stock_id) REFERENCES Stocks(id)
);

CREATE TABLE Cash (
  id          SERIAL PRIMARY KEY,
  amount      DECIMAL(10, 2) NOT NULL,
  currency    VARCHAR(255) NOT NULL,
  portfolio_id    INTEGER,
  FOREIGN KEY (portfolio_id) REFERENCES Portfolios(id)
);
