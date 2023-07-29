a = input("enter a string : ").lower()
for i in range(0, len(a)):
    if a[i] in "aeiou":
        b = a.replace(a[i], "_")
print(b)
c = b.split('_')
print(c)
