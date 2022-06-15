from dataclasses import dataclass
import pandas as pd
import streamlit as st
import numpy as np
import datetime as dt
import joblib;

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

    )

cities = (
        "Delhi",
        "Kolkata",
        "Banglore",
        "Mumbai",
        "Chennai",

    )

#load model
model = joblib.load('prediction-model.joblib')

def make_predictions(journey_date, journey_time, arrival_date, arrival_time, source, destination, stops, airline):
    pred_input = []

    stops = int(stops)
    pred_input.append(stops)

    #depart
    journey_day = int(pd.to_datetime(journey_date, format="%Y-%m-%dT%H:%M").day)
    pred_input.append(journey_day)

    journey_month = int(pd.to_datetime(journey_date, format ="%Y-%m-%dT%H:%M").month)
    pred_input.append(journey_month)

    dep_min = int(journey_time.minute)
    pred_input.append(dep_min)

    dep_hour = int(journey_time.hour)
    pred_input.append(dep_hour)

    arrival_min = int(arrival_time.minute)
    pred_input.append(arrival_min)

    arrival_hour = int(arrival_time.hour)
    pred_input.append(arrival_hour)

    arrival_day = int(pd.to_datetime(arrival_date, format="%Y-%m-%dT%H:%M").day)
    pred_input.append(arrival_day)

    duration_min = abs(arrival_min - dep_min)
    pred_input.append(duration_min)

    duration_hour = abs(arrival_hour - dep_hour)
    pred_input.append(duration_hour)

    for a in airlines:
        if a == airline:
            pred_input.append(1)
        else:
            pred_input.append(0)
    
    for b in cities:
        if b == source:
            pred_input.append(1)
        else:
            pred_input.append(0)

    for c in cities:
        if c == source:
            pred_input.append(1)
        else:
            pred_input.append(0)
    
    prediction = model.predict(np.array([pred_input]))

    return int(prediction)

def show_predict_page():
    st.title("Ticket Price Prediction")
    st.write(" ### Insert parameters here! ")

    airline =  st.selectbox("Airline", airlines) 

    col1, col2 = st.columns([2, 1])
    source =  col1.selectbox("Departing City", cities) 
    destination = col2.selectbox("Arrival City", cities)

    total_stops = st.slider("Total Stops", 0, 4, 0)

    col3, col4 = st.columns([4, 3])
    depart_date = col3.date_input("Departure Date")
    depart_time = col4.time_input("Departure Time")

    col5, col6 = st.columns([6, 5])
    arrival_date = col5.date_input("Arrival Date")
    arrival_time = col6.time_input("Arrival Time")

    ok = st.button("Calculate Fare Price")

    if ok:
        with st.spinner('Calculating...'):
            Fare = make_predictions(depart_date, depart_time, arrival_date, arrival_time, source, destination, total_stops, airline)
            Fare_IDR = (Fare-1000) * 188.99
        st.success('Your Fare will be around Rp. ' + str(Fare_IDR))

  
