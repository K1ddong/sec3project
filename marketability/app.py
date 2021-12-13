from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)
import sys
sys.path.append('./marketability.pkl')
model = pickle.load(open('marketability.pkl', 'rb'))


@app.route('/', methods=['GET'])
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['d']
    data6 = request.form['d']
    data7 = request.form['d']
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(debug=True)