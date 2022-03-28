"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.
"""

def missing_elem(A):
    """
    :param A: list
    :return: int
    """
    return sum(range(1, len(A) + 2)) - sum(A)

print(missing_elem([2, 3, 1, 5]))