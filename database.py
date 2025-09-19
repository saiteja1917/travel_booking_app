import sqlite3
import streamlit as st

def init_database():
    try:
        conn = sqlite3.connect("SBook.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                booking_type TEXT,
                departure TEXT,
                arrival TEXT,
                travel_date TEXT,
                passengers INTEGER,
                full_name TEXT,
                email TEXT,
                payment_status TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city_name TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Hotels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hotel_name TEXT,
                city TEXT
            )
        """)

        # Seed Cities
        cursor.execute("SELECT COUNT(*) FROM Cities")
        if cursor.fetchone()[0] == 0:
            cities = ['Hyderabad', 'Vizag', 'Bangalore', 'Chennai', 'Mumbai', 'Delhi']
            for city in cities:
                cursor.execute("INSERT INTO Cities (city_name) VALUES (?)", (city,))

        # Seed Hotels
        cursor.execute("SELECT COUNT(*) FROM Hotels")
        if cursor.fetchone()[0] == 0:
            hotels = [
                ('Taj Hotel', 'Hyderabad'),
                ('The Park', 'Vizag'),
                ('ITC Gardenia', 'Bangalore'),
                ('The Leela Palace', 'Chennai'),
                ('The Oberoi', 'Mumbai'),
                ('The Imperial', 'Delhi')
            ]
            for hotel in hotels:
                cursor.execute("INSERT INTO Hotels (hotel_name, city) VALUES (?, ?)", hotel)

        conn.commit()
        return conn, cursor
    except Exception as e:
        st.error(f"Error initializing the database: {e}")
        return None, None

def save_to_database(cursor, conn, data):
    try:
        cursor.execute("""
            INSERT INTO Bookings (booking_type, departure, arrival, travel_date, passengers, full_name, email, payment_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        st.success("Booking saved to the database successfully!")
    except Exception as e:
        st.error(f"Error saving booking to the database: {e}")
