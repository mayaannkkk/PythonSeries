# this loop version can be concise using loop comprhension
# dub = []
# for x in range(1, 11):
#    dub.append(x * 2)
# print(dub)

# 1
doubles = [x * 2 for x in range(1, 11)]
print(doubles)

# 2
fruits = ["apple", "banana", "grapes", "orange"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)

# 3
grades = [23, 43, 55, 64, 65, 43, 11, 23]
passing_grade = [x for x in grades if x >= 60]
print(passing_grade)
