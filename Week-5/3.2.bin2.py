import time

def bin2(n: int, k: int) -> int:
    B = [[0] * (k + 1) for _ in range(n + 1)]
    # Complete the code here
    
    for row in range(n + 1):
        for col in range(k + 1):
            if(row == col or col == 0):
                B[row][col] = 1
            else:
                B[row][col] = B[row-1][col] + B[row-1][col-1]
            
    return B[n][k]


