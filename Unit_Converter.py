import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

# Streamlit App UI
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom Light Theme Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
        }
        .stMarkdown h1, .stMarkdown p {
            color: #333 !important;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            font-size: 16px;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .stSuccess {
            color: #007bff !important;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: #007bff;'>🔄 Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #333;'>Convert different units instantly!</p>", unsafe_allow_html=True)

category = st.selectbox("Choose a category", ["Length", "Temperature", "Weight"])
unit_options = {}

if category == "Temperature":
    unit_options = {"Celsius to Fahrenheit": celsius_to_fahrenheit, "Fahrenheit to Celsius": fahrenheit_to_celsius}
elif category == "Length":
    unit_options = {"Meters to Kilometers": meters_to_kilometers, "Kilometers to Meters": kilometers_to_meters}
elif category == "Weight":
    unit_options = {"Kg to Pounds": kg_to_pounds, "Pounds to Kg": pounds_to_kg}

conversion_type = st.selectbox("Select Conversion Type", list(unit_options.keys()))
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

if st.button("Convert"):
    converted_value = unit_options[conversion_type](value)
    st.markdown(f"<p class='stSuccess'>Converted Value: {converted_value:.2f}</p>", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #ddd;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 16px; color: #333;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
