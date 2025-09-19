import streamlit as st

def user_login():
    st.markdown("<h3>Login</h3>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "user" and password == "password":
            st.session_state["user_authenticated"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid credentials. Please try again.")

def user_register():
    st.markdown("<h3>Register</h3>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if password == confirm_password:
            st.session_state["user_authenticated"] = True
            st.success("Registration successful!")
        else:
            st.error("Passwords do not match.")
