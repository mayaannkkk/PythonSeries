num = int(input("Enter Number:"))
check = num
summ = 0
digit = len(str(num))
while num!=0:
    ld = num % 10
    summ = summ + pow(ld,digit)
    num = num //10

if summ == check:
    print(f"{check} is a Armstrong Number")
else:
    print(f"{check} is not a Armstrong Number")
