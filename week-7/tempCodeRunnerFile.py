try:
    a = open(input("enter file name : "), "r")
    word = input("Enter a word to search : ")
    b = a.readlines()
    exists = False
    num = 0
    for i in range(len(b)):
        if word in b[i]:
            exists = True
            num = i+1
            break
    if exists:
        print(f"The word {word} first appears on line {num}")
    else:
        print("The word doesnot exists in file")
except FileNotFoundError:
    print("File not found")
