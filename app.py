# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 19:22:34 2021

@author: ajayr
"""

from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
model = pickle.load(open('logistic_regression.pkl', 'rb'))
@app.route('/')
def home():
    return render_template("home.html")


@app.route('/heart-prediction', methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        age = request.form.get("age")
        sex = request.form.get("sex")
        chestpain = request.form.get("cp")
        bp = request.form.get("bp")
        chol = request.form.get("chol")
        bs = request.form.get("bs")
        ecg = request.form.get("ec")
        heartrate = request.form.get("hb")
        exercise = request.form.get("ex")
        oldpeak = request.form.get("ang")
        slope = request.form.get("sl")
        vessels = request.form.get("ves")
        thalassemia = request.form.get("thl")
        final = model.predict([[age, sex, chestpain, bp, chol, bs, ecg, heartrate,exercise, oldpeak,slope,vessels,thalassemia]])
        if age != None:
            if final==0:
                txt = "The result is POSITIVE."
                txt1 = "Please continue with further treatment."
            elif final==1:
                txt = "The result is NEGATIVE."
                txt1 = "Even though keep eye on cholestrol, bp and blood sugar level ."
        return render_template("predict.html", txt =txt, txt1 = txt1)
    else:
        return render_template('predict.html')
@app.route('/about')

def about():
    return render_template("about.html")


if __name__== '__main__':
    app.run(debug=True, port=1234)
    