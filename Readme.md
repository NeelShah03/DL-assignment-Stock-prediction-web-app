Name: Neel Shah
Mis no : 752462009
Batch no : 2

Real-Time Stock Prediction Web App
Problem Statement
Predicting stock price movements is critical for informed financial decision-making. This project offers a real-time tool to forecast whether a stock's price will go up or down, enabling users to make data-driven investment choices.

Overview
A machine learning-powered web app that:

Predicts stock price movements based on historical and real-time data.
Fetches the latest stock information using Yahoo Finance API.
Displays prediction results with probabilities, key metrics, and a 5-day stock price chart.

Features
Machine Learning: Neural network for binary classification of stock price movements.
Real-Time Data: Fetches recent stock data (Open, High, Low, Close, Volume).
Interactive Results: Dynamic charts and detailed metrics.
User-Friendly Interface: Built with Flask and Bootstrap.

Tech Stack
Backend: Flask, Python
Frontend: HTML, CSS (Bootstrap), Chart.js
ML Framework: TensorFlow, Scikit-learn
Data Source: Yahoo Finance API (yfinance)

Setup

1. Prerequisites
Python 3.7 or higher installed.
Required Python libraries:
bash
pip install flask tensorflow yfinance joblib

2. Clone the Repository
Clone the GitHub repository to your local system:
git clone https://github.com/NeelShah03/DL-assignment-Stock-prediction-web-app.git
cd DL-assignment-Stock-prediction-web-app

3. Train the Model (Optional)
If you want to train the model from scratch:
bash
python stock_model.py
This will generate stock_model.h5 (the trained model) and stock_scaler.save (the scaler for preprocessing).

4. Run the Flask App
Start the web server:
bash
python app.py

5. Access the Web App
Open your browser and go to:
http://127.0.0.1:5000/

Usage
Enter a stock ticker (e.g., AAPL, TSLA).
View:
Prediction (Up/Down) with probability.
Stock metrics (Open, High, Low, Close, Volume).
A 5-day stock price chart.
