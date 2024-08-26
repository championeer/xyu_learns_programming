def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

fib_20 = fibonacci(20)
print("斐波那契数列的前20个数:")
print(fib_20)
