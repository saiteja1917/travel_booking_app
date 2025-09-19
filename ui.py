import streamlit as st

def set_custom_css():
    st.markdown("""
        <style>
            body {
                background-color: #f9f9f9;
            }
            .title-box {
                background-color: #87CEEB;
                color: white;
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .stTextInput > div > div > input, .stDateInput > div > div > input, .stNumberInput > div > div > input {
                border-radius: 10px;
                border: 2px solid #ccc;
                padding: 10px;
            }
            .stButton > button {
                background-color: #1a73e8;
                color: white;
                border-radius: 8px;
                padding: 10px 15px;
                font-weight: bold;
                border: none;
            }
            .stButton > button:hover {
                background-color: #1559c7;
            }
            .search-section {
                margin: 0 auto;
                max-width: 600px;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }
        </style>
    """, unsafe_allow_html=True)

def show_available_bookings(cursor):
    st.markdown('<div class="search-section">', unsafe_allow_html=True)
    st.subheader("Available Bookings")

    cursor.execute("SELECT DISTINCT city_name FROM Cities")
    cities = [row[0] for row in cursor.fetchall()]

    st.write("### Available Cities:")
    for city in cities:
        st.write(f"- {city}")
    
    cursor.execute("SELECT hotel_name, city FROM Hotels")
    hotels = cursor.fetchall()

    st.write("### Available Hotels:")
    for hotel in hotels:
        st.write(f"- {hotel[0]} in {hotel[1]}")

    st.markdown('</div>', unsafe_allow_html=True)
