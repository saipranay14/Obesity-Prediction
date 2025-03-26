
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model.pkl")

# Title
st.title("Obesity Prediction System")

# Sidebar for user input
st.header("Enter Patient Details")

# Collecting user input for prediction
age = st.number_input("Age",value=None )
gender = st.selectbox("Gender",['Male', 'Female'])
height = st.number_input("Height (m)",value=None)
weight = st.number_input("Weight (kg)",value=None)
fcvc = st.number_input("Frequency of Vegetable Consumption",value=None)
ncp = st.number_input("Number of Main Meals per Day (1-4)",value=None)
ch2o = st.number_input("Daily Water Intake (Liters)",value=None)
faf = st.number_input("Physical Activity Frequency (Days per Week)",value=None)
tue = st.number_input("Time Using Technology per Day (Hours)",value=None)

# Binary & Categorical Inputs
favc = st.selectbox("Do you eat high-calorie food frequently?", ['NO', 'YES'])
family_history = st.selectbox("Family history of obesity?", ['NO', 'YES'])
smoke = st.selectbox("Do you smoke?", ['NO', 'YES'])
scc = st.selectbox("Do you monitor calories?", ['NO', 'YES'])
caec = st.selectbox("Frequency of Eating Between Meals",['NO','Sometimes','Frequently','Always'])  # Encoded
calc = st.selectbox("Alcohol Consumption", ['NO','Sometimes','Frequently','Always'])  # Encoded
mtrans = st.selectbox("Mode of Transportation", ['Automobile','Bike','Public_transportation','Walking'])  # Encoded

# Prepare input data for prediction

dict = {'NO':0,'YES':1}
encoded={'NO':0,'Sometimes':1,'Frequently':2,'Always':3}
gender1={'Female':0,'Male':1}
MTRANS_Bike	=0
MTRANS_Motorbike=0	
MTRANS_Public_Transportation=0	
MTRANS_Walking=0
if mtrans=='Bike': MTRANS_Bike=1

if mtrans=='Motorbike': MTRANS_Motorbike=1  
if mtrans=='Public_transportation': MTRANS_Public_Transportation=1
if mtrans=='Walking': MTRANS_Walking=1
X_new = np.array([[age, height, weight, fcvc, ncp, ch2o, faf, tue, 
                   encoded[caec],encoded[calc],gender1[gender],MTRANS_Bike,MTRANS_Motorbike,MTRANS_Public_Transportation,MTRANS_Walking,dict[favc],dict[family_history],dict[smoke],dict[scc]]])

# Prediction button
result={0:'Insufficient_Weight' ,
 1:'Normal_Weight' ,
 2:'Obesity_Type_I',
 3:'Obesity_Type_II',
 4:'Obesity_Type_III',
 5:'Overweight_Level_I',
 6:'Overweight_Level_II'}
if st.button("Predict Obesity Level"):
    prediction = model.predict(X_new)
    st.success(f"Predicted Obesity Level: {result[prediction[0]]}")
