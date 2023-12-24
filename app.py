import streamlit as st
import os  
from utils import check_folder_exists, show_form
# Strealit app title

st.title("Project X")
st.header("Your personal closer, Jr Harvey Specter")


if st.button("Set Profile"):
    show_form()

st.selectbox("Position applying for?",("full-time","intern","Intern/full-time"))



# Set profile and editprofile buttons


st.selectbox("Select applying for?",("Closer","Sales Manager"))

if st.button("Edit Profile"):
        show_form()







company_link = st.text_input("Enter the company website link")

genrate_email = st.button("Genrate Email")
