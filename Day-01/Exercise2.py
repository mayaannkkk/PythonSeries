item = input("Enter item you want to buy:")
price = float(input("Enter price of that item:"))
quantity = int(input("Quantity of that item:"))

print(f"You bought {quantity} X {item}/s")
total = quantity * price
print(f"Your total is {total}")