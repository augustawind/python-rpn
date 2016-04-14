#! /usr/bin/env python
'''Reverse Polish Notation calculator.'''
from decimal import Decimal
import decimal
import math
import operator as op
import re

# Increase outer limits for exponents as much as possible
decimal.DefaultContext.Emax = decimal.MAX_EMAX
decimal.DefaultContext.Emin = decimal.MIN_EMIN

class RPNError(Exception):
    '''Exception for bad RPN input.'''

    def __init__(self, message:str):
        self.message = message

    def __str__(self) -> str:
        return self.message

def solve_rpn(equation:str, context=decimal.DefaultContext) -> Decimal:
    '''Solve an arithmetic problem in Reverse Polish Notation.'''
    decimal.setcontext(context)

    binary_ops = {'+': Decimal.__add__, '-': Decimal.__sub__,
                  '*': Decimal.__mul__, '/': Decimal.__truediv__,
                  '%': Decimal.__mod__, '**': Decimal.__pow__,
                  '//': Decimal.__floordiv__}

    unary_ops = {'abs': Decimal.__abs__, 'sqrt': Decimal.sqrt,
                 'ceil': Decimal.__ceil__, 'floor': Decimal.__floor__}

    number = re.compile(r'''-?  # optional minus sign
                            \d* # zero or more digits
                            \.? # optional decimal point
                            \d+ # one or more digits''', re.VERBOSE)

    stack = []
    for unit in re.split(r'\s+', equation.strip()):
        if number.match(str(unit)):
            stack.append(unit)
        elif unit in binary_ops:
            if (len(stack) < 2):
                raise RPNError("Too few arguments for operator "
                                 "'{}'".format(unit))

            num = binary_ops[unit](Decimal(stack.pop()), Decimal(stack.pop()))
            stack.append(num)
        elif unit in unary_ops:
            if (len(stack) < 1):
                raise RPNError("Too few arguments for operator "
                                 "'{}'".format(unit))

            num = unary_ops[unit](Decimal(stack.pop()))
            stack.append(num)
        else:
            raise RPNError("Unknown identifier '{}'".format(unit))
    else:
        if (len(stack) > 1):
            raise RPNError("No remaining operator(s) for numbers "
                             "{}".format(', '.join(map(str, stack))))

        return stack[0]
