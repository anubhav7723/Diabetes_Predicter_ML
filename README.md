# 🧠 Diabetes Prediction using Machine Learning

This project is a Machine Learning-based web application that predicts whether a person is diabetic or not based on their health parameters. The application is built using **Flask** for the backend and integrates a trained ML model using **Pickle** for deployment.

---

## 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [EDA (Exploratory Data Analysis)](#eda-exploratory-data-analysis)
- [Model Training](#model-training)
- [Flask Web Application](#flask-web-application)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## 🔍 Overview

This project predicts the diabetes status (positive or negative) of a person using 8 input features like glucose level, blood pressure, insulin level, BMI, etc. The Logistic Regression model achieved an **accuracy of 77%** on the test set.

---

## 📊 Dataset

- **Source:** [Kaggle - Diabetes Dataset](https://www.kaggle.com/datasets/saurabh00007/diabetescsv)
- **Features:**  
  - Pregnancies  
  - Glucose  
  - BloodPressure  
  - SkinThickness  
  - Insulin  
  - BMI  
  - DiabetesPedigreeFunction  
  - Age  
  - Outcome (Target)

---

## 📈 EDA (Exploratory Data Analysis)

Performed detailed analysis to:
- Understand the distribution of features.
- Identify missing or zero-value patterns.
- Visualize correlations.
- Normalize data where necessary.

---

## 🤖 Model Training

- **Algorithm Used:** Logistic Regression  
- **Libraries:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn`
- **Accuracy:** 77% on test data
- The trained model was saved using Python’s `pickle` module for integration into the web app.

---

## 🌐 Flask Web Application

- Created a simple and responsive web interface using **Flask**.
- User can input data through an HTML form.
- On submission, the data is passed to the model, and the prediction (Diabetic / Not Diabetic) is displayed on the same page.

---

## 🚀 How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/Diabetes_Predicter_ML.git
   cd Diabetes_Predicter_ML
