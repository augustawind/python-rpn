RPN
===

Reverse Polish Notation calculator for Python.

Binary Operators
----------------

* ``+``: addition
* ``-``: subtraction
* ``*``: multiplication
* ``/``: true division
* ``%``: modulo
* ``//``: floor division
* ``**``: exponentation

Unary Operators
---------------

* ``abs``: absolute value
* ``sqrt``: square root
* ``ceil``: rounding up
* ``floor``: rounding down

Examples
--------

::
    import decimal

    import rpn 
    result = rpn.solve_rpn('3.4 -3 abs + 100 sqrt -')
    print(result) # 3.6

    try:
        rpn.solve_rpn('3 3 3 +')
        rpn.solve_rpn('3 +')
        rpn.solve_rpn('abs')
        rpn.solve_rpn('3 a +')
    except RPNError:
        ...

    try:
        rpn.solve_rpn('0 5 /')
    except decimal.DivisionByZero:
        ...

    try:
        rpn.solve_rpn('-5 sqrt')
    except decimal.InvalidOperation:
        ...

    try:
        rpn.solve_rpn('9999999999999 9999999999999 **')
    except decimal.Overflow:
        ...

CLI Usage
---------

::
    $ rpn "1 2 + 8 -"
    $ 5
