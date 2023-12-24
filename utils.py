import os
import streamlit as st


def check_folder_exists(folder_path):
    return os.path.exists(folder_path) and os.path.isdir(folder_path)



def show_form():
    st.subheader("Fill out the form")

    # Add form fields using st.text_input, st.selectbox, etc.
    name = st.text_input("Name")
    email = st.text_input("Email")
    applying_role = st.text_input("Applying for")
    year_of_experience = st.text_input("Year of experience")
    education = st.selectbox("Education", ["Bachelor's", "Master's", "PhD"])
    education_domain = st.text_input("Education domain")
    github_link = st.text_input("Github link")
    projects = st.text_area("Project 1")
    projects = st.text_area("Project 2")
    skills = st.text_input("Skills (comma separated)")



    # Display the submitted form values
    if st.button("Submit"):
        st.success(f"Form submitted:\nName: {name}\nEmail: {email}\nAge: {age}\nGender: {gender}")


def show_edit_profile_form(DATA_DIR):
    st.subheader("Edit Profile")

    # Check if a profile file exists
    profile_file_path = os.path.join(DATA_DIR, "profile.txt")
    if os.path.exists(profile_file_path):
        # Read data from the profile file
        with open(profile_file_path, "r") as file:
            profile_data = file.read().splitlines()

        # Pre-fill form fields with existing data
        name = st.text_input("Name", value=profile_data[0])
        email = st.text_input("Email", value=profile_data[1])
        age = st.number_input("Age", min_value=0, max_value=100, value=int(profile_data[2]))
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(profile_data[3]))

        if st.button("Save Changes"):
            save_profile_data(name, email, age, gender)
            st.success("Profile updated successfully!")
    else:
        st.warning("No profile data found. Please add a profile first.")




def save_profile_data(DATA_DIR, file_name, name, email, age, gender):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    profile_data = [name, email, str(age), gender]
    profile_file_path = os.path.join(DATA_DIR, file_name)

    with open(profile_file_path, "w") as file:
        file.write("\n".join(profile_data))