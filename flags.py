"""
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N - 1 and A[P - 1] < A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly four peaks: elements 1, 3, 5 and 10.
"""

def solution(heights):
    N = len(heights)
    peaks = [0] * N
    cnt = 0

    for i in range(N - 2, 0, -1):
        if heights[i - 1] < heights[i] > heights[i + 1]:
            peaks[i] = i
            cnt += 1
        else:
            peaks[i] = peaks[i + 1]

    for intended in range(cnt, 0, -1):
        planted, i = 0, 1
        while i < N and peaks[i] and planted < intended:
            i = peaks[i]
            planted += 1
            i += intended
        if intended == planted:
            return planted
    
    return 0

print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))   