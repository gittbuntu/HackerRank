def count_substring(string, sub_string):
    count = 0
    # while string:
    #     if sub_string.upper() in string.upper():
    #         count += 1
    #         string = string[:-2]
    #     else:
    #         break
    for i in range(0, len(string)):
        if sub_string.lower() in string.lower():
            count += 1
            string = string[:-2]
    return count


string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)
