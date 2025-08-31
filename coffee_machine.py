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
    "profit":0
}

status="on"
def check_resources(coffee):
    option=0
    if (resources["water"] < MENU[coffee]["ingredients"]["water"]):
        print("Sorry there is not enough water!")
        option+=1
    if (cmd!="espresso"):
        if (resources["milk"] < MENU[coffee]["ingredients"]["milk"]):
            print("Sorry there is not enough milk!")
            option += 1

    if (resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]):
        print("Sorry there is not enough milk!")
        option+=1
    return option

def report():
    print(f"--- Available resourses ---")
    print(f"Water : {resources["water"]}")
    print(f"Milk : {resources["milk"]}")
    print(f"Coffee : {resources["coffee"]}")
    print(f"Profit :{resources["profit"]}")

def prepare_coffee(coffee):
    resources["water"]-=MENU[coffee]["ingredients"]["water"]
    if coffee!="espresso":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]

money=0

def check_money(p,n,d,q,c):
    global money
    total_amt=MENU[c]["cost"]
    user_amount=0
    user_amount+=(p*0.01)+(n*0.05)+(d*0.10)+(q*0.25)
    if(user_amount>total_amt):
        print(f"Take your change ${user_amount-total_amt}")
        resources["profit"]+=user_amount
    elif(user_amount==total_amt):
        resources["profit"] += user_amount
    elif(user_amount<total_amt):
        print(f"Insert a sufficient amount to but {c}  ")
        print(f" {c} cost is : ${total_amt}")
        money+=1

while status=="on":
    cmd=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if cmd == "espresso" or cmd == "latte" or cmd == "cappuccino":
        a=check_resources(cmd)
        if(a>0):
            print("Try again or refill the resources !")
            continue
        print("please insert the coin : ")
        pennies=int(input("Insert a pennies :"))
        nickel=int(input("Insert a nickel :"))
        dimes=int(input("Insert a dimes :"))
        quarter=int(input("Insert a quarter :"))
        check_money(pennies,nickel,dimes,quarter,cmd)
        if(money==1):
            continue
        else:
            print(f"Here you go ! Enjoy your {cmd} ☕ :) ")
        prepare_coffee(cmd)
    elif cmd=="report":
        report()
    elif cmd=="off":
        print("Shutting down......!!!")
        break

    else:
        print("Enter a valid input !")
