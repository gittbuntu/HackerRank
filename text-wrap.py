import textwrap

string = "This is a very very very very very long string."
print(textwrap.fill(string, 6))


# Hacker rank work like this format::::
# import textwrap

# def wrap(string, max_width):
#     r = textwrap.fill(string, max_width)
#     return r

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)
