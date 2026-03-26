"""
Scenario: Smart Shopping Cart (Functions & *args)
Question: Write a function that calculates the total price of a shopping cart. 
The number of items is unknown. The function should sum all prices. 
If the total is over 500 TL, apply a 10% discount and return the final price.
"""


def calculate_cart_total(*prices):
    total=sum(prices)
    if total>500:
        total=total*0.90
        print(" discount applied(%10)")

    return total        

print("Total 1:", calculate_cart_total(100, 200, 50))       
print("Total 2:", calculate_cart_total(300, 400))           
print("Total 3:", calculate_cart_total(50, 100, 200, 300))  


print("**********************************")


"""
Scenario: Finding the Most Expensive Item
Question: You have a dictionary of items and their prices. 
Write a function that finds and returns the name and price 
of the most expensive item in the cart.


cart = {
    "Laptop": 15000,
    "Mouse": 450,
    "Keyboard": 1200,
    "Monitor": 3500
}

"""


cart = {
    "Laptop": 15000,
    "Mouse": 450,
    "Keyboard": 1200,
    "Monitor": 3500
}


def find_most_expensive(shopping_dict):
    max=0
    item=""

    for k,v in cart.items():
        if v>max:
            max=v
            item=k

    return item,max        

print(find_most_expensive(cart))



print("********************************")

"""
Scenario: Inventory Control and Billing
Question: You have two dictionaries: 'prices' and 'stock'.
Write a function that takes an item name and quantity.
If stock is sufficient, return the total price and decrease the stock.
Otherwise, return an "Insufficient stock" message.


prices = {"iPhone": 50000, "MacBook": 80000, "AirPods": 5000}
stock = {"iPhone": 5, "MacBook": 2, "AirPods": 10}

"""


prices = {"iPhone": 50000, "MacBook": 80000, "AirPods": 5000}
stock = {"iPhone": 5, "MacBook": 2, "AirPods": 10}


def sell_product(name,quantity):
    if name in prices:
        if quantity<=stock[name]:
            total=prices[name]*quantity
            stock[name]-=quantity
            return f"total: {total} ----> remaining stock for {name} : {stock[name]}"
        else:
            print("ERROR: insufficent stock!")
    else:
        print("ERROR: product not found!")            

print(sell_product("iPhone", 2))  
print(sell_product("MacBook", 5)) 
print(sell_product("iPad", 1))    
