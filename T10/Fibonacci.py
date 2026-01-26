import math


# Function to calculate the nth Fibonacci number using memoization (safe version)
def fibonacci(n, memo=None):
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# Function to calculate the area of a circle with input validation
def circle_area(radius):
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number.")
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    return math.pi * radius ** 2


# Function to find the maximum value in a list using recursion (optimized)
def find_max(numbers):
    if not numbers:
        raise ValueError("Cannot find the maximum of an empty list.")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers.")

    def helper(index):
        if index == len(numbers) - 1:
            return numbers[index]
        max_rest = helper(index + 1)
        return max(numbers[index], max_rest)

    return helper(0)


# Function to compute the geometric mean of a list of numbers
def geometric_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate geometric mean of an empty list.")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numbers.")
    if any(num <= 0 for num in numbers):
        raise ValueError("All numbers must be positive for geometric mean.")

    log_sum = sum(math.log(num) for num in numbers)
    return math.exp(log_sum / len(numbers))


# Main function to demonstrate the operations
def main():
    print("=== Fibonacci ===")
    n = 30
    try:
        print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n=== Circle Area ===")
    radius = 5
    try:
        print(f"The area of a circle with radius {radius} is: {circle_area(radius)}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n=== Find Max ===")
    numbers = [3, 7, 2, 9, 5]
    try:
        print(f"The maximum value in the list {numbers} is: {find_max(numbers)}")
    except (ValueError, TypeError) as e:
        print(e)

    print("\n=== Geometric Mean ===")
    numbers = [1, 2, 4, 8]
    try:
        print(f"The geometric mean of {numbers} is: {geometric_mean(numbers)}")
    except (ValueError, TypeError) as e:
        print(e)


if __name__ == "__main__":
    main()
