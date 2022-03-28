"""
given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [-1, -3], the function should return 1.
"""

def missing_integer(A):
    """
    :param A: list
    :return: int
    """
    A = list(set(A))
    A.sort()
    for i in range(1, len(A) + 1):
        if A[i - 1] != i:
            return i
    return len(A) + 1

print(missing_integer([1, 3, 6, 4, 1, 2]))
print(missing_integer([-1, -3]))
print(missing_integer([1, 2, 3]))