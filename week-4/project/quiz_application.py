print("Welcome to the quiz.")
print("There are total of 5 multiple choice questions in the quiz. \nEach question carries 1 mark \nLet's start!\n")
questions = ["1. Who developed Python Programming Language?",
             "2. Which of the following is the correct extension of the Python file?",
             "3. Which of the following is used to define a block of code in Python language?",
             "4. Which keyword is used for function in Python language?",
             "5. Which of the following character is used to give single-line comments in Python?"]

options = [["a) Wick van Rossum", "b) Rasmus Lerdorf", "c) Guido van Rossum", "d) Niene Stom"],
           ["a) .python", "b) .pl", "c) .py", "d) .p"],
           ["a) Indentation", "b) key", "c) brackets", "d) All of the above"],
           ["a) Function", "b) def", "c) fun", "d) define"],
           ["a) /*", "b) //", "c) !", "d) #"]]

answers = ["c", "c", "a", "b", "d"]

guesses = []
score = 0

for i in range(0, len(questions)):
    print(questions[i])
    for j in range(0, len(options[i])):
        print(options[i][j])
    guess = input("Enter your answer (a, b, c or d): ").lower()
    guesses.append(guess)
    if guess == answers[i]:
        print("Correct Answer!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        score += 1
    else:
        print(f"Incorrect Answer. Correct answer is {answers[i]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("answers: ", end="")
for i in answers:
    print(i, end=" ")
print()

print("guesses: ", end="")
for i in guesses:
    print(i, end=" ")
print()

print(f"Your score is {score} out of 5")

if score == 4 or score == 5:
    print("Good Work! Keep it up!")
elif score == 2 or score == 3:
    print("Work Harder. Better luck next time.")
else:
    print("Underperformed! Improvement needed.")
