num = int(input("Enter Number:"))
count = 0
isPrime = False
if num == 0 or num == 1:
    print(f"{num} is neither prime nor composite")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        isPrime = True
    print("Prime Number" if isPrime else "Not a Prime Number")
