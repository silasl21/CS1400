# Silas Loosli
# CS1400 - MWF 9:30

print("Welcome to the investment calculator! Please press enter to get started!")
input()

# - Get the user's initial investment
int_investment = float(input("Enter the initial investment amount in dollars: "))
# - Get the monthly investment
monthly_investment = float(input("Enter your monthly investment amount in dollars: "))
# - Get the yearly interest rate
year_interest_rate = float(input("Enter the annual interest rate as a percentage: "))
# - Get the number of years to calculate
num_years = int(input("Enter how many years you would like to calculate for: "))

# - Calculate monthly interest based off of yearly percentage
month_interest_rate = (year_interest_rate / 12) / 100
num_months = num_years * 12

# - calculate final value

future_value = (int_investment * (1 + month_interest_rate) ** num_months) + (monthly_investment * ((((1 + month_interest_rate) ** num_months) - 1) / month_interest_rate) * (1 + month_interest_rate))
future_value_rounded = round(future_value, 2)

print("In " + str(num_years) + " years, you will have $" + str(future_value_rounded) + " in your investment account")