from decimal import Decimal
import decimal

import pytest

from rpn import solve_rpn, RPNError

def test_add():
    assert solve_rpn('3 5 +') == 5 + 3
    assert solve_rpn('-5 3 +') == 3 + (-5)
    assert solve_rpn('5 4 + 3 +') == 3 + (4 + 5)
    assert solve_rpn('3.4 2.2 +') == Decimal('2.2') + Decimal('3.4')

def test_sub():
    assert solve_rpn('3 5 -') == 5 - 3
    assert solve_rpn('-5 2 -') == 2 - (-5)
    assert solve_rpn('5 -2 -') == (-2) - 5
    assert solve_rpn('3.4 2.2 -') == Decimal('2.2') - Decimal('3.4')
    assert solve_rpn('5 4 - 3 -') == 3 - (4 - 5)

def test_mul():
    assert solve_rpn('3 5 *') == 5 * 3
    assert solve_rpn('-5 2 *') == 2 * (-5)
    assert solve_rpn('5 -2 *') == (-2) * 5
    assert solve_rpn('3.4 2.2 *') == Decimal('2.2') * Decimal('3.4')
    assert solve_rpn('5 4 * 3 *') == 3 * (4 * 5)

def test_truediv():
    assert solve_rpn('3 5 /') == Decimal('5') / Decimal('3')
    assert solve_rpn('-6 2 /') == Decimal('2') / Decimal('-6')
    assert solve_rpn('5 -2 /') == Decimal('-2') / Decimal('5')
    assert solve_rpn('3.4 2.2 /') == Decimal('2.2') / Decimal('3.4')
    assert solve_rpn('5 4 / 3 /') == Decimal('3') / (Decimal('4') /
                                                     Decimal('5'))

def test_mod():
    assert solve_rpn('3 5 %') == 5 % 3
    assert solve_rpn('-5 2 %') == 2 % Decimal('-5')
    assert solve_rpn('5 -2 %') == Decimal('-2') % 5
    assert solve_rpn('3.4 2.2 %') == Decimal('2.2') % Decimal('3.4')
    assert solve_rpn('5 4 % 3 %') == 3 % (4 % 5)

def test_pow():
    assert solve_rpn('3 5 **') == 5 ** 3
    assert solve_rpn('-5 2 **') == 2 ** (-5)
    assert solve_rpn('5 -2 **') == (-2) ** 5
    assert solve_rpn('3.4 2.2 **') == Decimal('2.2') ** Decimal('3.4')
    assert solve_rpn('5 4 ** 3 **') == Decimal('3') ** (Decimal('4') **
                                                        Decimal('5'))

def test_floordiv():
    assert solve_rpn('3 5 //') == 5 // 3
    assert solve_rpn('-5 2 //') == 2 // Decimal('-5')
    assert solve_rpn('5 -2 //') == Decimal('-2') // 5
    assert solve_rpn('3.4 2.2 //') == Decimal('2.2') // Decimal('3.4')
    assert solve_rpn('5 7 // 3 //') == 3 // (7 // 5)

def test_abs():
    assert solve_rpn('3 abs') == abs(3)
    assert solve_rpn('-5 abs') == abs(-5)
    assert solve_rpn('3.4 abs') == abs(Decimal('3.4'))
    assert solve_rpn('-3.4 abs') == abs(Decimal('-3.4'))

def test_sqrt():
    assert solve_rpn('3 sqrt') == Decimal('3').sqrt()
    assert solve_rpn('3.4 sqrt') == Decimal('3.4').sqrt()

def test_ceil():
    assert solve_rpn('3.4 ceil') == Decimal(3.4).__ceil__()
    assert solve_rpn('-3.4 ceil') == Decimal(-3.4).__ceil__()

def test_floor():
    assert solve_rpn('3.4 floor') == Decimal(3.4).__floor__()
    assert solve_rpn('-3.4 floor') == Decimal(-3.4).__floor__()

def test_stack():
    assert solve_rpn('3 -4 abs + 7 * 10 100 sqrt - *') == 0

def test_rpn_error():
    with pytest.raises(RPNError):
        solve_rpn('3 +')

    with pytest.raises(RPNError):
        solve_rpn('3 3 3 +')

    with pytest.raises(RPNError):
        solve_rpn('3 4 + 3 - *')

    with pytest.raises(RPNError):
        solve_rpn('3 4 + a -')

def test_decimal_errors():
    with pytest.raises(decimal.Overflow):
        solve_rpn('999999999999999999999999999 9999999999999999 **')

    with pytest.raises(decimal.InvalidOperation):
        solve_rpn('-5 sqrt')

    with pytest.raises(decimal.DivisionByZero):
        solve_rpn('0 5 /')
        solve_rpn('0 5 //')

def test_whitespace():
    assert solve_rpn('  4   3 +   5  -     ') == -2
