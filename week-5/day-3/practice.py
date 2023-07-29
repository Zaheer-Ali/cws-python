"""
Ask sentence
Ask letter


If letter exists
    Then only ask new letter
    Then replace old letter with new letter

Else
    Print does not exists
"""


a = input('Enter a sentence : ')
b = input("enter a letter : ")

if a.find(b) != -1:
    print("it exists")
    c = input("enter a new letter to replace : ")
    d = a.replace(b, c)
    print(d)
else:
    print("does not exists")
