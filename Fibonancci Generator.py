num = int(input("Enter the number to generate fibonacci series: "))


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(f"The fibonacci of number {num} is {fib(num)}.")
