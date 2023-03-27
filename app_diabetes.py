import streamlit as st
import pandas as pd
import pickle
model = pickle.load(open('pipe_diabetes.pkl', 'rb'))
st.title('Diabetes Predictor')

preg=st.number_input('Pregnancies')
glu=st.number_input('Glucose Level')
Bp=st.number_input('BloodPressure')
sk=st.number_input('SkinThickness')
ins=st.number_input('Insulin')
bmi=st.number_input('BMI')
dpf=st.number_input('DiabetesPedigreeFunction')
age=st.number_input('Age')

if(st.button('Predict')):
    input_df=pd.DataFrame({'Pregnancies':[preg],'Glucose Level':[glu],'BloodPressure':[Bp],'SkinThickness':[sk],'Insulin':ins,'BMI':[bmi],
                           'DiabetesPedigreeFunction':[dpf],'Age:':[age]})

    y=model.predict(input_df)
    if y==1:
        st.header("You have high chances of Diabetes,Please visit a doctor")
    else:
        st.header("No worries you are fine!!!")

