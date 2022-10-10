# from http import client
from flask import Flask
from flask import request
from flask import jsonify



import pickle

def load(filename):
    with open(filename, 'rb') as f_in:
        return pickle.load(f_in)


dv = load('dv.bin')
model = load('model1.bin')

app = Flask("churn")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    X = dv.transform([data])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return result


if __name__ == "__main__":
    app.run(debug=True, port=9696)