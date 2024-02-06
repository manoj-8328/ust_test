"""This program is to fetch all the values that are divided by 5 and 7
Arguments: n
"""

def smart_devide(func):
    def inner(n):
        print("Start")
        func(n)
        print("End")
    return inner


@smart_devide
def devide(n):
    for i in range(1, n+1):
        if i % 5 == 0 and i % 7 == 0:
            print(i, end = ",")
            break
    else:
        print("There no divisible number by 5 and 7.")