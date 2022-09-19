

def swap(s):
    new_string = ""
    words_list = '''`-=/*+.~!@#$%^&*()_[]{};'\:"|,\| /<>?"'''
    for word in s:
        if word.islower():
            word = word.upper()
            new_string += word
        elif word.isupper():
            word = word.lower()
            new_string += word
        if word.isnumeric():
            new_string += word
        if word in words_list:
            new_string += word
    return new_string


s = '''hACkERrank.com pRESents "pythonist 2"'''
n = swap(s)
print(n)
