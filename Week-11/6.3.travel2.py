from heapq import heappush, heappop
from typing import List, Tuple
import time

INF = float("inf")

class Node:
    def __init__(self, level, path):
        self.level = level
        self.path = path[:]
        self.bound = 0

def remainder(path: List[int], n: int) -> int:
    return n * (n + 1) // 2 - sum(path)

def pathlength(path: List[int], W: List[List[float]]) -> float:
    # Complete the code here
    length = 0
    for i in range(len(path) - 1):
        length += W[path[i]][path[i+1]]

    return length

def hasOutgoing(v: int, path: List[int]) -> bool:
    return v in path[:len(path)-1]

def hasIncoming(v: int, path: List[int]) -> bool:
    return v in path[1:]

def boundof(v: Node, n: int, W: List[List[float]]) -> float:
    global INF
    lower = pathlength(v.path, W)
    for i in range(1, n + 1):
        # Complete the code here
        if(hasOutgoing(i, v.path)):
            continue

        minimun = INF
        for j in range(1, n + 1):
            if(i==j): continue
            if(j==1 and i==v.path[v.level]): continue

            if(hasIncoming(j, v.path)): continue

            minimun = min(minimun, W[i][j])
        lower += minimun

    return lower

def travel2(n: int, W: List[List[float]]) -> Tuple[float, List[int]]:
    global INF
    heap = [] # Initialize Priority Queue
    v = Node(0, [1])
    v.bound = boundof(v, n, W)
    minlength, opttour = INF, []
    heappush(heap, (v.bound, time.time(), v))

    while len(heap) != 0:
        v = heappop(heap)[2]
        if v.bound < minlength:
            for i in range(2, n + 1):
                # Complete the code here
                if i in v.path:
                    continue

                u = Node(v.level + 1, v.path + [i])
                if(u.level == n-2):
                    u.level += 1
                    u.path.append(remainder(u.path, n))
                    u.path.append(1)
                    length = pathlength(u.path, W)
                    if(length < minlength):
                        minlength = length
                        opttour = u.path[:]
                else:
                    u.bound = boundof(u, n, W)
                    if(u.bound < minlength):
                        heappush(heap, (u.bound, time.time(), u))

                
    return minlength, opttour
