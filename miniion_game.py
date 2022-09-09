def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    vowels = "AEIOU"
    list = []
    if string[0] is not vowels:
        for i in range(len(string)):
            for j in range(i+1, len(string)+1):
                list.append(string[i:j])
    stuart_list =[]
    kevin_list = []
    for word in list:
        if word[0] in vowels:
            kevin_list.append(word)
            kevin +=1
        else:
            stuart_list.append(word)
            stuart += 1
    if kevin == stuart or stuart == kevin:
        print("Draw")
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("kevin", kevin)
        
string = input("Enter your string here : ").upper()
minion_game(string)
