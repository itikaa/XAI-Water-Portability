# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 10:40:11 2022

@author: Avinash
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('model_trained.sav', 'rb'))

#creating a function
def waterQuality_prediction(input):
   
    #change to numpy array  
    input_as_numpy = np.asarray(input) 
    
    #reshape array 
    input_reshaped = input_as_numpy.reshape(1,-1) 
    
    prediction = loaded_model.predict(input_reshaped) 
    
    print(prediction) 
    if (prediction[0]==0): 
      return "water is not potable" 
    else :
      return "water is potable"
  

def main():
    
    #giving title
    st.title('Water Portability Prediction')
    
    # getting input from user
    
    
    ph = st.text_input("pH value of water")
    Hardness = st.text_input("Hardness value of water")
    Solids = st.text_input("Solids value of water")
    Chloramines = st.text_input("Chloramines value of water")
    Sulfate = st.text_input("Sulfate value of water")
    Conductivity = st.text_input("Conductivity value of water")
    Organic_carbon = st.text_input("Organic_carbon value of water")
    Trihalomethanes = st.text_input("Trihalomethanes value of water")
    Turbidity = st.text_input("Turbidity value of water")
    
    #code for prediction
    diagonosis = ''
    
    #creating a button for prediction
    if st.button('Water Portability Test'):
        diagonosis = waterQuality_prediction([ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity])
    
    st.success(diagonosis)
    
if __name__ == '__main__':
    main()