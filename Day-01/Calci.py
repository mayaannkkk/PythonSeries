num1 = float(input("Enter Number one:"))
num2 = float(input("Enter Number two:"))
operator = input("Enter operator:")

if operator == "+":
    print(f"Addition is {num1+num2}")
elif operator == "-":
    print(f"Substraction is {num1-num2}")
elif operator == "*":
    print(f"Multiplication is {num1 * num2}")
elif operator == "/":
    if num2==0:
        print("Division is undefined")
    else:
        print(f"Division is {num1 / num2}")
else:
    print(f"{operator} is not a valid operator")

