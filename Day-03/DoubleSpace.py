from dataclasses import replace

string = input("Enter your string:")
print(string.count("  "))

print(string.replace("  "," "))