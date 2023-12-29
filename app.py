import streamlit as st
import os  
from utils import check_folder_exists, show_info_form, show_roles_form, chech_file_exists
import http.client
# Strealit app title

st.title("Project X")
st.header("Your personal closer, Jr Harvey Specter")

if chech_file_exists("new_profiles/profile.txt"):

    if st.button("Edit Profile"):
        show_roles_form()
        show_info_form()

    st.selectbox("Position applying for?",("full-time","intern","Intern/full-time"))



    # Set profile and editprofile buttons

    # read the roles from the roles.txt file
    with open("new_profiles/roles.txt", "r") as f:
        roles = f.readlines()
        role_applying = st.selectbox("Select applying for?",roles)
    # st.selectbox("Select applying for?",("Closer","Sales Manager"))



    # Side Bar Section
    with st.sidebar:

        # Save openai api key
        openai_apikey = st.text_input("Open AI API Key")
        save_openai_key = st.button("Save OpenAI API Key")

        if save_openai_key:
            if openai_apikey == "":
                st.warning("Please enter API Key")
            else:
                with open("temp_config.py", "a") as f:
                    # f.write("[API_KEYS]\n")
                    f.write("OPENAI_API_KEY=")
                    f.write(f"{openai_apikey} \n")
                st.success("API Key added successfully")   

        # Svae gemini api key
        gemini_apikey = st.text_input("Gemini API Key")
        save_gemini_key = st.button("Save Gemini API Key")

        if save_gemini_key:
            if gemini_apikey == "":
                st.warning("Please enter API Key")
            else:
                with open("temp_config.py", "a") as f:
                    # f.write("[API_KEYS]\n")
                    f.write("GEMINI_API_KEY=")
                    f.write(gemini_apikey + "\n")
                st.success("API Key added successfully")       

    company_link = st.text_input("Enter the company website link")

    genrate_email = st.button("Genrate Email")
    try:
        response_data = http.client.HTTPSConnection(company_link)
    except Exception as e:
        st.error(e)

    if genrate_email:
        if company_link == "":
            st.warning("Please enter company website link")
        else:
            
            st.success("Email genrated successfully")
else:
    st.warning("Please create a profile first")
    # create_inital_profile = st.button("Create Profile")
    st.text("Enter the roles that you want to apply for!!!")

    roles = show_roles_form()

    st.text("Enter the information about yourself!!!")
    profile_information = show_info_form()    