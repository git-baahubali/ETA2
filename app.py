import streamlit as st
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
import pickle

# load model
model = pickle.load(open(r"./estimator.pkl","rb"))

# 17.4933,78.3914,17.4399,78.4983,15,4,1,4,13

start_lat = st.number_input("Enter the start latitude:",value=17.4933)
start_lang = st.number_input("Enter the start longitude:",value = 78.3914)
end_lat = st.number_input("Enter the destination latitude:",value = 17.4399)
end_lang = st.number_input("Enter the destination longitude:",value = 78.4983)
# dist = st.number_input("Enter the distance:",value = 15)
# density = st.number_input("Enter the density:",value = 4)
weather = st.text_input("Enter the weather condition:",value="rainy",)
day  = st.number_input("Enter the day:",value = 4)
hour = st.number_input("Enter the hour:",value = 13)

weather_numerical = (1 if weather == "rainy" else 2 if weather == "foggy" else 3)
if st.button("Submit"):
    # time = model.predict([[start_lat,start_lang ,end_lat,end_lang,dist,density,weather_numerical,day,hour]])[0]
    time = model.predict([[start_lat,start_lang ,end_lat,end_lang,weather_numerical,day,hour]])[0] # dropped distance and density
    st.write("The Estimated time is",time,'minutes')