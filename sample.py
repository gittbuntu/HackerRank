string = input("Enter your string:")
s1 = ""
s2 = ""
x = 0
for s in string:
    if x % 2 == 0:
        s1 += s
        # print(s1)
    elif x % 2 == 1:
        s2 += s
    x += 1
print(s1 + " " + s2)
