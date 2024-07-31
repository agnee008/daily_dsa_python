def find_last_round_trip(trips, a2b, b2a):
    # Initialize current time and trips completed
    current_time = 0
    trips_completed = 0
    
    while trips_completed < trips:
        # Find the next flight from A to B that departs after or at current_time
        for departure in a2b:
            if departure >= current_time:
                current_time = departure + 100  # Time to reach B
                break
                
        # Find the next flight from B to A that departs after reaching B
        for departure in b2a:
            if departure >= current_time:
                current_time = departure + 100  # Time to reach A
                break
        
        # Increment the number of trips completed
        trips_completed += 1
    
    return current_time

# Example input
a2b = [99, 210, 320]
b2a = [120, 230, 340]
trips = 2

# Call the function with the example input
print(find_last_round_trip(trips, a2b, b2a))  # Output should be the time in minutes when the last round trip is finished
