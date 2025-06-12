from flask import Flask, request, app,render_template, Response
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)

scaler = pickle.load(open(r'C:\Users\anubh\OneDrive\Documents\Coding\DS-Python\ML_Project_Diabetes\models\scaler1.pkl', 'rb'))
model = pickle.load(open(r'C:\Users\anubh\OneDrive\Documents\Coding\DS-Python\ML_Project_Diabetes\models\model_for_prediction.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    result = ''

    if request.method == 'POST':
        try:
            Pregnancies = int(request.form.get('Pregnancies'))
            Glucose = float(request.form.get('Glucose'))
            BloodPressure = float(request.form.get('BloodPressure'))
            SkinThickness = float(request.form.get('SkinThickness'))
            Insulin = float(request.form.get('Insulin'))
            BMI = float(request.form.get('BMI'))
            DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
            Age = float(request.form.get('Age'))

            new_data = scaler.transform([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            predict = model.predict(new_data)

            result = 'Diabetic' if predict[0] == 1 else 'Non-Diabetic'
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('home.html', result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0')