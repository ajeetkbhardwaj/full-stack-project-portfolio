import streamlit as st
import numpy as np
import joblib
import warnings

# Ignore warnings for a cleaner output
warnings.filterwarnings('ignore')

# --- MODEL LOADING ---
# Load the pre-trained linear regression model from the specified path.
# Ensure the model file exists before loading to avoid runtime errors.
try:
    lr_model = joblib.load("model/ols_model.pkl")
except FileNotFoundError:
    st.error("Model file 'linear_regression_model.pkl' not found.")
    st.stop() # Stop the app if the model can't be loaded

# --- PREDICTION FUNCTION ---
def predict_sales(tv, radio, newspaper):
    """
    Takes TV, Radio, and Newspaper advertising spends and returns the predicted sales.
    
    Args:
        tv (float): Amount spent on TV advertising.
        radio (float): Amount spent on Radio advertising.
        newspaper (float): Amount spent on Newspaper advertising.
        
    Returns:
        float: The predicted sales amount.
    """
    # Create a numpy array from the inputs in the same order the model expects
    input_features = np.array([[tv, radio, newspaper]])
    
    # Use the loaded model to make a prediction
    prediction = lr_model.predict(input_features)
    
    return prediction[0] # Return the single prediction value

# --- STREAMLIT APP LAYOUT ---
def run():
    """
    Sets up the Streamlit user interface and handles user interaction.
    """
    # Set the title and a simple description for the app
    st.title("Advertising Sales Predictor")
    st.markdown("""
    This app predicts sales based on advertising spending across different channels.
    Enter the advertising budget for TV, Radio, and Newspaper to see the predicted sales revenue.
    """)

    # --- INPUT FIELDS ---
    # Create number input fields for the user to enter advertising spend.
    # Using st.number_input is better than st.text_input for numerical data.
    st.subheader("Enter Advertising Budget")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        tv_spend = st.number_input("📺 TV Spend", min_value=0.0, format="%.2f")
    
    with col2:
        radio_spend = st.number_input("📻 Radio Spend", min_value=0.0, format="%.2f")
        
    with col3:
        newspaper_spend = st.number_input("📰 Newspaper Spend", min_value=0.0, format="%.2f")

    # --- PREDICTION BUTTON AND OUTPUT ---
    # Create a button that triggers the prediction when clicked.
    if st.button("Predict Sales"):
        # Call the prediction function with the user's input
        prediction_result = predict_sales(tv_spend, radio_spend, newspaper_spend)
        
        # Display the prediction in a formatted success message
        st.success(f"Predicted Sales Revenue: ${prediction_result:,.2f}K")

# main function to run the streamlit app
if __name__ == '__main__':
    run()