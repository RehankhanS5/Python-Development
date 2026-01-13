def generate_fibonacci(n):
    fib_sequence = []

    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence


# User input
terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer")
else:
    sequence = generate_fibonacci(terms)
    print("Fibonacci sequence:")
    print(sequence)
