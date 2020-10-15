def white_6_lines(file_name: str):
    with open(file_name, 'a') as my_file:
        for _ in range(3):
            input_string = input("Input string: ")
            my_file.write(f'{input_string}\n')


white_6_lines(file_name='file_for_task_10.02.txt')
