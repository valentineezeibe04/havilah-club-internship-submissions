# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, functions, and error handling.
# Submit this script with a working menu system.


# ── Function 1: Grade Calculator ─────────────────────────────────────────────
# Accepts a score (0-100) and returns the letter grade.
# A = 70-100, B = 60-69, C = 50-59, D = 40-49, F = below 40

def calculate_grade(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'


# ── Function 2: Multiplication Table ─────────────────────────────────────────
# Asks the user to enter a number and prints its full multiplication table (1-12).
# Repeats until the user types 'quit'.

def multiplication_table():
    print("\n--- Multiplication Table Utility ---")
    while True:
        user_input = input("Enter a number for the table (or type 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Exiting multiplication table.")
            break
        try:
            num = float(user_input)
            print(f"\nMultiplication Table for {num}:")
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")
            print()
        except ValueError:
            print("Invalid input! Please enter a valid number or 'quit'.\n")


# ── Function 3: Temperature Converter ────────────────────────────────────────
# Receives a temperature in Celsius as a parameter, converts it to Fahrenheit.

def convert_temperature():
    print("\n--- Temperature Converter ---")
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F\n")
    except ValueError:
        print("Invalid input! Please enter a valid numerical temperature.\n")


# ── Main Menu ─────────────────────────────────────────────────────────────────
# Display a simple menu so the user can pick which function to run.
# Include try/except to handle invalid input.

def main():
    while True:
        print("==============================")
        print("   PYTHON UTILITY MENU        ")
        print("==============================")
        print("1. Grade Calculator")
        print("2. Multiplication Table")
        print("3. Temperature Converter")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            try:
                score = float(input("\nEnter student score (0-100): "))
                if 0 <= score <= 100:
                    grade = calculate_grade(score)
                    print(f"The grade for a score of {score} is: {grade}\n")
                else:
                    print("Score must be between 0 and 100.\n")
            except ValueError:
                print("Invalid input! Please enter a numerical score.\n")
                
        elif choice == '2':
            multiplication_table()
            
        elif choice == '3':
            convert_temperature()
            
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option! Please choose between 1 and 4.\n")


if __name__ == "__main__":
    main()