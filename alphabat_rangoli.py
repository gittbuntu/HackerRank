

# 1.alphabat
# 2.width
# 3.rhombus
#    top
#   left-triangle and right-triangle
#    bottom
#    left-triangle and right-triangle
# 4.wholestructure
# --------------------
# center size determine the size of rangoli (5 alphabats in decending order and 4 alphabats in accending order, total
# 9 alphabats but between these alphabats there is 8 hiphens('-'),so width of rangoli is 8*9= 17
# if size of n = 5
#      5             +      5-1           +     (5+5-1) -1
# 5 alphabats in dec + 4 alphabats in ass + total -1 hiphens('-')
#      3             +      3-1           +     (3+3-1) -1
#      2             +      2-1           +     (2+2-1) -1
#      n             +      n-1           +     (n+n-1) -1 (count of n's is 4 and count 0f 1's is 3)
#  4 * n -3 (is the formula of witdh)

# 0   1   2   3   4
# a   b   c   d   e
# n-5 n-4 n-3 n-2 n-1

# list-slicing
#  Right-triangle in assending         left-triangle in decending
#      n-1:n (e)                          n-1:n-0:-1 () (in slicing -1 indicte reverse order)
#      n-2:n (d,e)                        n-1:n-1:-1 (e)
#      n-3:n (c,d,e)                      n-1:n-2:-1 (e,d)
#      n-4:n (b,c,d,e)                    n-1:n-3:-1 (e,d,c)
#      n-5:n (a,b,c,d,e)                  n-1:-4:-1 (e,d,c,b)
#      n-i:n                              n-1:n-i:-1

import string

list = []


def print_rangoli(size):
    # your code goes here
    n = size
    width = 4 * n - 3
    char = string.ascii_lowercase
    for i in char:
        list.append(i)
    for i in range(1, n+1):
        print('-'.join(list[n-1:n-i:-1]+list[n-i:n]).center(width, '-'))
    for i in range(n-1, 0, -1):
        print('-'.join(list[n-1:n-i:-1]+list[n-i:n]).center(width, '-'))


n = int(input())
print(print_rangoli(n))
