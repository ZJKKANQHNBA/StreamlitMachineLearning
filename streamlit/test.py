import streamlit as st
import numpy as np
import pickle

# Set page configuration
st.set_page_config(
    page_title="Iris Species Predictor",
    page_icon="🌸",
    layout="centered"
)

# App Title and Description
st.title("🌸 Iris Flower Classification")
st.write("""
This app predicts the species of an **Iris** flower based on its sepal and petal measurements.
""")

# Load the trained model
@st.cache_resource
def load_model():
    with open("iris_model.pkl", "rb") as file:
        return pickle.load(file)

try:
    model = load_model()
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Define target classes (matching load_iris().target_names)
target_names = ['setosa', 'versicolor', 'virginica']

# Sidebar or main page input controls
st.subheader("Input Flower Features")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=5.4,
        step=0.1
    )
    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        max_value=10.0,
        value=1.5,
        step=0.1
    )

with col2:
    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=3.4,
        step=0.1
    )
    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        max_value=10.0,
        value=0.2,
        step=0.1
    )

# Prediction button
if st.button("Predict Species"):
    # Format inputs into the shape expected by scikit-learn: (1, 4)
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    # Run inference
    prediction_idx = model.predict(features)[0]
    predicted_species = target_names[prediction_idx]
    
    # Display result
    st.success(f"Predicted Species: **Iris-{predicted_species.capitalize()}**")
    
    # Display prediction probabilities if supported by the model
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(features)[0]
        st.write("---")
        st.write("### Prediction Confidence")
        for name, prob in zip(target_names, probabilities):
            st.write(f"- **{name.capitalize()}**: {prob * 100:.2f}%")
