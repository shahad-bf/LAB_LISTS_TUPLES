# List of initially booked seats
booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

# Function to display all booked seats
def display_booked_seats():
    print("\nBooked Seats:")
    for seat in booked_seats:
        print(f"Row {seat[0]}, Seat {seat[1]}")

# Function to check if a seat is available
def check_availability():
    row = int(input("Enter row number (1-10): "))
    seat = int(input("Enter seat number (1-20): "))
    if (row, seat) in booked_seats:
        print("This seat is already booked.")
    else:
        print("This seat is available.")

# Function to add a booking
def add_booking():
    row = int(input("Enter row number (1-10): "))
    seat = int(input("Enter seat number (1-20): "))
    if (row, seat) in booked_seats:
        print("This seat is already booked.")
    else:
        booked_seats.append((row, seat))
        print("Booking added successfully.")

# Function to cancel a booking
def cancel_booking():
    row = int(input("Enter row number to cancel: "))
    seat = int(input("Enter seat number to cancel: "))
    if (row, seat) in booked_seats:
        booked_seats.remove((row, seat))
        print("Booking cancelled.")
    else:
        print("This seat is not booked.")

# Function to show all booked seats sorted by row and seat
def sorted_bookings():
    print("\nSorted Booked Seats:")
    for seat in sorted(booked_seats):
        print(f"Row {seat[0]}, Seat {seat[1]}")

# Function to show booking summary
def booking_summary():
    total = len(booked_seats)
    print(f"\nTotal booked seats: {total}")
    row_counts = [0] * 10
    for row, seat in booked_seats:
        row_counts[row - 1] += 1
    for i in range(10):
        print(f"Row {i + 1}: {row_counts[i]} seats booked")

# Main menu
while True:
    print("""
Cinema Booking System
1. Display all booked seats
2. Check seat availability
3. Add a booking
4. Cancel a booking
5. Show sorted booked seats
6. Booking summary
Type 'exit' to quit
""")

    choice = input("Choose an option: ").strip()

    match choice:
        case "1":
            display_booked_seats()
        case "2":
            check_availability()
        case "3":
            add_booking()
        case "4":
            cancel_booking()
        case "5":
            sorted_bookings()
        case "6":
            booking_summary()
        case "exit" | "Exit":
            print("Goodbye!")
            break
        case _:
            print("Invalid option. Please try again.")
