from dataclasses import dataclass
import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('insert-model-here', 'rb') as file:
        data = pickle.load(file)
    return data

#data = load_model()

#regressor = data["model"]

def show_predict_page():
    st.title("Ticket Price Prediction")
    st.write(" ### Insert parameters here! ")

    airlines = (
        "Jet Airways",
        "IndiGo",
        "AirIndia",
        "SpiceJet",
        "Vistara",
        "Air Asia",
        "GoAir",
        "Jet Airways Business",
        "Trujet",
        "Multiple carriers",
        "Multiple carriers premium economy",
        "Jet Airways Business",
        "Vistara Premium economy",

    )

    sources = (
        "Delhi",
        "Kolkata",
        "Banglore",
        "Mumbai",
        "Chennai",

    )

    destinations = (
        "Delhi",
        "Kolkata",
        "Banglore",
        "Mumbai",
        "Chennai",
    )

    airline =  st.selectbox("Airline", airlines) 
    source =  st.selectbox("Source", sources) 
    destination =  st.selectbox("Destination", destinations) 
    total_stops = st.slider("Total Stops", 0, 4, 0)
    depart_date = st.date_input("Departure Date")
    depart_time = st.time_input("Departure Time")
    arrival_date = st.date_input("Arrival Date")
    arrival_time = st.time_input("Arrival Time")

    ok = st.button("Calculate Fare Price")