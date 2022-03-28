"""
given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
"""

def count_div(A, B, K):
    """
    :param A: int
    :param B: int
    :param K: int
    :return: int
    """
    return sum(i % K == 0 for i in range(A, B + 1))


print(count_div(6, 11, 2))