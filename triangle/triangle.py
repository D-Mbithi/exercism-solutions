def is_valid_triangle(a, b, c):
    if a + b >= c and b + c >= a and c + a >= b:
        return True
    else:
        return False


def equilateral(sides):
    if 0 in sides:
        return False

    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == b and b == c and a == c:
        return True
    return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if not is_valid_triangle(a, b, c):
        return False

    if a == b and a == c:
        return True
    elif a == b and b != c:
        return True
    elif a != b and a == c:
        return True
    elif a != b and b == c:
        return True
    else:
        return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if not is_valid_triangle(a, b, c):
        return False

    if a != b and b != c and a != c:
        return True
    return False
