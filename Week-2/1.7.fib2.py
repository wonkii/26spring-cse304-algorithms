# name: 장원준
# student id: 2022105489
def fib2(n: int) -> int:
    f = [0] * (n + 1)
    # Complete the code here

    f[0] = 0
    if(n > 0):
        f[1] = 1
        for i in range (n+1):
            if(i > 1):
                f[i] = f[i-1] + f[i-2]

    return f[n]