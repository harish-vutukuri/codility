"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.
"""

def perm_check(A):
    """
    :param A: list
    :return: int
    """
    A.sort()
    return 1 if list(range(1, max(A) + 1)) == A else 0

print(perm_check([4, 1, 3]))