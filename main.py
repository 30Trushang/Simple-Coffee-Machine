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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money= 0

def report_machine():
    print("Water:", resources["water"])
    print("Milk:", resources["milk"])
    print("Coffee:", resources["coffee"])
    print("Money:", total_money)

def check_resource(user_input):
    value = MENU[user_input]["ingredients"]
    if value.get("water", 0)>resources["water"]:
        print("Sorry there is not enough water.")
        return False
    elif value.get("milk", 0)>resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    elif value.get("coffee", 0)>resources["coffee"]:
        print("Sorry there is not enough coffee.") 
        return False
    return True

def calculate_coin(user_quater, user_dimes, user_nickel, user_penny):
    total = (user_quater * 0.25)+(user_dimes * 0.10)+(user_nickel * 0.05)+(user_penny * 0.01)
    return round(total, 2)


def make_coffee(drink):
    value = MENU[drink]["ingredients"]
    resources["water"] -= value.get("water", 0)
    resources["milk"] -= value.get("milk", 0)
    resources["coffee"] -= value.get("coffee", 0)

machine_status = True
while machine_status:
    user_input = input("​What would you like? (espresso/latte/cappuccino):").lower()
    
    if user_input == "off":
        machine_status = False
        print("Machine is been off")

    elif user_input == "report":
        report_machine()

    elif user_input in MENU:
        is_enough = check_resource(user_input)
        if is_enough:
            print("Insert the Coin:")
            user_quater = int(input("How many quarters?:"))
            user_dimes = int(input("How many dime?:"))
            user_nickel = int(input("How many nickel?:"))
            user_penny = int(input("How many penny?:"))
            payment = calculate_coin(user_quater, user_dimes, user_nickel, user_penny)
            if payment >= MENU[user_input]["cost"]:
                make_coffee(user_input)
                
                change = round(payment - MENU[user_input]["cost"], 2)

                total_money += MENU[user_input]["cost"]
                print(f'Here is your {user_input}. Enjoy! ☕')
                print(f'Here is ${change} dollars in change')
            else:
                print("​Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry its a invalid input. Please choose from this (espresso/latte/cappuccino).")


