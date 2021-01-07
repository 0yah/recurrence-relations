# Tower of Hanoi
"""
The Tower of Hanoi is a mathematical puzzle consisting of three towers
and more than one ring. Rings are of different sizes and stacked in ascending order.

Rules:
    1. Only one disk can move among the towers at a time
    2. Only the top disk on a given tower can be removed
    3. No large disk can sit over a small disk
"""

def tower(disks, source, auxillary, destination):
    
    if disks == 1:
        print("Move disc 1 from %s to %s" % (source, destination))
    else:
        tower(disks-1, source, destination, auxillary)
        print("Move disc %s from %s to %s" % (disks, source, destination))
        tower(disks-1, auxillary, source, destination)

def no_of_steps(n):
    steps = pow(2,n) - 1
    return steps


disks = 3
tower(disks, 'A', 'B', 'C')
steps = no_of_steps(disks)
print("Completed after %d moves"%steps)
