# Portfolio Management Application

This application allows you to manage your stock portfolio by tracking transactions, dividends, and cash. In this guide, we'll walk you through setting up the project using Docker and Python virtual environment.

## Prerequisites

- Python 3.6 or higher installed on your system

## Setting up the project

1. **Installing Python 3.6 or Later**

Follow the instructions below to install Python 3.6 or a later version on your system.

#### Windows

A. Visit the official Python download page: [Download Python](https://www.python.org/downloads/)

B. Choose a suitable Python version (3.6 or later) and click on the corresponding download link for Windows.

C. Run the installer and follow the instructions. Make sure to check the box that says "Add Python to PATH" during the installation.

#### macOS

A. Install [Homebrew](https://brew.sh/) if you haven't already.

B. Open a terminal and run the following command to install Python 3.6 or later:
  ```
brew install python@3.6
  ```

C. Add the newly installed Python to your `PATH` by adding the following line to your `~/.bash_profile` or `~/.zshrc` file:
  ```
export PATH="/usr/local/opt/python@3.6/bin:$PATH"
  ```

D. Reload your shell configuration:
  ```
source ~/.bash_profile
  ```


2. **Create a Python virtual environment**

In the project directory, create a new Python virtual environment by running the following command:


Activate the virtual environment:

- On Linux or macOS:

  ```
  source venv/bin/activate
  ```

- On Windows:

  ```
  venv\Scripts\activate
  ```

3. **Upgrade pip and install the required packages**

Upgrade pip by running the following command:


Next, install the required packages from the `requirements.txt` file:
  ```
pip install -r requirements.txt
  ```

## How the code works

The application consists of several components:

- `dashapp.py`: The Dash application file that creates an interactive web interface.
- `database/`: This directory contains the database configuration, models, and utility functions.
- `models.py`: Defines the database models for users, portfolios, stocks, transactions, dividends, and cash.
- `functions.py`: Contains the functions to perform operations like buying and selling stocks, registering dividends, and adding cash to the portfolio.
- `schema.sql`: A Schema DDL to create the schema upon creating the database.
- `README.md`: This guide on setting up and understanding the application.


The application allows users to enter their username and portfolio name, create new portfolios, and manage transactions such as buying stocks, selling stocks, and registering dividends. Users can also add cash to their portfolios (under development). The Dash interface provides an interactive way to perform these operations.
