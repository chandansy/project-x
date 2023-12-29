import os
import streamlit as st


def check_folder_exists(folder_path):
    return os.path.exists(folder_path) and os.path.isdir(folder_path)


def chech_file_exists(file_path):
    return os.path.exists(file_path) and os.path.isfile(file_path)


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






def show_roles_form():
    try:
        with st.form("roles_form"):
            
            if check_folder_exists("new_profiles"):
                with open("new_profiles/roles.txt", "r") as f:
                    roles = f.readlines()
                    old_role1 = roles[0]
                    old_role2 = roles[1]
                    old_role3 = roles[2]
                    f.close()

                role1 = st.text_input("Role 1", value=old_role1)
                role2 = st.text_input("Role 2", value=old_role2)
                role3 = st.text_input("Role 3", value=old_role3)

            else:
                role1 = st.text_input("Role 1")
                role2 = st.text_input("Role 2")
                role3 = st.text_input("Role 3")
            
            save_roles_info = st.form_submit_button(label="Save Roles")
            
            roles_list = [role1, role2, role3]

            # Checking if all the fields are non empty
            if save_roles_info:
                st.write(save_roles_info)
                
                if check_folder_exists("new_profiles"):
                    with open("new_profiles/roles.txt", "w") as f:
                        for role in roles_list:
                            f.write(role + "\n")
                        f.close()
                else:
                    os.makedirs("new_profiles")
                    with open("new_profiles/roles.txt", "w") as f:
                        for role in roles_list:
                            f.write(role + "\n")
                        f.close()



                if role1 or role2 or role3:
                    # add_user_info(id, name, age, email, phone, gender)

                    st.success("You will be applying for \n  "+role1 + ",\n" + role2 + ",\n " + role3 +" roles")
                else:
                    st.warning("Please fill all the fields")
    except Exception as e:
        st.error(e)
        st.error("Something went wrong. Please try again later")



def show_info_form():
    with st.form("Pofile information"):
        st.subheader("Fill out the form")

        # Add form fields using st.text_input, st.selectbox, etc.
        name = st.text_input("Name")
        year_of_experience = st.text_input("Year of experience")
        education = st.selectbox("Education", ["Bachelor's", "Master's", "PhD"])
        education_domain = st.text_input("Education domain/Certifications")
        github_link = st.text_input("Github link")
        project1 = st.text_area("Project 1")
        project2 = st.text_area("Project 2")
        skills = st.text_input("Skills (comma separated)")
        save_profile_data = st.form_submit_button(label="Save Profile")

        if save_profile_data:
            if check_folder_exists("new_profiles"):
                with open("new_profiles/profile.txt", "w") as f:
                    f.write("name : " + name + "\n")
                    f.write("year of experience : " + year_of_experience + "\n")
                    f.write("education : " + education + "\n")
                    f.write("education domain/certifications : " +education_domain + "\n")
                    f.write("github Link : " + github_link + "\n")
                    f.write("project 1 : " + project1 + "\n")
                    f.write("project 2 : " + project2 + "\n")
                    f.write("skills : " + skills + "\n")
                    f.close()
            else:
                os.makedirs("new_profiles")
                with open("new_profiles/profile.txt", "w") as f:
                    f.write("name : " + name + "\n")
                    f.write("year of experience : " + year_of_experience + "\n")
                    f.write("education : " + education + "\n")
                    f.write("education domain/certifications : " +education_domain + "\n")
                    f.write("github Link : " + github_link + "\n")
                    f.write("project 1 : " + project1 + "\n")
                    f.write("project 2 : " + project2 + "\n")
                    f.write("skills : " + skills + "\n")
                    f.close()



        # Display the submitted form values
