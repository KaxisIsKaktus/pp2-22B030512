import os

file_path = input('Enter a file path: ')

print(file_path)

if os.path.exists(file_path):
    print('The file exists')

    with open(file_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

        print(lines)
else:
    print('The specified file does NOT exist')
