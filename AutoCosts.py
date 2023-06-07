# The purpose of this program is to give the user their total monthly and yearly expense bill

# First we will get user input
def main():

    loan_payments = float(input("How much is the loan payment?: "))
    insurance = float(input("How much is the monthly insurance?: "))
    gas = float(input("How much is the monthly gas bill?: "))
    oil = float(input("How much is the monthly average oil change cost?: "))
    tires = float(input("How much is the monthly average tire replacement cost?: "))
    maintenance = float(input("How much is the monthly average maintenance cost?: "))

# Call the functions from main
    calculate_in_months = monthly_cost(loan_payments, insurance, gas, oil, tires, maintenance)
    calculate_in_year = yearly_cost(loan_payments, insurance, gas, oil, tires, maintenance)

# Return User Output
    print("Costs: ")
    print("Monthly: ", calculate_in_months)
    print("Yearly: ", calculate_in_year)

# Create a function for total monthly cost
def monthly_cost(loan_payment, insurance, gas, oil, tires, maintenance):

    total_in_months = loan_payment + insurance + gas + oil + tires + maintenance

    return total_in_months

# Create a function for total yearly cost
def yearly_cost(loan_payment, insurance, gas, oil, tires, maintenance):

    total_in_year = (loan_payment + insurance + gas + oil + tires + maintenance) * 12

    return total_in_year

if __name__ == '__main__':
    main()