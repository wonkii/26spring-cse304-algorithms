# name: 장원준
# student id: 2022105489
from typing import List

def binsearch(n: int, S: List[int], x: int) -> int:
    low, high = 0, n - 1
    location = -1
    
    # Complete the code here
    while(low <= high):
        middle = (low + high) / 2
        if(S[int(middle)] == x):
            location = int(middle)
            break
        elif(S[int(middle)] > x):
            high = int(middle) - 1
        else:
            low = int(middle) + 1

    return location