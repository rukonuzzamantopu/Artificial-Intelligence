def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
n = 10  
print(f"The first {n} numbers in the Fibonacci series are: {fibonacci(n)}")