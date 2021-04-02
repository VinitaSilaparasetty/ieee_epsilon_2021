import streamlit as st
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.preprocessing import minmax_scaling 
from keras.models import load_model
sns.set()
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline


st.markdown("<h1 style='text-align: center;'>Diabetes Prediction </h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Epsilon 2021</h3>",unsafe_allow_html=True)

file_to_be_uploaded = st.file_uploader("Choose patient records...", type="csv")

st.text('2. Results of your selection:')

gesture = pd.read_csv('/Users/apple/Desktop/diabetes.csv')

st.sidebar.title('Select a Patient:')

a=st.sidebar.number_input(label='Enter a value upto 255:',min_value=0,value=0,step=1)

    
    # Take the label
label = diabetes['label'][a]
    

    
    



st.cache(allow_output_mutation=True)
model = tf.keras.models.load_model('hand_gesture.h5')
predictions=model.predict_classes(x_test)
  

st.success('Done!')

#st.image(predictions[a].astype('uint8'),clamp=True)
st.text('The alphabet is {}'.format(chr(ord('`')+label)))



      

