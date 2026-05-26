from typing import List

# Global variables
W: List[List[int]] = []     # Adjacency matrix
vcolor: List[int] = []      # Vertex colors
n: int = 0                  # Number of vertices
count: int = 0              # Solution counter

def promising(i: int) -> bool:
    global W, vcolor
    # Complete the code here
    j = 1
    while(j < i):
        if(W[i][j] and vcolor[i] == vcolor[j]):
            return False
        j+=1
   
    return True

def mcoloring(i: int, m: int) -> None:
    global n, vcolor, count
    if promising(i):
        if i == n:
            print(vcolor[1:])
            # Complete the code here
            count+=1
        else:
            # Complete the code here
            for c in range(1, m + 1):
                vcolor[i+1] = c
                mcoloring(i+1, m)


