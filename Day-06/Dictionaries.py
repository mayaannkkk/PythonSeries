capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "Russia ": "Moscow"}

print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("Capitals exist")
else:
    print("Capital Does not exist!")

capitals.popitem()


capitals.update({"USA":"Chinese"})
print(capitals.keys())


keys = capitals.keys()
for key in keys:
    print(key)


# keys = capitals.values()
# # for key in keys:
# #     print(key)

print(capitals.items())