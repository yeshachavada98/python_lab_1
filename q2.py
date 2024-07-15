def calculate_simple_interest(P, T, R):
    # Calculate simple interest
    simple_interest = (P * T * R) / 100
    return simple_interest

# Input values
principal = float(input("Enter the principal amount (P): "))
time = float(input("Enter the time period in years (T): "))
rate = float(input("Enter the interest rate (R): "))

# Calculate and print simple interest
interest = calculate_simple_interest(principal, time, rate)
print(f"Simple Interest = {interest}")
