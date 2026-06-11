from typing import Dict, Tuple

def knapsack(n: int, W: int, DP: Dict[Tuple[int, int], int]) -> int:
    global w, p
    if n == 0 or W <= 0:
        DP[(n, W)] = 0
    else:
        # Complete the code here
        if (n, W) not in DP:
            if w[n] > W:
                DP[(n, W)] = knapsack(n - 1, W, DP)
            else:
                e = knapsack(n - 1, W, DP)
                i = p[n] + knapsack(n - 1, W - w[n], DP)
                DP[(n, W)] = max(e, i)

    return DP[(n, W)]