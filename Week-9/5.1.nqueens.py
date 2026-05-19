from typing import List

def promising(i: int, n: int, col: List[int]) -> bool:
    is_promising = True
    # Complete the code here
    for j in range(1, i):
        if(is_promising):
            if(col[i] == col[j] or abs(col[i] - col[j]) == i-j):
                is_promising = False
                j += 1

    return is_promising

def nqueens(i: int, n: int, col: List[int]) -> None:
    if promising(i, n, col):
        if i == n:
            print("found=", col[1:])
        else:
            # Complete the code here
            for j in range(1, n+1):
                col[i+1] = j
                nqueens(i+1, n, col)
                
