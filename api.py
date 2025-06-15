from flask import Flask, request, jsonify
import pickle
import time


next_day_price = pickle.load(open('next_day_price.pkl','rb'))
next_week_price = pickle.load(open('next_week_price.pkl','rb'))
next_month_price = pickle.load(open('next_month_price.pkl','rb'))

app = Flask(__name__)


def next_day():
    current_time = int(time.time())  # Get current Unix timestamp
    prices = next_day_price
    number_day = len(next_day_price)
    timestamps = [current_time + i * 86400  for i in range(number_day)]
    data = [{"t": t, "y": y} for t, y in zip(timestamps, prices)]
    return data

def next_week():
    current_time = int(time.time())  # Get current Unix timestamp
    prices = next_week_price
    number_week = len(next_week_price)
    timestamps = [current_time + i * 86400  for i in range(number_week)]
    data = [{"t": t, "y": y} for t, y in zip(timestamps, prices)]
    return data

def next_month():
    current_time = int(time.time())  # Get current Unix timestamp
    prices = next_month_price
    number_month = len(next_month_price)
    timestamps = [current_time + i * 86400  for i in range(number_month)]
    data = [{"t": t, "y": y} for t, y in zip(timestamps, prices)]
    return data


@app.route('/')
def home():
    return "Hello, World!"

@app.route('/day', methods=['GET'])
def day():
    predictions = next_day()
    return jsonify({"data": predictions, "message": "success"})
    return jsonify(data)

@app.route('/week', methods=['GET'])
def week():
    predictions = next_week()
    return jsonify({"data": predictions, "message": "success"})
    return jsonify(data)

@app.route('/month', methods=['GET'])
def month():
    predictions = next_month()
    return jsonify({"data": predictions, "message": "success"})
    return jsonify(data)


print(len(next_month_price))

if __name__ == '__main__':
    app.run(debug=True)