def square(number):
    if number < 0:
        raise ValueError("square must be between 1 and 64")
    elif number == 0:
        raise ValueError("square must be between 1 and 64")
    elif number > 64:
        raise ValueError("square must be between 1 and 64")

    expo_num = number - 1

    total = 2 ** expo_num
    return total 


def total():
    return 2 ** 64 - 1
