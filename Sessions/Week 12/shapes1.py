# print odd numbers for number of rows = limit

def my_version(max):
    for i in range(0, max):
        if i < max / 2:
            print("*" * (i * 2 + 1))
        else:
            print("*" * ((max - i) * 2 + 1))

def other_version(max):
    for i in range(1, max + 1, 2):
        print("*" * i)
    for i in range(max + 1, 0, -2):
        print("*" * i)

my_version(int(input("ENTER: ")))
