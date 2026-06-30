import streamlit as st
import pandas as pd
import pickle


# Load model
data = pickle.load(open("model.pkl","rb"))

model = data["model"]
features = data["features"]


st.title("Employee Attrition Prediction")

st.write(
    "Predict whether an employee is likely to leave the company"
)


Age = st.number_input("Age",18,60)

JobLevel = st.number_input(
    "Job Level",
    1,
    5
)

MonthlyIncome = st.number_input(
    "Monthly Income",
    1000,
    20000
)

YearsAtCompany = st.number_input(
    "Years At Company",
    0,
    40
)


OverTime = st.selectbox(
    "OverTime",
    ["Yes","No"]
)


BusinessTravel = st.selectbox(
    "Business Travel",
    [
        "Travel_Rarely",
        "Travel_Frequently",
        "Non-Travel"
    ]
)



if st.button("Predict"):


    # create empty dataframe with all training columns

    input_data = pd.DataFrame(
        0,
        index=[0],
        columns=features
    )


    # fill user values

    input_data["Age"] = Age

    input_data["JobLevel"] = JobLevel

    input_data["MonthlyIncome"] = MonthlyIncome

    input_data["YearsAtCompany"] = YearsAtCompany


    if "OverTime_Yes" in features:
        input_data["OverTime_Yes"] = (
            1 if OverTime=="Yes" else 0
        )


    if "BusinessTravel_Travel_Frequently" in features:
        input_data["BusinessTravel_Travel_Frequently"] = (
            1 if BusinessTravel=="Travel_Frequently" else 0
        )


    prediction = model.predict(input_data)



    if prediction[0]==1:

        st.error(
            "Employee is likely to leave"
        )

    else:

        st.success(
            "Employee is likely to stay"
        )