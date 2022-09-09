
n = int(input("Number of students : "))
student_marks = {}
for i in range(n):
    line = input("Enter Name and  marks: ").split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input("Enter name of student : ")

new_dict ={}
for keys, values in student_marks.items():
    val = 0
    sum = []
    for v in values:
        sum.append(v)
        val += v 
    val = val / len(sum)
    if keys not in new_dict:
        new_dict[keys] = val
required_format = new_dict[query_name]        
format_float = "{:.2f}".format(required_format)
print(format_float)

