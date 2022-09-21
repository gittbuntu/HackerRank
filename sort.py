list = [45, 54, 23, 2, 6, 9, 89, 78, 87, 4, 6, 3, 0]
new_list = []
_min = 0
_max = 0
while list:
    minimum = list[0]  # arbitrary number in list
    for x in list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    list.remove(minimum)
_min += new_list[0]
_max += new_list[-1]
print(new_list)
print(_min)
print(_max)
