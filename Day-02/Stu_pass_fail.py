First_sub = int(input("Enter marks for 1st subject:"))
Second_sub = int(input("Enter marks for 2nd subject:"))
Third_sub = int(input("Enter marks for 3rd subject:"))

Average = (First_sub+Second_sub+Third_sub)/3

if Average>40 and First_sub>=33 and Second_sub>=33 and Third_sub>=33:
    print("Passed")
else:
    print("Fail")
