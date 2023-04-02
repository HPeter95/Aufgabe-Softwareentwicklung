from datetime import datetime

# Get the current time
now = datetime.now()

# Print the current time in ISO format
print(now.isoformat())

# Store the current time in a variable as a string
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(current_time)
