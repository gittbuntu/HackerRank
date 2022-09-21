# 1st method

from turtle import position


string2 = "abracadabra"
l = list(string2)
l[5] = 'k'
print(l)
string2 = ''.join(l)
print(string2)

# 2nd method

string1 = "abracadabra"
string1 = string1[:5] + "k" + string1[6:]
print(string1)

# Through function


def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = ''.join(string)
    return string


string = input()
position, character = input().split()

mutate = mutate_string(string, int(position), character)
print(mutate)
