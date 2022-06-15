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

