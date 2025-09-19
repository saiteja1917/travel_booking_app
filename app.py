import streamlit as st
import pandas as pd
from database import init_database, save_to_database
from utils import is_valid_email, save_to_csv
from auth import user_login, user_register
from ui import show_available_bookings, set_custom_css

def main():
    if "user_authenticated" not in st.session_state:
        st.session_state["user_authenticated"] = False

    conn, cursor = init_database()

    # CSS + Title
    set_custom_css()
    st.markdown('<div class="title-box">Travel Booking System</div>', unsafe_allow_html=True)

    # Sidebar Menu
    menu = ["Login/Register", "Search & Book", "Admin Panel"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Login/Register
    if choice == "Login/Register":
        if not st.session_state["user_authenticated"]:
            auth_choice = st.radio("Select Action", ["Login", "Register"])
            if auth_choice == "Login":
                user_login()
            elif auth_choice == "Register":
                user_register()
        else:
            st.success("You are logged in!")
            show_available_bookings(cursor)

    # Search & Book
    elif choice == "Search & Book":
        if st.session_state["user_authenticated"]:
            st.markdown('<div class="search-section">', unsafe_allow_html=True)
            st.subheader("Search and Book")

            booking_type = st.selectbox("Booking Type", ["Train", "Bus", "Hotel", "Flight"], index=0)

            col1, col2 = st.columns(2)
            departure = col1.text_input("From")
            arrival = col2.text_input("To" if booking_type != "Hotel" else "Location")
            
            col3, col4 = st.columns(2)
            travel_date = col3.date_input("Travel Date")
            passengers = col4.number_input("Passengers", min_value=1, max_value=10, step=1)

            st.markdown("### Personal Details")
            full_name = st.text_input("Full Name")
            email = st.text_input("Email Address")

            payment_status = st.selectbox("Payment Status", ["Pending", "Completed"])

            if st.button("Book Now"):
                if departure and (arrival or booking_type == "Hotel") and full_name and email:
                    if not is_valid_email(email):
                        st.error("Invalid email format.")
                    else:
                        data = (booking_type, departure, arrival, travel_date, passengers, full_name, email, payment_status)
                        save_to_database(cursor, conn, data)
                        save_to_csv([data])
                        st.success(f"Your {booking_type} booking from {departure} to {arrival} is confirmed!")
                else:
                    st.error("Please fill in all required fields.")

            st.markdown('</div>', unsafe_allow_html=True)

    # Admin Panel
    elif choice == "Admin Panel":
        st.subheader("Admin Panel: View All Bookings")
        cursor.execute("SELECT * FROM Bookings")
        bookings = cursor.fetchall()
        if bookings:
            df = pd.DataFrame(bookings, columns=["ID", "Type", "From", "To", "Date", "Passengers", "Name", "Email", "Payment"])
            st.dataframe(df)
        else:
            st.write("No bookings available.")

if __name__ == "__main__":
    main()
