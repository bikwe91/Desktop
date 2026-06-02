# Define the function computepay
def computepay(hours, rate):
    """
    Compute the total pay based on hours worked and hourly rate.
    Overtime (hours over 40) should be paid at 1.5 times the hourly rate.
    """
    if hours > 40:
        overtime_hours = hours - 40
        # TODO: Calculate total pay with overtime correctly
        total_pay = (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        # TODO: Calculate total pay for regular hours
        total_pay = hours * rate  # Placeholder, students need to ensure this is correct

    return total_pay  # Ensure the function returns the correct pay

# Prompt the user to enter hours and rate
try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    # TODO: Call the computepay function with correct arguments
    pay = computepay(hours, rate)  # Placeholder, students need to ensure correct function call

    # TODO: Print the correct pay result
    print("Pay:", pay)  # Placeholder, students need to ensure correct output

except ValueError:
    print("Error: Please enter numeric values for hours and rate.")