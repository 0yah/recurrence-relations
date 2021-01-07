# Tower of Hanoi
"""
The Tower of Hanoi is a mathematical puzzle consisting of three towers
and more than one ring. Rings are of different sizes and stacked in ascending order.

Rules:
    1. Only one disk can move among the towers at a time
    2. Only the top disk on a given tower can be removed
    3. No large disk can sit over a small disk
"""

def tower(a, fro, aux, to):
    
    if a == 1:
        print("Move disc 1 from %s to %s" % (fro, to))
    else:
        tower(a-1, fro, to, aux)
        print("Move disc %s from %s to %s" % (a, fro, to))
        tower(a-1, aux, fro, to)

def no_of_steps(n):
    steps = pow(2,n) - 1
    return steps


tower(10, 'A', 'B', 'C')
steps = no_of_steps(10)
print("Completed after %d moves"%steps)
