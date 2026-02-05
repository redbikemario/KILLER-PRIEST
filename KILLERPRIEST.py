import random

NAME_LIST = []

def setup():
    global NAME_LIST
    global name
    for i in range(1,9,1):
        name = str(input(f"name {i} here     "))
        NAME_LIST.append(name)

setup()
print(NAME_LIST)
