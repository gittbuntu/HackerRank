print("Hello World !", "Hello World !", sep="-",end=" | ")
print("Hello World !")

help(print)

ran = range(1, 11, 2)
print(list(ran))

# Map function
# e.g # 1
string = ["My", "World", "Apple", "Pear !"]

new = map(len, string)
print(list(new))

# e.g # 2

new_string = map(lambda x: x + 's', string)
print(list(new_string))

#filter function
def length_greater(string):
    return len(string) > 4
#e.g-1
len_greater = filter(length_greater, string)
print(list(len_greater))
#e.g-2
len_greater_then = filter(lambda x: len(x) > 4, string)
print(list(len_greater_then))


# Sorted
people = [
    {'name':'Bob','age':20},
    {'name':'Hob','age':25},
    {'name':'Nob','age':30},
    {'name':'Dob','age':35},
]

sorted_list = sorted(people, key=lambda person:person['age'], reverse=True)
print(sorted_list)
