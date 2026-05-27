
import math

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

#Request input from user
menu = input("Please choose either investment or bond: ").lower()

#The if-elif-else statements will output the calculation based off if the user chose their type of interest
if menu == "investment":
    deposit = float(input("How much money would you like to deposit? "))
    print()
    interest= float(input("Please enter the interest rate you would like to have: "))
    print()
    years = int(input("Please input the number of years you plan on investing: "))
    print()

    type_of_interest = input("Please enter if you are interested in a 'simple' or 'compound' interest: ").lower()

    rate_of_interest = interest / 100

    if type_of_interest == "simple":
        simple_interest = deposit * (1 + rate_of_interest * years)
        print("This is your simple interest amount: ", simple_interest)

    elif type_of_interest == "compound":
        compound_interest = deposit * math.pow((1 + rate_of_interest), years)
        print("This is your compound interest amount: ", round(compound_interest,2))
#If user input is incorrect, requested again
    else:
        print("Please enter a valid interest type")

elif menu == "bond":
    house_value = float(input("Please enter the present value of your house: "))
    print()
    interest_rate = float(input("Please enter the interest rate you would like to have: "))
    print()
    months = int(input("Please input the number of months you plan to repay the bond: "))
    print()

    monthly_interest_rate = (interest_rate / 100) / 12

    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** ( -months))
    print("This is your monthly repayment: ", round(repayment,2))
#If user input is incorrect, requested again
else:
    print("Please enter either investment or bond.")


