def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(add(1, 2, 3))  # it packs all the argument in a single args


def address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:10}:{value:10}")

print(address(steet="GBU",
              city="Gr. noida",
              state="UP",
              zip="212121"))