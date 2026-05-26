from heapq import heappush, heappop
from typing import List

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = 0

def boundof(u: Node, n: int, W: float, w: List[float], p: List[float]) -> float:
    if u.weight >= W:
        return 0
    else:
        # Complete the code here
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while(j <= n and totweight + w[j] <= W):
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if(k <= n):
            result += (W-totweight)* p[k] / w[k]

        return result

def knapsack3(n: int, W: float, w: List[float], p: List[float]) -> float:
    count = 0
    heap = [] # Initialize Priority Queue
    v = Node(0, 0, 0)
    v.bound = boundof(v, n, W, w, p)
    maxprofit = 0
    heappush(heap, (-v.bound, v))
    count +=1
    while len(heap) != 0:
        # Complete the code here
        v = heappop(heap)[1]
        count -= 1

        if v.bound > maxprofit:
            u1 = Node(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1])
            if(u1.weight <= W and u1.profit > maxprofit):
                maxprofit = u1.profit
            
            u1.bound = boundof(u1, n, W, w, p)
            if(u1.bound > maxprofit):
                heappush(heap, (-u1.bound, u1))
                count += 1
            
            u2 = Node(v.level + 1, v.weight, v.profit)
            u2.bound = boundof(u2, n, W, w, p)

            if(u2.bound > maxprofit):
                heappush(heap, (-u2.bound, u2))
                count += 1
    return maxprofit
