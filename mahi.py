#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:31:22 2019

@author: sid
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('diseases.html')


import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('data1.csv')
x = dataset.iloc[:, 0: 13].values

sc_x = StandardScaler()
x = sc_x.fit_transform(x)

with open("hear4", "rb") as f:
    model = pickle.load(f)


def pred(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    test = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    test = pd.DataFrame(test)
    test = sc_x.transform(test)
    ans = str(model.predict(test)[0])
    return ans


@app.route("/submit", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        username = request.form.get('username')
        mobile = request.form.get('mobile no')
        age = request.form.get('age')
        sex = request.form.get('sex')
        cp = request.form.get('cp')
        trestbps = request.form.get('trestbps')
        chol = request.form.get('chol')
        fbs = request.form.get('fbs')
        restecg = request.form.get('restecg')
        thalach = request.form.get('thalach')
        exang = request.form.get('exang')
        oldpeak = request.form.get('oldpeak')
        slope = request.form.get('slope')
        ca = request.form.get('ca')
        thal = request.form.get('thal')

        return render_template('heart.html',
                               results=pred(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope,
                                            ca, thal))

    return render_template('heart.html')


if __name__ == '__main__':
    app.run(debug=True)

# app.run(host="127.0.0.1", port = 5000)