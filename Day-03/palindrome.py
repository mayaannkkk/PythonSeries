num = int(input("Enter Number:"))
rev = 0

while num != 0:
    ld = num % 10
    rev = rev * 10 + ld
    num = num // 10

print(rev)
