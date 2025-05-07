# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.title("Data Analysis App")

# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     # Read the CSV file into a DataFrame
#     df = pd.read_csv(uploaded_file)

#     # Display the first few rows of the DataFrame
#     st.subheader("Data Preview")
#     st.write(df.head())

#     # Display data summary
#     st.subheader("Data Summary")
#     st.write(df.describe())

#     st.subheader("Filter Data")
#     column = df.columns.to_list()
#     selected_column = st.selectbox("Select a column to filter", column)
#     unique_values = df[selected_column].unique()
#     selected_value = st.selectbox("Select value ", unique_values)
    
#     filtered_data = df[df[selected_column] == selected_value]
#     st.write(filtered_data)

#     st.subheader("Plot Data")
#     x_axis = st.selectbox("Select X-axis column",column)
#     y_axis = st.selectbox("Select Y-axis column",column)

#     if st.button("Generate plot"):
#         st.line_chart(filtered_data.set_index(x_axis)[y_axis])

# else:
#     st.write("waiting for file upload...")



import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="📊 Data Analysis App", page_icon="📈", layout="centered")

# Custom styling
st.markdown("""
    <style>
        # .main-container {
        #     background-color: #f9f9fb;
        #     padding: 30px;
        #     border-radius: 20px;
        #     box-shadow: 0 0 15px rgba(0,0,0,0.05);
        # }
        .section-header {
            font-size: 24px;
            font-weight: bold;
            color: #3e64ff;
            margin-top: 25px;
            margin-bottom: 10px;
        }
        .sub-text {
            font-size: 16px;
            color: #555;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<h1 style="text-align:center; color:#3e64ff;">📊 Smart Data Analysis App</h1>', unsafe_allow_html=True)
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# File Upload
uploaded_file = st.file_uploader("📁 Upload your CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.markdown('<div class="section-header">🔍 Data Preview</div>', unsafe_allow_html=True)
    st.write(df.head())

    st.markdown('<div class="section-header">📈 Data Summary</div>', unsafe_allow_html=True)
    st.write(df.describe())

    st.markdown('<div class="section-header">🎛️ Filter Data</div>', unsafe_allow_html=True)
    column = df.columns.to_list()
    selected_column = st.selectbox("🧩 Select a column to filter", column)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("🔎 Select value", unique_values)

    filtered_data = df[df[selected_column] == selected_value]
    st.success(f"✅ Showing rows where `{selected_column}` is `{selected_value}`")
    st.write(filtered_data)

    st.markdown('<div class="section-header">📉 Plot Data</div>', unsafe_allow_html=True)
    x_axis = st.selectbox("📍 X-axis", column)
    y_axis = st.selectbox("📍 Y-axis", column)

    if st.button("📊 Generate Plot"):
        st.line_chart(filtered_data.set_index(x_axis)[y_axis])
else:
    st.write("📤 Please upload a CSV file to begin analysis.")

st.markdown('</div>', unsafe_allow_html=True)


    