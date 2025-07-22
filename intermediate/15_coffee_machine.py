# Coffee Machine Program
# This program simulates a coffee machine that can make different types of coffee drinks.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Check resources sufficient?
def check_resources(drink):
    """ check if there are enough resources to make the selected drink """
    is_sufficient = True
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_sufficient = False
    return is_sufficient

# Process coins.
def process_coins():
    """ Calculate the monetary value of the coins inserted. 
    E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52 """
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    # Calculate the total value of the coins.          
    quarters_value = 0.25 
    dimes_value = 0.10
    nickles_value = 0.05 
    pennies_value = 0.01
    total_money = quarters_value * quarters + dimes_value * dimes + nickles_value * nickles + pennies_value * pennies
    return total_money

# Check transaction successful?
def is_transaction_successful(money_received, drink_cost):
    """ 
    Check that the user has inserted enough money to purchase the drink they selected.
        - If the user has inserted enough money, then the cost of the drink gets added to the machine 
            as the profit and this will be reflected the next time “report” is triggered.
        - If the user has not inserted enough money, then the machine will return the coins and
            prompt the user to insert more coins.
        - If the user has inserted too much money, the machine should offer change.
    """
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = money_received - drink_cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")   
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

# Make Coffee
def make_coffee(drink):
    """ 
    If the transaction is successful and there are enough resources to make the drink the user selected, 
    then the ingredients to make the drink should be deducted from the coffee machine resources. 
    """
    if is_transaction_successful and check_resources(drink):
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        if "milk" in MENU[drink]["ingredients"]:
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        print(f"Here is your {drink}. Enjoy!")

# Print report.
def print_report():
    """ Print the current resources and profit of the coffee machine. """
    print("Current resources:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit:.2f}")

# Final Program Function
def coffee_machine():
    """ Run the Coffee Machine Program.
        - Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        - If the user enters "off", then the program should terminate.
        - If the user enters "report", then the program should print a report of the current resources and profit.
        - If the user enters a valid drink choice, then the program should check if there are enough resources to make that drink.
        - If there are enough resources, then the program should prompt the user to insert coins and process the payment.
        - If the payment is successful, then the program should make the drink and deduct the ingredients from the resources.
        - If there are not enough resources, then the program should print a message indicating that there are not enough resources. 
    """
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print_report()
        elif choice in MENU:
            if check_resources(choice):
                print(f"Please insert coins for {choice}.")
                money_received = process_coins()
                if is_transaction_successful(money_received, MENU[choice]["cost"]):
                    make_coffee(choice)
        else:
            print("Invalid choice. Please try again.")

coffee_machine()