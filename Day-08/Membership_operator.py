Word = "APPLE"

letter = input("Guess the letter in the word:").upper()

if letter in Word:
    print(f"There is letter '{letter}' in the word")
else:
    print("There is no such letter in the word")