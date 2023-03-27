# DP (상) - 외판원 순회

import sys
input = sys.stdin.readline

# 현재 도시 pos에서 시작하여 방문하지 않은 모든 도시를 방문하는 최단 경로를 계산
def tsp(pos, visited):
    # 'visited' 비트마스크는 이미 방문한 도시를 추적하는 데 사용
    if visited == (1 << n) - 1:
        return w[pos][0] if w[pos][0] > 0 else INF

    if dp[pos][visited] != -1:
        return dp[pos][visited]

    dp[pos][visited] = INF
    for i in range(1, n):
        if not visited & (1 << i) and w[pos][i]:
            dp[pos][visited] = min(dp[pos][visited], tsp(i, visited | (1 << i)) + w[pos][i])

    return dp[pos][visited]

INF = float('inf')
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * (1 << n) for _ in range(n)]

print(tsp(0, 1))