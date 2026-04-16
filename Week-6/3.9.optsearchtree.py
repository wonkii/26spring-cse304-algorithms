from typing import Tuple

class Node:
    def __init__(self, key: int):
        self.key: int = key
        self.left: 'Node | None' = None
        self.right: 'Node | None' = None
    
    def preorder(self, path: list[int]) -> None:
        path.append(self.key)
        if self.left is not None:
            self.left.preorder(path)
        if self.right is not None:
            self.right.preorder(path)

    def inorder(self, path: list[int]) -> None:
        if self.left is not None:
            self.left.inorder(path)
        path.append(self.key)
        if self.right is not None:
            self.right.inorder(path)

def minimum(i: int, j: int, A: list[list[int]], p: list[int]) -> tuple[int, int]:
    minvalue, mink = INF, 0
    for k in range(i, j + 1):
        # Complete the code here
        if(minvalue > A[i][k-1] + A[k+1][j]):
            minvalue = A[i][k-1] + A[k+1][j]
            mink = k

            
    for m in range(i, j+1):
        minvalue += p[m]      
    return minvalue, mink

def optsearchtree(n: int, p: list[int]) -> tuple[int, list[list[int]], list[list[int]]]:
    A: list[list[int]] = [[INF] * (n + 1) for _ in range(n + 2)]
    R: list[list[int]] = [[0] * (n + 1) for _ in range(n + 2)]
    for i in range(1, n + 1):
        A[i][i - 1] = R[i][i - 1] = 0
        A[i][i], R[i][i] = p[i], i
    A[n + 1][n] = R[n + 1][n] = 0

    for diagonal in range(1, n):
        # Complete the code here
        # Tip. Implement minimum() and use it
        for idx in range(1, n - diagonal + 1):
            j = idx + diagonal
            A[idx][j], R[idx][j] = minimum(idx, j, A, p)

    return A[1][n], A, R

def tree(i: int, j: int, K: list[int], R: list[list[int]]) -> 'Node | None':
    k = R[i][j]
    if k == 0:
        return None
    else:
        # Complete the code here
        p = Node(k)
        p.left = tree(i, k - 1, K, R)
        p.right = tree(k + 1, j, K, R)
        return p

INF: float = float("inf")