import random
import string

chars = string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
random.shuffle(chars)
print(chars)

amount = int(input("Enter how many numbers of digits password you want:"))
if amount < 8:
    print("Password length must be atleast 8")
else:
    time = 0
    password = ""
    while amount:
        password += chars[time]
        time = time + 1
        amount = amount - 1

    print(f"Your Password is:{password}")
