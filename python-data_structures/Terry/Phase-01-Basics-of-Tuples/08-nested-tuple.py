fruits_tuple = ('Strawberry', 'Orange', 'Banana')
second_fruits_tuple = ('Watermelon', 'Grapes')
nested_tuple = (fruits_tuple, second_fruits_tuple)

print(f'Accesing the first element {nested_tuple[0]}')
print(f'Accesing the first element of the first element {nested_tuple[0][0]}')