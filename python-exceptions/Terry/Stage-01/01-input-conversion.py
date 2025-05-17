try:
    num = int(input('Enter a number: '))
except ValueError:
    print(f'You must enter a number.')
else:
    print(f'You entered the number: {num}')
finally:
    print('Finally exiting.')
