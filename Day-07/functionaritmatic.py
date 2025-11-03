def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z


print(add(3, 2))
print(subtract(3, 2))
print(multiply(3, 2))
print(divide(3, 2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last #concatenate the string together return as a single string 


print(create_name("mayank","goyal"))
