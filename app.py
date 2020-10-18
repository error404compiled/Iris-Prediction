# -*- coding: utf-8 -*-
"""
Created on sun 18 oct 17:15:38 2020

@author: hrihik sharma 
"""


import streamlit as st
import pickle
import pandas as pd

from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)


# Get the Keys
def get_key(val,my_dict):
	for key,value in my_dict.items():
		if val == value:
			return key



def predict_note_authentication(SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
    prediction=classifier.predict([[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]])
    return prediction

def main():
    st.title("Iris prediction")
    html_temp = """
    <div style="background-color:orange;padding:10px">
    <h2 style="color:white;text-align:center;">Iris prediction ML App </h2>
    </div>
    """
    prediction_label = {"Iris-setosa":0,"Iris-versicolor":1,"Iris-virginica":2}
    st.markdown(html_temp,unsafe_allow_html=True)
    SepalLength = st.text_input("sepalLength","Type Here")
    SepalWidth = st.text_input("SepalWidth","Type Here")
    PetalLength= st.text_input("PetalLength","Type Here")
    PetalWidth = st.text_input("PetalWidth","Type Here")
    #result=""
    if st.button("Predict"):
        result=predict_note_authentication(SepalLength,SepalWidth,PetalLength,PetalWidth)
        final_result = get_key(result,prediction_label)
        st.success('The Type of Flower is {}'.format(final_result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    

