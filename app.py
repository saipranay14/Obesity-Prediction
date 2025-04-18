
import streamlit as st
import joblib
import numpy as np
import os

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(MODEL_PATH)

# Title
st.title("Obesity Prediction System")

# Sidebar for user input
st.header("Enter Patient Details")

# Collecting user input for prediction
age = st.number_input("Age",value=None )
gender = st.selectbox("Gender",['Male', 'Female'])
height = st.number_input("Height (m)",value=None)
weight = st.number_input("Weight (kg)",value=None)
fcvc = st.selectbox("Frequency of vegetable consumption.", ['Never', 'Sometimes','Always'])
ncp = st.number_input("Number of Main Meals per Day (1-4)",value=None)
ch2o = st.selectbox("Daily water intake.", ['1 liter or less','2 to 4 liters','More than 4 liters'])
faf = st.selectbox("Frequency of physical activity.", ['Never', 'Sometimes','Frequency','Always'])
tue = st.selectbox("Time spent using technology devices (e.g., computer, TV).", ['None','1-2 hours','3-4 hours','More than 4 hours'])

# Binary & Categorical Inputs
favc = st.selectbox("Do you eat high-calorie food frequently?", ['NO', 'YES'])
family_history = st.selectbox("Family history of obesity?", ['NO', 'YES'])

scc = st.selectbox("Do you monitor calories?", ['NO', 'YES'])
caec = st.selectbox("Do you eat any food between main meals?",['Never','Sometimes','Frequently','Always'])  # Encoded
smoke = st.selectbox("Do you smoke?", ['NO', 'YES'])
calc = st.selectbox("Alcohol Consumption", ['Never','Sometimes','Frequently','Always'])  # Encoded
mtrans = st.selectbox("Mode of Transportation", ['Automobile','Bike','Public_transportation','Walking'])  # Encoded

# Prepare input data for prediction
fcvc1={'Never':1,  'Sometimes':2, 'Always':3}
ch2o1={'1 liter or less':1,'2 to 4 liters':2,'More than 4 liters':3}
dict = {'NO':0,'YES':1}
tue1={'None':0,'1-2 hours':1,'3-4 hours':2,'More than 4 hours':3}
encoded={'Never':0,'Sometimes':1,'Frequently':2,'Always':3}
gender1={'Female':0,'Male':1}
MTRANS_Bike	=0
MTRANS_Motorbike=0	
MTRANS_Public_Transportation=0	
MTRANS_Walking=0
if mtrans=='Bike': MTRANS_Bike=1

if mtrans=='Motorbike': MTRANS_Motorbike=1  
if mtrans=='Public_transportation': MTRANS_Public_Transportation=1
if mtrans=='Walking': MTRANS_Walking=1
X_new = np.array([[age, height, weight, fcvc1[fcvc], ncp, ch2o1[ch2o], encoded[faf], tue1[tue],encoded[caec],encoded[calc],gender1[gender],MTRANS_Bike,MTRANS_Motorbike,MTRANS_Public_Transportation,MTRANS_Walking,dict[favc],dict[family_history],dict[smoke],dict[scc]]])

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
