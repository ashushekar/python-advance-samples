"""
Vendor machine problem
"""

# This will be the money used to purchase the snacks
money = 10.00
vending_machine = {"Chips": "0A", "Soda": "0B", "Chocolate": "0C", "Fruit Snacks": "0D"}
prices = {"Chips": "$0.75", "Soda": "$0.50", "Chocolate": "$1.25", "Fruit Snacks": "$.25"}


# Debug functions
def set_money(amount):
    """
    This function is used to set money
    """
    global money
    money = amount


def get_stock():
    """
    To keep track of number of stocks
    """
    stock = vending_machine.values()
    i = 0
    for amount in stock:
        i += amount
    print(i)


def purchase(needed_money):
    global money
    if money > needed_money:
        money -= needed_money
        print("Item vended")
    else:
        print("Not enough balance")


def transaction(user_input):
    global money
    if user_input == '0A':
        purchase(0.75)
    elif user_input == '0B':
        purchase(0.50)
    elif user_input == '0D':
        purchase(0.25)
    elif user_input == '0C':
        purchase(1.25)
    else:
        print("Invalid Input")


def main():
    item_list = []
    switch = 1
    while switch == 1:
        print("Welcome to the Vending Machine program.")  # Welcome Messages
        print("Here are your selections!")
        for item, selection in vending_machine.items():
            item_list.append((item, selection))
        print(item_list[::-1])

        print()
        print("Here are the prices")
        for item, price in prices.items():  # Prints the items and their prices on separate lines.
            print(item, price)

        print()

        user_switch = 1
        while user_switch == 1:
            print("You currently have $" + str(money))
            user_input = input("Input your selection: ").upper()
            transaction(user_input)
            print()
            choice = 1
            while choice == 1:
                user_input = input("Are you finished with the vending?(y/n): ").lower()
                if user_input == 'y':
                    user_switch = 0
                    switch = 0
                    choice = 0
                elif user_input == 'n':
                    user_switch = 1
                    choice = 0
                else:
                    print("Invalid command")
                    choice = 1
main()