# with open('open_file.txt') as file:
#     content = file.read()
#     print(content)

with open('not_a_file.txt', 'r') as file:
    # content = file.read()
    print(dir(file))
    print()
    print(file.name)
    print()
    print(file.read())