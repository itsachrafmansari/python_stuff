import time as t

chosen_time = "21:27"  # In 24H format e.g. 23:15

h = int(chosen_time.split(":")[0])  # Chosen hour
m = int(chosen_time.split(":")[1])  # Chosen minutes

while True:

    lh = t.localtime().tm_hour  # Check the local hour
    lm = t.localtime().tm_min  # Check the local minutes

    # Check if the local time equals the chosen time
    if h == lh and m == lm:
        # YOUR CODE HERE
        t.sleep(60)

    t.sleep(1)  # Wait a second before checking again
