def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def min_max(numbers):
    if not numbers:
        return None, None
    return min(numbers), max(numbers)


def count_even(numbers):
    return sum(1 for n in numbers if n % 2 == 0)
