"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
"""

def cyclic_rotation(A, K):
    """
    :param A: list
    :param K: int
    :return: list
    """
    return A[-K:] + A[:-K]


print(cyclic_rotation([3, 8, 9, 7, 6], 3))