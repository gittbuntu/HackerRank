
# python_students = []
# n = int(input("Enter Number:"))
# for i in range(0, n):
#     name = input("Enter name:")
#     score = float(input("Enter Score:"))
#     python_students.append([name, score])
python_students = [['Harry', 27], ['Berry', 27], ['Tina', 27], ['Akriti', 41], ['Harsh', 39]]
score = []
new_score =[]
new_list = []
for i in python_students:
    score.append(i[1])
score.sort()
print(score)
for v in score:
    if v not in new_score:
        new_score.append(v)
print(new_score)

second_lowest = new_score[1]
print(second_lowest)
for j in python_students:
    if second_lowest in j:
        new_list.append(j[0])
new_list.sort()
for k in new_list:
    print(k)