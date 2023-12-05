# Take input of the principal amount borrowed
# Annual interest rate and the years and tell you how much you can pay
# you can pay until you finish paying your loan

"""
1: Collect the necessary inputs: principal, apr,years
2: Calculate the monthly payment
3: Show to the user
"""


# create a signature function
def main():
    print("This is a monthly loan calculator ")
    print("")

    while True:
        principal = float(input("input the loan amount: "))
        apr = float(input("Input the annual interest rate: "))
        years = int(input("Input the amount of years: "))

        monthly_interest_rate = apr / 1200
        number_of_months = years * 12
        monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) **(-number_of_months))

        print(" The monthly payment for this loan is: $%.2f " % monthly_payment)
main()

