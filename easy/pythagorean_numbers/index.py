from math import sqrt

def _pythagorean_numbers(a_corner, b_corner):
    c_square=a_corner**2+b_corner**2
    c_corner = int(sqrt(c_square))
    if ((c_square - c_corner**2) == 0):
        return True
    else:
        return False

print(_pythagorean_numbers(5,12))