import threading
import time
import re
from datetime import timedelta
import Speak


def timer(duration):
    value = convert_time(duration)
    print(f"We have set your alarm for {value} seconds from now")
    print("Timer started.")
    time.sleep(value)
    print("Finish.")


def convert_time(duration):
    # Join the list of strings into a single string
    input_str = ' '.join(duration)

    # Use regular expressions to extract the hours, minutes and seconds from the input string
    pattern = r'(\d+)\s*(hour|minute|second)s?'
    matches = re.findall(pattern, input_str)

    # Map the units to the corresponding keyword arguments for the timedelta constructor
    unit_map = {'hour': 'hours', 'minute': 'minutes', 'second': 'seconds'}

    # Convert the hours, minutes and seconds to a timedelta object
    time_delta_args = {unit_map[unit]: int(value) for value, unit in matches}
    time_delta = timedelta(**time_delta_args)

    # Get the total number of seconds in the timedelta object
    total_seconds = time_delta.total_seconds()

    # Return the total number of seconds as an integer
    return int(total_seconds)

