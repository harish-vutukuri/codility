"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) - counter X is increased by 1,
max counter - all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2]
"""

def max_counters(N, A):
    """
    :param N: int
    :param A: list
    :return: list
    """
    counters = [0] * N
    max_counter = 0
    for i in A:
        if i > N:
            for j in range(N):
                counters[j] = max_counter
        else:
            counters[i - 1] += 1
            max_counter = max(max_counter, counters[i - 1])
    return counters

print(max_counters(5, [3, 4, 4, 6, 1, 4, 4]))