my_file = open('first_file.txt', 'r+')
row = my_file.readlines()


def first_string():
    print(f'Printed first string:---> {row[0]}')


def fifth_string():
    print(f'Printed fifth string:---> {row[4]}')


def first_five_strings():
    for every_string in row[0:4]:
        print(every_string.rstrip())


def from_s1_to_s2_strings():
    s1 = int(input("\nFirst string: "))
    s2 = int(input("Second string: "))
    for every_string in row[s1-1:s2]:
        print(every_string.rstrip())


def all_file():
    my_file.seek(0)
    while True:
        line = my_file.readline().rstrip()
        if not line:
            break
        print(line)


my_file.close()

