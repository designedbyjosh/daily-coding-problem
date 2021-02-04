def calculateRooms(intervals):
    # Store the bookings at each time 
    bookings = {}
    # Create the entry and exit values, and if there are duplicates, add another to that time interval
    for interval in intervals:
        bookings[interval[0]] = bookings[interval[0]] + 1 if interval[0] in intervals else 1 
        bookings[interval[1]] = bookings[interval[1]] - 1 if interval[1] in intervals else -1 
    # Arrange time in order so we can progress through time and watch the event
    time = sorted(bookings.items())
    # Store the rooms required (return value)
    required = 0
    # Store the rooms being used at this time interval
    rooms = 0
    # Loop through each time interval
    for time, event in time:
        # Add the entry/exit value for movement 
        rooms += event
        # If the rooms exceeds the required number at any one time, assign it
        if rooms > required: required = rooms      
    return required