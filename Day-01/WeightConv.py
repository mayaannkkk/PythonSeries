weight = float(input("Enter Your weight:"))
unit = input("Enter unit kilo or pound (K or L):")

if unit == "k":
    weight *= 2.205
    unit = "lbs"
elif unit == "l":
    weight /= 2.205
    unit = "kgs"
else:
    print(f"{unit} was not valid")

print(f"Your weight is {round(weight, 1)} {unit}/s")
