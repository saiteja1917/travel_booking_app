import re
import os
import pandas as pd

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def save_to_csv(data):
    filename = "bookings.csv"
    df = pd.DataFrame(data, columns=["Type", "From", "To", "Date", "Passengers", "Name", "Email", "Payment"])
    if not os.path.isfile(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)
