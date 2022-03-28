"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an i S such that 0 ≤ S < N - 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.
"""

def solution(A):
    leaders = {}
    leader = -1

    for i in A:
        if i in leaders:
            leaders[i] += 1
        else:
            leaders[i] = 1
    
    for k in leaders:
        if leaders[k] > len(A) // 2:
            leader = k
            break
        else:
            return 0
    
    leader_count = []
    num_leader = 0
    
    for item in A:
        if item == leader:
            num_leader += 1
            leader_count.append(num_leader)
        else:
            leader_count.append(num_leader)

    # print(leader_count)
    num_equi_leader = 0
    
    for i in range(len(A)):
        total_num_leader = leader_count[-1]
        left_num_leader = leader_count[i]
        right_num_leader = total_num_leader - left_num_leader
        left_leader_threshold = float( (i+1) / 2)
        right_leader_threshold = float( (len(A)-i-1) / 2)
        if left_num_leader > left_leader_threshold and right_num_leader > right_leader_threshold:
            num_equi_leader += 1
    
    return num_equi_leader

print(solution([4, 3, 4, 4, 4, 2]))