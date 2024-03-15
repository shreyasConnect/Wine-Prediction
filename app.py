# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 01:28:11 2023

@author: Shreyas Patil
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image


pickle_in=open("model.pkl","rb")
model=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfhur_dioxide,total_sulfhur_dioxide,density,pH,sulphates,alcohol):
    prediction=model.predict([[fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfhur_dioxide,total_sulfhur_dioxide,density,pH,sulphates,alcohol]])
    print(prediction)
    return prediction

def main():
    st.title("Wine Quality Prediction")
    html_temp='''
    <div style="background-color":tomato;padding:10px>
    <h2 style="color:white;text-align:center;">Streamlit Wine Quality Predictor ML App </h2>
    </div>'''
    
    st.markdown(html_temp,unsafe_allow_html=True)
    fixed_acidity=st.text_input("Fixed acidity - Primary fixed acids found in wine are tartaric, succinic, citric, and malic")
    volatile_acidity=st.text_input("Volatile acidity - Volatile acidity is the gaseous acids present in wine.")
    citric_acid=st.text_input("Citric acid - It is weak organic acid, found in citrus fruits naturally.")
    residual_sugar=st.text_input("Residual sugar - Amount of sugar left after fermentation.")
    chlorides=st.text_input("Chlorides - Amount of salt present in wine.")
    free_sulfhur_dioxide=st.text_input("Free Sulfhur Dioxide -  So2 is used for prevention of wine by oxidation and microbial spoilage.")
    total_sulfhur_dioxide=st.text_input("Total Sulfhur Dioxide")
    density=st.text_input("Density")
    pH=st.text_input("pH - In wine pH is used for checking acidity")
    sulphates=st.text_input("Sulphates - Added sulfites preserve freshness and protect wine from oxidation, and bacteria.")
    alcohol=st.text_input("Alcohol - Percent of alcohol present in wine")
    
   
    
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfhur_dioxide,total_sulfhur_dioxide,density,pH,sulphates,alcohol)
    if result==0:
        st.error("Bad Quality Wine.")
    else:
        st.success("Good Quality Wine.")
    if st.button("About"):
        st.text("Built with streamlit")


if __name__=='__main__':
    main()
        
        