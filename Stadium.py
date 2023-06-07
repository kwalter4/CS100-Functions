def main():
# Describe the Program to the user
# This program will calculate the ticket price by how many seats available, then return that total price.

    # How much each ticket costs
    print("Class A tickets cost $20.00 ea, Class B tickets cost $15.00 ea; Class C tickets cost $10.00 ea")

    # Get User Input
    class_a = (input("Class A qty: "))
    class_b = (input("Class B qty: "))
    class_c = (input("Class C qty: "))

    #Define Seats
    # seats = [input_a, input_b, input_c]

    cost_a = class_a_value(class_a)
    cost_b = class_b_value(class_b)
    cost_c = class_c_value(class_c)
    final_cost = cost_a + cost_b + cost_c

    #Output the final cost to the user
    print(f"Total income generated from ticket sales is ${final_cost}")
    return final_cost

# Class A Ticket Function
def class_a_value(class_a):
    value = int(class_a)
    cost = value * 20
    return cost

# Class B Ticket Function
def class_b_value(class_b):
    value = int(class_b)
    cost = value * 15
    return cost

# Class C Ticket Function
def class_c_value(class_c):
    value = int(class_c)
    cost = value * 10
    return cost

if __name__ == '__main__':
    main()