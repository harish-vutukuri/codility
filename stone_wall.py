"""
You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N-1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.
"""

def solution(H):
    """
    :param H: list[int]
    :return: int
    """
    stack = []
    blocks = 0
    for h in H:
        while stack and stack[-1] > h:
            stack.pop()
        if not stack or stack[-1] < h:
            stack.append(h)
            blocks += 1
    return blocks

print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))