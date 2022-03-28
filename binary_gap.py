"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
"""

def binary_gap(N):
    """
    :param N: int
    :return: int
    """
    binary = bin(N)[2:]
    max_gap, current_gap = 0, 0
    for i in binary:
        if i == '1':
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            current_gap += 1
    return max_gap

print(binary_gap(1041))