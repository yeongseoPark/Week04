"""
점화식
g(i, s) = min(Cost[i->k] + g(k, s - {k}))
k는 s집합에 속한 값

재귀를 통해 풀어보려 했으나, 메모이제이션을 사용하지 않아서 중복된 부분 문제를 모두 계산 
-> 뭔말인지 모르겠음
"""

# import sys
# input = sys.stdin.readline

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]

# def tsp_recur(start, vertices):
#     if len(vertices) == 0:
#         return graph[start][0] # 0으로 돌아오게

#     minVal = sys.maxsize
#     for i in vertices:
#         minVal = min(minVal, graph[start][i] + tsp_recur(i, vertices - {i}))

#     return minVal

# print(tsp_recur(0, set([i for i in range(1, n)])))


import sys

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# DP 배열 초기화
dp = [[-1] * n for _ in range(n)]

# start에서 시작하여 path 도시를 순회하고, 마지막으로 end 도시를 방문하는 경로의 최소 비용을 반환
def tsp_dp(start, end, path):
    # path에 도시가 포함되어 있지 않은 경우, 직접 이동하여 비용 계산
    if not path:
        return graph[start][end]

    # 이미 계산한 적이 있는 경우, 해당 결과 반환
    if dp[start][path[0]] != -1:
        return dp[start][path[0]]

    # 최소 비용 계산
    result = sys.maxsize
    for i in range(len(path)):
        next_city = path[i]
        rest = path[:i] + path[i+1:]
        result = min(result, graph[start][next_city] + tsp_dp(next_city, end, rest))

    # 계산 결과를 DP 배열에 저장하고 반환
    dp[start][path[0]] = result
    return result

# 시작 도시는 0번째 도시로 가정하여 계산
path = [i for i in range(1, n)]
print(tsp_dp(0, 0, path))
