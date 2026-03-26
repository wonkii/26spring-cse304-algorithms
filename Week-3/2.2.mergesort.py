from typing import List

def merge(h: int, m: int, U: List[int], V: List[int], S: List[int]) -> None:
    assert sorted(U) == U
    assert sorted(V) == V
    
    i = j = k = 0
    # Complete the code here
    while(i < h and j < m):
        if(U[i] < V[j]):
            S[k] = U[i]
            k += 1
            i += 1
        else:
            S[k] = V[j]
            k += 1
            j += 1
    
    while(i < h):
        S[k] = U[i]
        k += 1
        i += 1
    while(j < m):
        S[k] = V[j]
        k += 1
        j += 1


def mergesort(n: int, S: List[int]) -> None:
    h = n // 2 # h는 n을 2로 나눈 몫
    m = n - h # m은 n에서 h를 뺀 값
    U = []
    V = []
    if n > 1:
        # Complete the code here
        for i in S[:h]:
            U.append(i)
        for i in S[h:]:
            V.append(i)

        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)