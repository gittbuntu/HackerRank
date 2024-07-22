from keyword import kwlist, softkwlist


# for async programming
# import asyncio

# async def main() -> None:
#     print('I am an asynchronous function')
# if __name__ == '__main__':
#     asyncio.run(main=main())


def display_keywords() -> None:
    
    print("keywords:")
    for i, kw in enumerate(kwlist, start=1):
        print(f"{i:2}: {kw}")

    print('Soft keywords:')
    for i, skw in enumerate(softkwlist, start=1):
        print(f"{i:2}:{skw}")


def main() -> None:
    display_keywords()


if __name__ == '__main__':
    main()



#assertion error
# limit = 10
# n = 20
# assert n < limit, f"{n} is not less than {limit}."

#lambda
(lambda x: print(x))(10) 
# (function parameter: statement)(argument)
#e.g
def print_result(func, elements):
    for elm in elements:
        print(func(elm))

print_result(lambda x: x*2, [1,2,3,4])

print("---------------------------------")

from typing import Generator

def generate(limit):
    for i in range(0, limit):
        yield i 

var= generate(limit=10)
print(var)
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(list(var))

