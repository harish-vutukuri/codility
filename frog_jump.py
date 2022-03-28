"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.
"""

def frog_jump(X, Y, D):
    """
    :param X: int
    :param Y: int
    :param D: int
    :return: int
    """
    if Y < X:
        return 0
    return (Y - X) // D + 1

print(frog_jump(10, 85, 30))