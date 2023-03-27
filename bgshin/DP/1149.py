# DP - RGB 거리

import sys

n = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

for i in range(1,n):

    house[i][0] += min(house[i-1][1],house[i-1][2])

    house[i][1] += min(house[i-1][0],house[i-1][2])    

    house[i][2] += min(house[i-1][1],house[i-1][0])   
                                   
print(min(house[-1]))