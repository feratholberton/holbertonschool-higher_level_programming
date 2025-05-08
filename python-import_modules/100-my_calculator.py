#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    # Messages
    usage_error_massage = 'Usage: ./100-my_calculator.py <a> <operator> <b>'
    unknown_operator_message = 'Unknown operator. Available operators: +, -, * and /'

    supported_operators = ['+', '-', '*', '/']

    # Get arguments excluding the file name -> sys.argv[0]
    arguments = argv[1:]

    # Count retrieved arguments
    arguments_qty = len(arguments)

    def calculate():
        # Check if arguments quantity is 3
        if arguments_qty != 3:
            print(usage_error_massage)
            exit(1)
        # Give name to retrieved arguments if they are three
        else:
            operand_a = int(arguments[0])
            operator = arguments[1]
            operand_b = int(arguments[2])

            # Check if the operator is a supported
            if operator not in supported_operators:
                print(unknown_operator_message)
                exit(1)
            else:
                if operator == '+':
                    print(f'{operand_a} {operator} {operand_b} = {add(operand_a, operand_b)}')
                elif operator == '-':
                    print(f'{operand_a} {operator} {operand_b} = {sub(operand_a, operand_b)}')
                elif operator == '*':
                    print(f'{operand_a} {operator} {operand_b} = {mul(operand_a, operand_b)}')
                else:
                    print(f'{operand_a} {operator} {operand_b} = {div(operand_a, operand_b)}')

    calculate()
