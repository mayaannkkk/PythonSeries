def net_price(list_price, discount=0, tax=0.05):  # in general discount is 0 and sales tax in 5 percent
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))
print(net_price(500,0.1)) #when customer has 10 percent coupon code
print(net_price(500,0.1,0)) #when customer doesn't pay salestax



