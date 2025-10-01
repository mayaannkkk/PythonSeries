menu = {
        "pizza" : 400,
        "popcorn" : 1000,
        "nachos" : 300,
        "colddrink" : 400,
        "chips" : 200,
        "fries" : 400
        }
# Print menu
for key , value in menu.items():
    print(f"{key:10} : {value:.2f}")

cart = []
total = 0

while 1:
    food = input("Select an item (q to quit):").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        print(f"{food} is added into the cart")
    else:
        print(f"{food} is not present in the cart")
for food in cart:
    total +=menu.get(food)
    print(food, end="|")
print()
print(total)