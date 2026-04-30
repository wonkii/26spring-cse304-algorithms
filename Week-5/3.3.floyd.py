from typing import List

def floyd(n: int, W: List[List[int]]) -> List[List[int]]:
    D = W
    # Complete the code here
    for i in range(n):
        for k in range(n):
            for m in range(n):
                if(m == k):
                    continue
                D[k][m] = min(D[k][m], D[k][i] + D[i][m])
            
    return D
