import streamlit as st  # Import the Streamlit library for creating web applications

# Define the unit converter function
def unit_converter(value, value_from, value_to):
    
    unit_conversions = {  # Dictionary storing unit conversion factors
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000 
    }

    key = f"{value_from}_{value_to}"  # Generate a key based on the input and output units

    if key in unit_conversions:  # Check if conversion is available
        conversion = unit_conversions[key]  # Retrieve the conversion factor
        return value * conversion  # Perform the conversion
    else:
        return "Conversion not supported"  # Return a message if conversion is not available

st.title("Unit Converter 🔢 ")  # Display the application title

value = st.number_input("Enter the value:", min_value=1.0, step=1.0)  # Input field for the value to be converted

value_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])  # Dropdown for selecting the unit to convert from

value_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])  # Dropdown for selecting the unit to convert to

if st.button("Convert"):  # Button to trigger the conversion
    result = unit_converter(value, value_from, value_to)  # Call the conversion function
    st.write(f"Converted value: {result}")  # Display the converted value

# 🎉 Conclusion: This Streamlit-based Unit Converter provides a simple and efficient way to convert between meters, kilometers, grams, and kilograms. The app ensures ease of use with an interactive UI and real-time calculations. 🚀
