# DP - 파도반 수열

import sys

def wave(n):
    
    a = [0] * (n+3)
    
    a[1] = 1
    a[2] = 1
    a[3] = 1
    for i in range(4, n+1):
         a[i] = (a[i-2] + a[i-3])

    return a[n]     

t = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(t)]

for i in lst: 
    print(wave(i))