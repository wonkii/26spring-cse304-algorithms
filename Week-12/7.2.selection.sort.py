from typing import List

def selectionsort(n: int, S: List[int]) -> None:
    for i in range(0, n):
        smallest = i
        for j in range(i+1, n):
            if S[j] < S[smallest]:
                smallest = j
        x = S[i]
        S[i] = S[smallest]
        S[smallest] = x