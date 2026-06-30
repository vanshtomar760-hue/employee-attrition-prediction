# Employee Attrition Prediction using Machine Learning

## Project Overview

This project builds a Machine Learning system to predict employee attrition and identify the key factors that influence employees leaving an organization.

The project uses HR analytics data and applies data preprocessing, exploratory data analysis, classification models, and feature importance analysis to generate business insights for HR teams.

## Dataset

IBM HR Analytics Employee Attrition Dataset

- Records: 1470 employees
- Features: 35 employee-related attributes
- Target: Attrition (Yes/No)

## Project Workflow

- Data loading and exploration
- Data cleaning and preprocessing
- Categorical feature encoding
- Feature scaling
- Exploratory Data Analysis
- Machine Learning model training
- Model evaluation
- Business insights generation

## Machine Learning Models

The following models were trained:

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

## Model Performance

Best performing model:

**Logistic Regression**

ROC-AUC Score: 0.80

Accuracy: 75%

## Key Insights

- Overtime is one of the strongest factors affecting employee attrition.
- Sales Representatives have the highest attrition rate.
- Frequent business travel increases employee exit risk.
- Work-life balance and career growth influence retention.

## HR Recommendations

- Improve workload management for employees with high overtime.
- Focus retention programs on high-risk roles and departments.
- Provide better career growth opportunities.

## Technologies Used

Python  
Pandas  
NumPy  
Scikit-Learn  
Matplotlib  
Seaborn  
Jupyter Notebook

## Live Demo

Streamlit App:
https://employee-attrition-prediction-c9n3e5itbc9pvqfynivpkw.streamlit.app/