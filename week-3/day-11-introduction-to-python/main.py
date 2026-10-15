# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

name = "Valentine"          # String
age = 22                    # Integer
height = 5.9                # Float
is_intern = True            # Boolean

print("--- Exercise 1: Variables and Data Types ---")
print("Name (String):", name)
print("Age (Integer):", age)
print("Height (Float):", height)
print("Is Intern (Boolean):", is_intern)
print()


# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

print("--- Exercise 2: Temperature Converter ---")
celsius_input = float(input("Enter temperature in Celsius: "))
fahrenheit_output = (celsius_input * 9/5) + 32
print(f"{celsius_input}°C is equal to {fahrenheit_output}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_output = (fahrenheit_input - 32) * 5/9
print(f"{fahrenheit_input}°F is equal to {celsius_output:.2f}°C")
print()


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

print("--- Exercise 3: Age Calculator ---")
user_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year (e.g., 2000): "))

# Assuming current year is 2026
current_year = 2026
current_age = current_year - birth_year
year_turning_30 = birth_year + 30

print(f"Hello {user_name}, you are currently {current_age} years old.")
print(f"You will turn 30 years old in the year {year_turning_30}.")