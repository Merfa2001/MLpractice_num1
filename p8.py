def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter an integer: "))

result = factorial(num)

print("The factorial of", num, "is", result)
#done