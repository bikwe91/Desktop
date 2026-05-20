# Exercise 1
print("Exercise 1")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " +last_name  # Error: Missing space between first and last name
print("Hello " + full_name + "\n")  # Error: Incorrect variable name (should be full_name)

# Exercise 2: Lawn and Garden Service Payment Calculator
print("Exercise 2: Lawn and Garden Service Payment Calculator")
print("Welcome to the Lawn and Garden Service Payment Calculator!")
print("This tool helps you calculate the payment for your gardening services.")

# Get service details
service_hours = float(input("Enter the total hours spent on lawn care and gardening: "))  # Error: input() returns a string
hourly_rate = float(input("Enter the hourly rate for the service in dollars: "))

# Calculate total payment
total_payment = service_hours * hourly_rate  # Error: service_hours is a string, needs to be converted to float
rounded_payment = round(total_payment, 2)

# Display results
print("\nPayment Summary:")
print(f"Total hours worked: {service_hours}")  # Error: service_hours should be converted to float for calculations
print(f"Hourly rate: ${hourly_rate}")  # Error: Incorrect variable name (should be hourly_rate)
print(f"Total payment due: ${rounded_payment}")

# Exercise 3: Planning a Garden Plot
print("Exercise 3: Planning a Garden Plot")

# Garden dimensions
garden_width = float(input("Enter width in feet: "))  # ft
garden_length = float(input("Enter length in feet: "))  # Error: input() returns a string, needs to be converted to float

# Calculations for garden planning
garden_square_footage = garden_width * garden_length  # Error: Multiplying float with string
half_width_exact = garden_width / 2.0  # Error: Floor division used instead of normal division

print(f"\nGarden Planning Results:")
print(f"Garden square footage: {garden_square_footage}")
print(f"Exact half-width: {half_width_exact} ft")