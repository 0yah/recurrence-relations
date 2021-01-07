#Fibonnaci
# The next number of the sequence is the sum of the prevoius two numbers


def fibonacci(n):
    counter = 1
    term_one = 0
    term_two = 1
    next = 0

    while counter < n:
        next = term_one + term_two
        term_one = term_two
        term_two = next
        counter = counter +1
    
    return next

terms = 8
answer = fibonacci(terms)
print(answer)
