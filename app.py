#Name: Neel Shah
#Mis no : 752462009
#Batch no : 2

from flask import Flask, request, render_template, jsonify
import yfinance as yf
import tensorflow as tf
import numpy as np
import joblib

app = Flask(__name__)

# Load model and scaler
model = tf.keras.models.load_model("stock_model.h5")
scaler = joblib.load("stock_scaler.save")

# Fetch real-time stock data
def fetch_real_time_data(ticker, period="5d", interval="1d"):
    stock_data = yf.Ticker(ticker).history(period=period, interval=interval)
    return stock_data

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the stock ticker from the form
        ticker = request.form["ticker"]

        # Fetch recent stock data
        stock_data = fetch_real_time_data(ticker)
        latest_data = stock_data.iloc[-1]  # Get the most recent row

        # Prepare features for prediction
        features = np.array([[latest_data["Open"], latest_data["High"], latest_data["Low"],
                              latest_data["Close"], latest_data["Volume"]]])
        features_scaled = scaler.transform(features)

        # Predict stock movement
        prediction = model.predict(features_scaled)
        result = "Up" if prediction[0][0] > 0.5 else "Down"
        probability = prediction[0][0] * 100 if result == "Up" else (1 - prediction[0][0]) * 100

        # Prepare data for the chart
        dates = stock_data.index.strftime('%Y-%m-%d').tolist()  # Convert index to date strings
        prices = stock_data["Close"].tolist()

        # Render the result page
        return render_template("result.html",
                               ticker=ticker,
                               prediction=result,
                               probability=f"{probability:.2f}%",
                               open=latest_data["Open"],
                               high=latest_data["High"],
                               low=latest_data["Low"],
                               close=latest_data["Close"],
                               volume=latest_data["Volume"],
                               dates=dates,
                               prices=prices)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
