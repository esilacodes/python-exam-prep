# Scenario 1: Smart City Parking System (Dictionary & Functions)
# Task: Create a parking management system. 
# Calculate the fee based on the duration (20 TL per hour).

parked_cars = {
    "34ABC123": 10,  # License Plate: Entry Time
    "06DEF456": 14,
    "35GHI789": 16
}

def calculate_fee(plate, exit_time):
    # Getting entry time using .get() to prevent crashes
    entry_time = parked_cars.get(plate)
    
    # Check if the car exists in the systemm
    if entry_time is None:
        return f"Error: Vehicle with plate {plate} is not registered in the system."
    
    # Calculate the duration
    duration = exit_time - entry_time
    
    # Logic check: Exit cannot be before entry
    if duration < 0:
        return "Error: Exit time cannot be earlier than entry time!"
    
    # Fee calculation (20 TL per hour)
    total_fee = duration * 20
    
    return f"Vehicle: {plate} | Duration: {duration} hours | Total Fee: {total_fee} TL"

# Test cases
print(calculate_fee("35GHI789", 19)) # Successful calculation (3 hours)
print(calculate_fee("34ABC123", 8))  # Should trigger exit time error
print(calculate_fee("10XYZ010", 20)) # Should trigger "not registered" error