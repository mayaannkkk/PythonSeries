Num1 = int(input("Enter 1st Number:"))
Num2 = int(input("Enter 2nd Number:"))
Num3 = int(input("Enter 3rd Number:"))
Num4 = int(input("Enter 4th Number:"))

if Num1>=Num2 and Num1>=Num3 and Num1>=Num4:
    print(Num1)
elif Num2>=Num1 and Num2>=Num3 and Num2>=Num4:
    print(Num2)
elif Num3>=Num2 and Num3>=Num1 and Num3>=Num4:
    print(Num3)
elif Num4>=Num2 and Num4>=Num3 and Num4>=Num1:
    print(Num4)

# largest = Num1
#
# if Num2 > largest:
#     largest = Num2
# if Num3 > largest:
#     largest = Num3
# if Num4 > largest:
#     largest = Num4
#
# print("The largest number is:", largest)

