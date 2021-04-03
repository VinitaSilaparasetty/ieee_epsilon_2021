import streamlit as st
import pandas as pd
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
from mlxtend.preprocessing import minmax_scaling 
from keras.models import load_model
import warnings
warnings.filterwarnings('ignore')


st.markdown("<h1 style='text-align: center;'>Diabetes Prediction </h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Epsilon 2021</h3>",unsafe_allow_html=True)


#data_file = st.file_uploader("Choose patient records...", type="csv")
#if st.button ("Process"):
	#df=pd.read_csv(data_file)

@st.cache(allow_output_mutation=True)
def load_data(file):
    df=pd.read_csv(file)
    #df=pd.DataFrame(df)
    return df

data_file = st.file_uploader("Choose patient records...", type="csv")

if data_file is not None:
    df = load_data(data_file)  


st.sidebar.title('Select Patient:')

a=st.sidebar.number_input(label='Enter a value upto 10:',min_value=0,value=0,step=1)

name = df.iloc[a,0]
st.sidebar.write(name)    


df=pd.DataFrame(df.drop(columns=['Name']))


df=minmax_scaling(df,columns=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
  
model = tf.keras.models.load_model('diabetes.h5')

submit = st.button('Predict')

if submit:
	prediction = model.predict_classes(df)
	prediction = np.around(prediction[a])
	if prediction == 0:
		st.success('Congratulation! Patient is not diabetic')
	else:
		st.write('Sorry! Patient is Diabetic.')



      

