# DP - 2xn 타일링

import sys

def tile(n):
    
    a = [0] * (n+2)
    
    a[1] = 1
    a[2] = 2


    for i in range(3, n+1):
         a[i] = (a[i-1] + a[i-2]) % 10007

    return a[n]     

n = int(sys.stdin.readline())

print(tile(n))