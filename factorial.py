#Factorial
"""
The product of all positive integers less than or equal to n
"""
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

result = factorial(10)
print(result)