#! /usr/bin/env python
'''Reverse Polish Notation calculator.'''
import math
import re
import sys
from operator import *

def log_error(message: str):
    '''Print a message to stderr.'''
    print("Error:", message, file=sys.stderr)

def solve_rpn(equation: str) -> float:
    '''Solve an arithmetic problem in Reverse Polish Notation.'''
    binary_ops = {'+': add, '-': sub, '*': mul, '/': truediv, '%': mod,
                  '**': pow, '//': floordiv}
    unary_ops = {'abs': abs, 'sqrt': math.sqrt, 'ceil': math.ceil,
                 'floor': math.floor}

    number = re.compile(r'''-?  # optional minus sign
                            \d* # zero or more digits
                            \.? # optional decimal point
                            \d+ # one or more digits''', re.VERBOSE)

    stack = []
    for unit in equation.split(' '):
        if number.match(unit):
            stack.append(unit)
        elif unit in binary_ops:
            if (len(stack) < 2):
                log_error("Too few arguments for operator '{}'".format(unit))
                break

            num = binary_ops[unit](float(stack.pop()), float(stack.pop()))
            stack.append(str(num))
        elif unit in unary_ops:
            if (len(stack) < 1):
                log_error("Too few arguments for operator '{}'".format(unit))
                break

            num = unary_ops[unit](float(stack.pop()))
            stack.append(str(num))
        else:
            print("Error: Unknown identifier '{}'".format(unit),
                  file=sys.stderr)
            break
    else:
        if (len(stack) > 1):
            log_error("No remaining operator(s) for numbers "
                      "{}".format(', '.join(stack)))
            return

        return float(stack[0])

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        log_error("No equation given")
    else:
        result = solve_rpn(sys.argv[1])
        if result:
            print(result)
