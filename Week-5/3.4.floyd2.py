from typing import List

def floyd2(n: int, W: List[List[int]]) -> List[List[int]]:
    P = [[-1] * (n) for _ in range(n)]
    D = W
    # Complete the code here
    for i in range(n):
        for k in range(n):
            for m in range(n):
                if(m == k):
                    continue
                D[k][m] = min(D[k][m], D[k][i] + D[i][m])
                P[k][m] = m
    
    return D, P

def path(i: int, j: int, P: list[list[int]]):
    k = P[i][j]
    if k != -1:
        path(i, k)
        print("v" + str(k), end = " ")
        path(k, j)