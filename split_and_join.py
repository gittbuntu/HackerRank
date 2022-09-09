def split_and_join(line):
    a = line.split(" ")
    b = a
    c = "-".join(b)
    return c


line = input()
c = split_and_join(line)
print(c)
