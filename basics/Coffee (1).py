# Bohdana Vasylyshena
# This program will be able to calculate how much money you can save if you make coffee at home instead of buying it at the cafe, let's say one caffee every day except weekends. 
print("Bohdana Vasylyshena")
print("Part 2: Coffee Shop Savings")
print("This program will be able to calculate how much money you can save if you make coffee at home instead of buying it at the cafe, let's say one caffee every day except weekends.")


# Constants
COFFEE_SHOP_COST = 4.75   # Cost of one coffee in shop
COFFEE_HOME_COST = 0.85   # Cost of one coffee at home
COFFEE_DRINKS_DAYS_PER_YEAR = 260       # Number of coffee drinks per year

# Total costs
total_shop_cost = COFFEE_SHOP_COST * COFFEE_DRINKS_DAYS_PER_YEAR   # Cost at shop per year
total_home_cost = COFFEE_HOME_COST * COFFEE_DRINKS_DAYS_PER_YEAR   # Cost at home per year
total_savings = total_shop_cost - total_home_cost    # Savings per year

# Output 
print(f"Buying coffee at the cafe for one year will cost you: ${total_shop_cost:,.2f}")
print(f"Making coffee at home for one year will cost you: ${total_home_cost:,.2f}")
print(f"You can save that amount of money: ${total_savings:,.2f} by making your coffee at home.")
