import random


options = ("Rock", "Paper", "Scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

number = random.randint(1,100) #Generate random number with in range
numb = random.random() #Generate random float number between "0" to "1"
option = random.choice(options)
random.shuffle(cards)



print(cards)
print(number)
print(option)

