# 그리디 (하) - 동전 0

import sys

n,k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

cnt = 0
for i in coins[::-1]:
    if k < i:
        continue
    else:
        while k >= i:
            s,r = divmod(k,i)
            cnt += s
            k = r 
            if k == 0:
                print(cnt)
                break

