import random


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


while True:
    n = random.randint(1, 21)  # Generate a random number between 1 and 21
    print(f"Randomly generated n: {n}")
    print(f"Fibonacci number at position {n}: {fibonacci(n)}")
