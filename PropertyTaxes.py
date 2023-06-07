def main():
# The purpose of this program is to find the assesment value and property tax given the price of the property
# First get user input
    property_value = float(input("What is the property value?: "))
    input_value, property_tax = assesment(property_value)

# Output the information to the user
    print(f"The tax on a property with the assessed valued of ${input_value:.2f} is ${property_tax:.2f}")

# Create a function of assesment
def assesment(property_value):
    input_value = (property_value * 0.6)
    property_tax = (input_value / 100) * 0.72
    return input_value, property_tax


if __name__ == '__main__':
    main()