# BMI Calculator using Streamlit
import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="BMI Calculator", page_icon="🦾", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #fdfcff;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        .title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #663399;
            margin-bottom: 20px;
        }
        .result {
            font-size: 26px;
            font-weight: bold;
            color: #000;
            background-color: #e6f7ff;
            padding: 12px;
            border-radius: 12px;
            text-align: center;
            margin-top: 15px;
        }
        .category {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            margin-top: 1rem;
            padding: 10px;
            border-radius: 10px;
        }
        .bmi-info {
            font-size: 18px;
            background-color: #f0f0ff;
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# App container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="title">Smart BMI Calculator 💪</div>', unsafe_allow_html=True)

    st.markdown("#### 📏 Select your height (in cm):")
    height = st.slider("", 100, 250, 170)

    st.markdown("#### ⚖️ Select your weight (in kg):")
    weight = st.slider("", 30, 200, 65)

    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)
    st.markdown(f'<div class="result">📊 Your BMI is: <strong>{bmi:.2f}</strong></div>', unsafe_allow_html=True)

    # Category with color + emoji
    if bmi < 18.5:
        category = "🚨 Underweight"
        color = "#ffcccc"
    elif 18.5 <= bmi < 25:
        category = "✅ Normal weight"
        color = "#ccffcc"
    elif 25 <= bmi < 30:
        category = "⚠️ Overweight"
        color = "#fff2cc"
    else:
        category = "🔥 Obesity"
        color = "#ffb3b3"

    st.markdown(
        f'<div class="category" style="background-color: {color};">{category}</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
        <div class="bmi-info">
        <h4>📚 BMI Categories</h4>
        <ul>
        <li>🚨 Underweight: BMI < 18.5</li>
        <li>✅ Normal weight: 18.5 ≤ BMI < 25</li>
        <li>⚠️ Overweight: 25 ≤ BMI < 30</li>
        <li>🔥 Obesity: BMI ≥ 30</li>
        </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
