import streamlit as st
import pickle
import numpy as np
import os

# Get the absolute path to the file
file_path = os.path.join(os.path.dirname(__file__), 'irisdataset.pkl')

# Open the file
with open(file_path, 'rb') as f:
    model = pickle.load(f)
    # ...existing code...
st.title("Iris dataset visualization and Prediction")
speal_length = st.slider("Sepal Length",1.0,8.0)
speal_width = st.slider("Sepal Width",1.0,8.0)
petal_length = st.slider("Petal Length",1.0,8.0)
petal_width = st.slider("Petal Width",1.0,8.0)
if st.button("Predict"):
    input_data = np.array([[speal_length, speal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    species=["Setosa","Versicolor","Virginica"]
    st.success(f"The flower species is {species[prediction]}")