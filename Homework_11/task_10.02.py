def white_6_lines(file_name: str):
    with open(file_name, 'w+') as my_file:
        string = 1
        while string <= 6:
            my_file.writelines([input(), '\n'])
            string += 1


white_6_lines("file_for_task_10.02.txt")