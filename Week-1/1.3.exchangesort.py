from typing import List

def exchangesort(n: int, S: List[int]) -> None:
    # Complete the code here
    if n <= 0:
        return
    while(True):
        biggest = -9999 
        bigidx = -1
        for i in range (0, n):
            if S[i] > biggest:
                biggest = S[i]
                bigidx = i
        S[bigidx] = S[n-1]
        S[n-1] = biggest
        n = n-1
        if n<1: 
            break


# n = 5라고 가정 : 
# biggest, bigidx 초기화

# for문으로 0부터 n -1번까지 돌림 
# S[0] ~ S[4]중에 가장 큰 수 biggest 저장
# 가장 큰수의 차례 일때 i는 bigidx에 저장

# for문 이후 biggest는 n-1번 요소와 위치 이동
# 이 일을 n-1번 전체적으로 반복




        