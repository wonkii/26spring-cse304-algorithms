from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int: 
    location = 0
    
    for i in S:
        if i == x:
            return location
        location = location + 1

    location = -1
    # Complete the code here
    return location