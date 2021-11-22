test = {}


def __init__():
    while True:
        input1 = str(input())
        if input1 == "add":
            name = str(input())
            count = int(input())
            test.update({name: count})
        else:
            print(test)
