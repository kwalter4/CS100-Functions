
def main():
    # This program will have the user input a number. Then it will tell the user whether that number is positive or negative.

    # Get a number from the user
    value = int(input("Input a number: "))

    # Evaluate whether the number is positive or negative.
    result = isPositive(value)

    # Output the results
    result = value
    if result >= 0:
        print(f"The number {value} is positive")
    else:
        print(f"The number {value} is negative")

def isPositive(value):
    """Tests to see if value is Positive"""
    pass


if __name__ == '__main__':
    main()