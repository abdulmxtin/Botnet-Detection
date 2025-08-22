import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from google.auth.transport import requests
from google.oauth2 import id_token

# Load the saved model
diabetes_model = pickle.load(open('C:/Users/ama32/OneDrive/Documents/Botnet Detection[1]/botnet.sav', 'rb'))

# Function to perform botnet prediction
def predict_botnet(maxactive, duration, stdbkptl, stdactive, minfpktl, minbpktl, minactive, meanfpktl, meanbpktl, maxfiat, maxbpktl):
    prediction = diabetes_model.predict([[maxactive, duration, stdbkptl, stdactive, minfpktl, minbpktl, minactive, meanfpktl, meanbpktl, maxfiat, maxbpktl]])
    return prediction

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Botnet prediction using ML', ['Home',  'Botnet prediction using ML', 'About'], default_index=0)
  
# Home Page
if selected == 'Home':
    st.title('Botnet prediction using ML')
    st.image("Botnet2.png", use_column_width=True)

# Botnet Prediction Page
if selected == 'Botnet prediction using ML':
    st.title('Botnet prediction using ML')
    st.image('Botet1.png', use_column_width=True)
    
    # Getting input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        maxactive = st.text_input('maxactive (range 0 to 50000)')
        stdactive = st.text_input('stdactive (range 0 or 1)')
        minactive = st.text_input('minactive (range 0 to 200000)')
        maxfiat = st.text_input('maxfiat (range 0 to 200000)')
    with col2:
        duration = st.text_input('duration (range 0 to 7000000)')
        minfpktl = st.text_input('minfpktl (range 0 to 500)')
        meanfpktl = st.text_input('meanfpktl (range 0 to 500)')
        maxbpktl = st.text_input('maxbpktl (range -1 to 150)')
    with col3:
        stdbkptl = st.text_input('stdbkptl (range 0 or 1)')
        minbpktl = st.text_input('minbpktl (range 0 to 500)')
        meanbpktl = st.text_input('meanbpktl (range -1 to 500)')
    
    # Code for prediction
    if st.button('Botnet Result'):
        prediction = predict_botnet(maxactive, duration, stdbkptl, stdactive, minfpktl, minbpktl, minactive, meanfpktl, meanbpktl, maxfiat, maxbpktl)
        st.success('The output is {}'.format(prediction))

# About Page
if selected == "About":
    st.markdown("<h1 style='text-align: center; color: #FF5733;'>About Botnet Detection using Machine Learning</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    Botnets are networks of compromised computers, also known as "zombies" or "bots," that are controlled remotely by an attacker. 
    They are often used for malicious activities such as launching DDoS attacks, spreading malware, and stealing sensitive information.
    Detecting botnet activities is crucial for cybersecurity.
    """)
    
    st.markdown("""
    This web application demonstrates how machine learning can be used for botnet detection. 
    It uses a Random Forest classifier trained on features extracted from network traffic data to predict whether a given activity is indicative of botnet behavior.
    """)
    
    st.markdown("<h2 style='color: #17A589;'>Built with Streamlit</h2>", unsafe_allow_html=True)
    st.markdown("""
    [Streamlit](https://streamlit.io/) is an open-source Python library that makes it easy to create web applications for machine learning and data science projects.
    With Streamlit, you can build interactive and intuitive user interfaces directly from your Python scripts, without needing to write any HTML, CSS, or JavaScript.
    """)
    
    st.markdown("<h2 style='color: #FFC300;'>How to Use</h2>", unsafe_allow_html=True)
    st.markdown("""
    To use this application, navigate to the "Botnet prediction using ML" page from the sidebar.
    Enter the required features for botnet prediction, and click the "Botnet Result" button to see the prediction output.
    """)
    
    st.markdown("<h2 style='color: #6C3483;'>About OpenAI</h2>", unsafe_allow_html=True)
    st.markdown("""
    [OpenAI](https://openai.com/) is an artificial intelligence research laboratory consisting of the for-profit corporation OpenAI LP and its parent company, the non-profit OpenAI Inc.
    OpenAI's mission is to ensure that artificial general intelligence (AGI) benefits all of humanity.
    """)
    
    if st.button("Additional Resources"):
        st.markdown("<h2 style='color: #3498DB;'>Additional Resources</h2>", unsafe_allow_html=True)
        st.markdown("""
        - [Botnet Detection: A Review and Survey](https://ieeexplore.ieee.org/document/5500799)
        - [Machine Learning for Cybersecurity: A Review](https://link.springer.com/article/10.1186/s13673-020-00230-8)
        - [OpenAI Blog](https://openai.com/blog/)
        - [Python for Network Engineers: Netmiko, NAPALM, pyntc, Telnet](https://www.udemy.com/course/python-for-network-engineers-netmiko-napalm-pyntc-telnet/)
        - [Cybersecurity Specialization](https://www.coursera.org/specializations/cyber-security)
        - [Botnet Detection and Mitigation: A Machine Learning Approach](https://www.springer.com/gp/book/9789811586129)
        """)
    
    st.success("Built by OpenAI")
    st.info("For educational purposes only")
