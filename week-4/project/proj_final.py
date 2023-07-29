questions = ["What is capital of India?",
             "What is the national bird of India?",
             "How many states are there in India?",
             "Which is the longest river in the world?",
             "what is the height of mount everesrt?"]

options = [["a) Delhi", "b) Mumbai", "c) Chennai", "d) Kolkata"],
           ["a) Eagle", "b) Peacock", "c) Ostrich", "d) Pegion"],
           ["a) 27", "b) 28", "c) 29", "d) 31"],
           ["a) Amazon", "b) Nile", "c) Mississippi", "d) Brahmaputra"],
           ["a) 7562m", "b) 8102m", "c) 8762m", "d) 8849m"]]

answers = ["a", "b", "b", "b", "d"]
total_score = 0
for i in range(0, len(questions)):
    print(questions[i])
    for j in range(0, len(options[i])):
        print(options[i][j])
    choice = input("Choose an option : ")
#     if i == 0:
#         if choice == "a":
#             total_score += 4
#     if i == 1:
#         if choice == "b":
#             total_score += 4
#     if i == 2:
#         if choice == "b":
#             total_score += 4
#     if i == 3:
#         if choice == "b":
#             total_score += 4
#     if i == 4:
#         if choice == "d":
#             total_score += 4
    if choice == answers[i]:
        total_score += 1
print(total_score)
