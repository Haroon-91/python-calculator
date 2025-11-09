#!/usr/bin/env python3
#This is my updated version the old version is made by me and this version is polished by AI
"""
Simple CLI calculator and unit converter.
Refactored for input validation, modularity, and fixed conversion factors.
"""

import sys

SECRET_CODE = 6969400
DEV_PASSWORD = "777000777"  # keep as string to avoid float/int issues


def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            v = int(input(prompt).strip())
            if (min_val is not None and v < min_val) or (max_val is not None and v > max_val):
                print("Please enter a valid option.")
                continue
            return v
        except ValueError:
            print("Please enter a whole number.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a numeric value.")


def addition():
    a = get_float("Enter your first number for addition: ")
    b = get_float("Enter your second number: ")
    print(f"Result: {a + b}")


def subtraction():
    a = get_float("Enter a number for subtraction: ")
    b = get_float("Enter a second number for subtraction: ")
    print(f"Result: {a - b}")


def multiplication():
    a = get_float("Enter a number for multiplication: ")
    b = get_float("Enter second number for multiplication: ")
    print(f"Result: {a * b}")


def division():
    a = get_float("Enter a number to divide (numerator): ")
    b = get_float("Enter a number to divide by (denominator): ")
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {a / b}")


def secret_dev_menu():
    print("=== Secret Dev Menu ===")
    print("1. Easter egg")
    print("2. Help")
    print("3. Developer info")
    choice = get_int("Enter an option (1-3): ", 1, 3)
    pwd = input(f"You chose {choice}. Enter password to continue: ").strip()
    if pwd != DEV_PASSWORD:
        print("Incorrect password.")
        return
    if choice == 1:
        print("You found an easter egg — nothing much here yet. ;-)")
    elif choice == 2:
        print("Developer help: work in progress.")
    elif choice == 3:
        print("Made by Haroon")
        print("Built with VS Code")
        print("Created: November 2025")


def measurements_menu():
    while True:
        print("\nMeasurements")
        print("1. Length")
        print("2. Mass")
        print("3. Time")
        print("4. Temperature")
        print("5. Back to main menu")

        opt = get_int("Choose an option: ", 1, 5)
        if opt == 1:
            length_conversions()
        elif opt == 2:
            mass_conversions()
        elif opt == 3:
            time_conversions()
        elif opt == 4:
            temperature_conversions()
        else:
            break


def length_conversions():
    print("\nLength conversions")
    print("1. km -> m")
    print("2. m -> cm")
    print("3. cm -> mm")
    print("4. inch -> cm")
    print("5. foot -> inch")
    print("6. yard -> foot")
    print("7. mile -> km")
    choice = get_int("Pick an option from 1 to 7: ", 1, 7)

    if choice == 1:
        x = get_float("Kilometers: ")
        print(f"{x} km = {x * 1000} meters")
    elif choice == 2:
        x = get_float("Meters: ")
        print(f"{x} m = {x * 100} centimeters")
    elif choice == 3:
        x = get_float("Centimeters: ")
        print(f"{x} cm = {x * 10} millimeters")
    elif choice == 4:
        x = get_float("Inches: ")
        print(f"{x} in = {x * 2.54} centimeters")
    elif choice == 5:
        x = get_float("Feet: ")
        print(f"{x} ft = {x * 12} inches")
    elif choice == 6:
        x = get_float("Yards: ")
        print(f"{x} yd = {x * 3} feet")
    elif choice == 7:
        x = get_float("Miles: ")
        print(f"{x} mi = {x * 1.60934} kilometers")


def mass_conversions():
    print("\nMass conversions")
    print("1. kg -> g")
    print("2. g -> mg")
    print("3. lb -> kg")
    print("4. oz -> g")
    print("5. ton -> kg")
    choice = get_int("Select an option from 1-5: ", 1, 5)

    if choice == 1:
        x = get_float("Kilograms: ")
        print(f"{x} kg = {x * 1000} grams")
    elif choice == 2:
        x = get_float("Grams: ")
        print(f"{x} g = {x * 1000} milligrams")
    elif choice == 3:
        x = get_float("Pounds: ")
        print(f"{x} lb = {x * 0.45359237} kilograms")
    elif choice == 4:
        x = get_float("Ounces: ")
        print(f"{x} oz = {x * 28.349523125} grams")
    elif choice == 5:
        x = get_float("Tons: ")
        print(f"{x} t = {x * 1000} kilograms")


def time_conversions():
    print("\nTime conversions")
    print("1. hour -> minutes")
    print("2. minute -> seconds")
    print("3. days -> hours")
    print("4. weeks -> days")
    print("5. years -> days")
    choice = get_int("Enter an option from 1-5: ", 1, 5)

    if choice == 1:
        x = get_float("Hours: ")
        print(f"{x} hours = {x * 60} minutes")
    elif choice == 2:
        x = get_float("Minutes: ")
        print(f"{x} minutes = {x * 60} seconds")
    elif choice == 3:
        x = get_float("Days: ")
        print(f"{x} days = {x * 24} hours")
    elif choice == 4:
        x = get_float("Weeks: ")
        print(f"{x} weeks = {x * 7} days")
    elif choice == 5:
        x = get_float("Years: ")
        print(f"{x} years ≈ {x * 365} days (ignores leap years)")


def temperature_conversions():
    print("\nTemperature conversions")
    print("1. Celsius -> Fahrenheit")
    print("2. Fahrenheit -> Celsius")
    print("3. Celsius -> Kelvin")
    print("4. Kelvin -> Celsius")
    choice = get_int("Enter an option (1-4): ", 1, 4)

    if choice == 1:
        c = get_float("Celsius: ")
        print(f"{c} °C = {(c * 9/5) + 32} °F")
    elif choice == 2:
        f = get_float("Fahrenheit: ")
        print(f"{f} °F = {(f - 32) * 5/9} °C")
    elif choice == 3:
        c = get_float("Celsius: ")
        print(f"{c} °C = {c + 273.15} K")
    elif choice == 4:
        k = get_float("Kelvin: ")
        print(f"{k} K = {k - 273.15} °C")


def main():
    running = True
    while running:
        print("\n=== Calculator ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Divide")
        print("5. Measurements")
        print("6. Exit")

        # allow non-crashing input
        opt = None
        try:
            opt = get_int("Enter a number please: ", 1, 6)
        except KeyboardInterrupt:
            print("\nExiting.")
            sys.exit(0)

        if opt == SECRET_CODE:
            # unreachable because SECRET_CODE is huge; keeping the check for backward compatibility
            secret_dev_menu()
            continue

        if opt == 1:
            addition()
        elif opt == 2:
            subtraction()
        elif opt == 3:
            multiplication()
        elif opt == 4:
            division()
        elif opt == 5:
            measurements_menu()
        elif opt == 6:
            print("Exiting calculator... Goodbye!")
            running = False


if __name__ == "__main__":
    main()
