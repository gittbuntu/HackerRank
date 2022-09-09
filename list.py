list = []
n = int(input("Enter number :"))
for i in range(n):
    command = input()
    command_list = command.split(" ")
    if command_list[0] == "append":
        list.append(int(command_list[1]))
    elif command_list[0] == "insert":
        list.insert(int(command_list[1]), int(command_list[2]))
    elif command_list[0] == "remove":
        list.remove(int(command_list[1]))
    elif command_list[0] == "pop":
        list.pop()
    elif command_list[0] == "sort":
        list.sort()
    elif command_list[0] == "reverse":
        list.reverse()
    elif command_list[0] == "print":
        print(list)
