option_list = ['Sunny', 'Rainy', 'Stormy', 'Cloudy', 'Windy']

try:
    num = int(input(f'Which one you like the most: {list(enumerate(option_list))}\n'))
except IndexError:
    print(f'The number you enter is out of range.')
except ValueError:
    print(f'You must enter a number.')
except Exception as e:
    print(e)
else:
    print(f'You entered the number: {num} for {option_list[num]}')
