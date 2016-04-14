#! /usr/bin/env python
'''Reverse Polish Notation calculator.'''
import math
import re
from operator import *

class RPNError(Exception):
    '''Exception for bad RPN input.'''
    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        return self.message

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
                raise RPNError("Too few arguments for operator "
                                 "'{}'".format(unit))

            num = binary_ops[unit](float(stack.pop()), float(stack.pop()))
            stack.append(str(num))
        elif unit in unary_ops:
            if (len(stack) < 1):
                raise RPNError("Too few arguments for operator "
                                 "'{}'".format(unit))

            num = unary_ops[unit](float(stack.pop()))
            stack.append(str(num))
        else:
            raise RPNError("Unknown identifier '{}'".format(unit))
    else:
        if (len(stack) > 1):
            raise RPNError("No remaining operator(s) for numbers "
                             "{}".format(', '.join(stack)))

        return float(stack[0])
