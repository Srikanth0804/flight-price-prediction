import streamlit as st

st.title("✈️ Flight Ticket Price Prediction App")
st.subheader("Welcome to my Machine Learning Project!")

st.markdown("""
## 📌 Project Introduction:
Welcome to the **Flight Ticket Price Prediction App**.  
In this project, I have developed a machine learning model using **K-Nearest Neighbors (KNN)** to predict the price of flight tickets based on several factors such as airline, source, destination, stops, travel class, and more.

---

### 📚 Project Overview:
- Built using Python and Streamlit.
- Deployed on Hugging Face Spaces.
- Machine Learning Algorithm: **KNN Regressor**

---

### 👨‍💻 Project by:
**Srikanth Gunti**  
Postgraduate Data Science Student  
Nizam College, Osmania University

---
""")

if st.button('Next'):
    st.switch_page('pages/1_Problem_Statement.py')