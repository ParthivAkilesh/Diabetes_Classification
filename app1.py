import numpy as np
import pickle
import pandas as pd
import streamlit as st 

mod = open('mod.pkl', 'rb')
model = pickle.load(mod)

def welcome():
    return "Welcome All"

def diabetes_classification(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age):
     
    prediction = model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    print(prediction)
    return prediction

def main():
    st.title("Diabetes Classification")
    html_temp = """
    <div style="background-color:rgb(4, 22, 82);padding:10px">
    <h2 style="color:rgb(241, 153, 20);text-align:center;">WebApp for Diabetes Classification</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)


    a, b = st.columns(2)
    Pregnancies	= a.slider('Enter number of pregnancies :',min_value=0, max_value=20, value=0, step=1)
    Pregnancies	= int(Pregnancies)

    Glucose	= a.text_input('Enter Glucose level :',0)
    Glucose	= int(Glucose)

    BloodPressure	= a.text_input('Enter BloodPressure :',0)
    BloodPressure	= int(BloodPressure)

    SkinThickness	= a.text_input('Enter the skin thickness :',0)
    SkinThickness	= int(SkinThickness)
    	
    Insulin	= b.text_input('Enter insulin level :',0)
    Insulin	= int(Insulin)

    BMI	= b.text_input('Enter BMI :',0)
    BMI	= float(BMI)

    DiabetesPedigreeFunction	= b.text_input('Enter Diabetes Pedigree Function :',0)
    DiabetesPedigreeFunction	= float(DiabetesPedigreeFunction)

    Age	= b.text_input('Enter age :',0)
    Age	= int(Age)	
	
    result=""
    if st.button("Classify"):
        result=diabetes_classification(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age)
        st.success('The result of the classification is  {}'.format('True' if(result  == 0) else 'False'))
    
    
    if st.button("About"):
        st.text("This is a diabetes classification model made using StreamLit")
        st.text("This model is built by Parthiv Akilesh A S")

if __name__=='__main__':
    main()