# Day 11 — Introduction to Python

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables representing information about a student or engineer. 
# Include at least one string, one integer, one float, and one boolean. 
# Print each value with a descriptive label and use type() to display its data type.

engineer_name = "Valentine Ezeibe"  # String
age = 22                          # Integer
experience_years = 1.5            # Float
is_employed = True                # Boolean

print("--- Exercise 1: Variables and Data Types ---")
print("Name:", engineer_name, "| Type:", type(engineer_name))
print("Age:", age, "| Type:", type(age))
print("Experience (Years):", experience_years, "| Type:", type(experience_years))
print("Is Employed:", is_employed, "| Type:", type(is_employed))
print()


# ── Exercise 2: Basic Arithmetic Calculator ──────────────────────────────────
# Ask the user to enter two numbers. Convert the inputs and display the sum, 
# difference, product, quotient, and remainder.

print("--- Exercise 2: Basic Arithmetic ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum ({num1} + {num2}): {num1 + num2}")
print(f"Difference ({num1} - {num2}): {num1 - num2}")
print(f"Product ({num1} * {num2}): {num1 * num2}")
if num2 != 0:
    print(f"Quotient ({num1} / {num2}): {num1 / num2}")
    print(f"Remainder ({num1} % {num2}): {num1 % num2}")
else:
    print("Quotient & Remainder: Division by zero is undefined.")
print()


# ── Exercise 3: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius and convert it to Fahrenheit. 
# Then ask for a temperature in Fahrenheit and convert it to Kelvin.

print("--- Exercise 3: Temperature Converter ---")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit_from_c = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit_from_c:.2f}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
kelvin_output = (fahrenheit_input - 32) * 5/9 + 273.15
print(f"{fahrenheit_input}°F is equal to {kelvin_output:.2f}K")
print()


# ── Exercise 4: Robot Sensor Monitor ─────────────────────────────────────────
# Simulate data collection from a robot sensor: Robot Name, Robot ID, Sensor Name, 
# Sensor Reading, and Operating Limit. Calculate the difference between the 
# operating limit and the current sensor reading.

print("--- Exercise 4: Robot Sensor Monitor ---")
robot_name = input("Enter Robot Name: ")
robot_id = input("Enter Robot ID: ")
sensor_name = input("Enter Sensor Name: ")
sensor_reading = float(input("Enter current Sensor Reading: "))
operating_limit = float(input("Enter Operating Limit: "))

reading_difference = operating_limit - sensor_reading

print("\n=== Robot Sensor Report ===")
print(f"Robot Name: {robot_name} (ID: {robot_id})")
print(f"Sensor Monitored: {sensor_name}")
print(f"Current Reading: {sensor_reading}")
print(f"Operating Limit: {operating_limit}")
print(f"Margin from Limit: {reading_difference}")