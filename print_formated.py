# n = int(input())
# w = len(str(bin(n)).replace('0b', ''))
# # print(w)
# for i in range(1, n+1):
#     a = oct(i).replace('0o','').rjust(w, ' ')
#     b = hex(i).replace('0Xupper().rjust(w, ' ')
#     c = bin(i).rjust(w, ' ')
# print(i, a[3:], b[3:], c[2:])

def print_formatted(number):

    l1 = len(bin(number)[2:])

    for i in range(1, number+1):
        print(str(i).rjust(l1, ' '), end=" ")
        print(oct(i)[2:].rjust(l1, ' '), end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1, ' '), end=" ")
        print(bin(i)[2:].rjust(l1, ' '), end=" ")
        print("")


n = int(input())
print_formatted(n)
