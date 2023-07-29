phy = int(input("enter marks in physics:"))
chem = int(input("enter marks in chemistry:"))
his = int(input("enter marks in history:"))
comp = int(input("enter marks in computers:"))
eng = int(input("enter marks in english:"))

total = phy+his+chem+comp+eng

percentage = (total/500)*100

if percentage > 33:
    print("pass")
else:
    print("fail")
