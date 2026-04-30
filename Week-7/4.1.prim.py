from typing import List, Tuple

def prim(n: int, W: List[List[float]]) -> List[Tuple[int, int, float]]:
    F = []
    nearest = [-1] * (n + 1)
    distance = [-1] * (n + 1)
    INF = float("inf")

    for i in range(2, n + 1):
        nearest[i] = 1
        distance[i] = W[1][i]

    for _ in range(n - 1):
        min = INF
        # Complete the code here
        for i in range(2, n + 1):
            if(0 <= distance[i] < min):
                min = distance[i]
                vnear = i
        F.append((vnear, nearest[vnear], min))
        distance[vnear] = -1

        for i in range(2, n + 1):
            if(W[i][vnear] < distance[i]):
                distance[i] = W[i][vnear]
                nearest[i] = vnear

    return F