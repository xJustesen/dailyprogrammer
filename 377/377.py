#!bin/bash/python3
import math as m
from report_memory_usage import *


def FitBox(Crate, Box):
    ''' Calculate how many boxes of size 'Box' can fit in a crate of size 'Crate' '''
    n = [m.floor(Crate[i] / Box[i]) for i in range(len(Crate))]  # number of boxes along each axis
    N = 1
    for i in range(len(n)):
        N *= n[i]
    return N


def FindPermuationIndices(seq):
    k = [i - 1 for i in range(len(seq) - 1, -1, -1) if seq[i] > seq[i - 1]][0]
    l = [i for i in range(len(seq)) if seq[k] < seq[i]].pop()
    return k, l


def PermuteSequence(seq, k, l):
    sl = seq[l]
    sk = seq[k]
    seq[k] = sl
    seq[l] = sk
    seq[k + 1::] = list(reversed(seq[k + 1::]))


def FitBoxRotate(Crate, Box):
    ''' Calculate how many boxes of size 'Box' can fit in a crate of size 'Crate'.
        We can rotate all boxes by 90 degrees against any axis.
     '''
    N1 = 0
    total_permutations = m.factorial(len(Box))
    current_permutation = 1
    while True:
        print('Checking permutation no. ', current_permutation, ' of ', total_permutations)
        N2 = FitBox(Crate, Box)
        if N2 > N1:
            N1 = N2
        # Generate permutation (https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order)
        k, l = FindPermuationIndices(Box)
        if k < 0:
            break
        PermuteSequence(Box, k, l)
        current_permutation += 1
    return N1


help(display_top)

tracemalloc.start()

N = FitBoxRotate([123, 456, 789, 1011, 1213, 1415], [16, 17, 18, 19, 20, 21])
print('Maximum number of boxes = ', N)
snapshot = tracemalloc.take_snapshot()
display_top(snapshot)
