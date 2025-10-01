questions = ("How many elements are there in periodic table?:",
             "Which element lays the largest eggs?:",
             "What is the most abundant gas in the earth atmosphere",
             "How many bones are there in human body?:",
             "Which planet in the solar system is the hottest?:")

options = (("A.116", "B.117", "C.118", "D.119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. carbon-dioxide", "D. hydrogen"),
           ("A. 205", "B. 206", "C. 207", "D. 208"),
           ("A. Mercury", "B. venus", "C. Earth", "D. Mars"))
answers = ("C", "D", "A", "B", "B")
score = 0
guesses = []
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter Your guess (A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
    question_num += 1

print("--------------------")
print("     Result         ")
print("--------------------")
res = int(score / len(questions)) * 100
print(res)

print("Answers is", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses is", end="")
for guess in guesses:
    print(guess, end=" ")
