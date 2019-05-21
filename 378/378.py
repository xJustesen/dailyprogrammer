#!/bin/python3


def HavelHakimi(seq):
    '''
    The Havel–Hakimi algorithm is an algorithm in graph theory solving the graph realization problem.
    That is, it answers the following question:
            Given a finite list of nonnegative integers, is there a simple graph such that its degree sequence is exactly this list

    This function takes a finite list of nonnegative integers as input (seq) and solves the graph
    realization problem, ouputting either True or False
    '''
    seq = sorted([s for s in seq if s], reverse=True)
    if not seq:
        return True
    elif seq[0] > len(seq) - 1:
        return False
    else:
        return HavelHakimi([s - 1 for s in seq[1:seq[0] + 1]] + seq[seq[0] + 1:])


print(HavelHakimi([16, 9, 9, 15, 9, 7, 9, 11, 17, 11, 4, 9, 12, 14, 14, 12, 17, 0, 3, 16]))
