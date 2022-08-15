def is_armstrong_number(number):
    numbers = [int(value) ** len(str(number)) for value in str(number)]

    return sum(numbers) == number
