user_name = input("Enter Your Name:")

len1 = len(user_name)
res1= user_name.isalpha()

if len1>12:
    print("user_name is incorrect")
elif not user_name.isalpha() == -1:
    print("user_name can't contain spaces")
elif not user_name.isalpha():
    print("User name can't contain spaces")
else:
    print(f"Welcome,f{user_name}")
