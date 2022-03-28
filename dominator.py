"""
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
"""

def solution(A):
    """
    :param A: list[int]
    :return: int
    """
    dominator = {}
    for i in A:
        if i in dominator:
            dominator[i] += 1
        else:
            dominator[i] = 1
    
    for k in dominator:
        if dominator[k] > len(A) // 2:
            return A.index(k)
        else:
            return -1

print(solution([3, 4, 3, 2, 3, -1, 3, 3]))