

import datetime


def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")

display_current_datetime()


take_input = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    future_date = datetime.datetime.now() + datetime.timedelta(days=take_input)
    format = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {format}")

calculate_future_date()