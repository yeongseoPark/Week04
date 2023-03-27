import sys
input = sys.stdin.readline

n , m = map(int, input().split())

dp = [[sys.maxsize] * (int((2*n) ** 0.5) + 2) for _ in range(n+1)]
# int((2*n) ** 0.5) 이 속도가 끊임없이 증가하며 점프할때 n 도달시의 속도 근사값
# 근데 왜 + 1 함?? -> 마지막 속도에서 +1 하는것 고려
dp[1][0] = 0

stone = set()
for _ in range(m):
    stone.add(int(input()))

for i in range(2, n+1):
    if i in stone:
        continue
    for j in range(1, int((2*n) ** 0.5) + 1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1
    
if min(dp[n]) == sys.maxsize:
    print(-1)
else:
    print(min(dp[n]))

