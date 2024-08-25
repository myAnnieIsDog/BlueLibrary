import math
import numbers
from pprint import pprint
import random
import statistics

D = decimal.Decimal
cntxt = decimal.getcontext()

pi5 = D('3.14159')
tau5 = 2 * pi5
print(str(pi5) + ' is the value of PI, defined as the perimeter divided by DIAMETER.')
print(str(tau5) + ' is the value of TAU, defined as the perimeter divided by RADIUS.\n')


print(D(2).sqrt())
print(D(1).exp())
print(D(10).ln())
print(D(10).log10())
print(D(5).logb(cntxt))


def run()
    data = sorted(list(map(
        D, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split())))
    sum = 0
    for i in data:
        print(moneyfmt(i).rjust(20))
        sum += i
    total = 'Total =  ' + moneyfmt(sum)
    print(total.rjust(20))

def moneyfmt(value, places=2, curr='$', sep=',', dp='.',
             pos='', neg='(', trailneg=')'):
    """Convert Decimal to a money formatted string.
    From https://docs.python.org/3/library/decimal.html 

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = D(10) ** -places      # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = list(map(str, digits))
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')
    if places:
        build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))


if __name__ == '__main__':
    run()
    
