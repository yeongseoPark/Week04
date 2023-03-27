# DP (중) - 행렬 곱셈 순서 

# import sys

# def matrix_mlt(n, nums, memo):
#     if n in memo:
#         return memo[n]

#     if n == 1:
#         return 0

#     min_cost = float('inf')
#     for k in range(1, n):
#         left_part = matrix_mlt(k, nums[:k] + [nums[n]], memo)
#         right_part = matrix_mlt(n - k, [nums[0]] + nums[k:n], memo)
#         cost = left_part + right_part + nums[0] * nums[k] * nums[n]
#         min_cost = min(min_cost, cost)

#     memo[n] = min_cost
#     return min_cost

# n = int(sys.stdin.readline())
# nums = []
# for _ in range(n):
#     r, c = map(int, sys.stdin.readline().split())
#     if not nums:
#         nums.append(r)
#     nums.append(c)

# memo = {}
# result = matrix_mlt(n, nums, memo)
# print(result)


import sys

n = int(sys.stdin.readline())
nums = []
# 행렬만들고 
for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    if not nums:
        nums.append(r)
    nums.append(c)

def matrix_mlt(n, nums):
    #  모든 요소가 0으로 설정된 크기 (n+1) x (n+1)의 2D 테이블 dp를 초기화
    dp = [[0] * (n+1) for _ in range(n+1)] 
    #  0에서 n-1까지 행렬 인덱스(d) 간의 차이를 반복
    for d in range(n):
        # d에 대해 시작 행렬 인덱스(i)를 0부터 n-d-1까지 반복
        for i in range(n - d):
            # 종료 행렬 인덱스(j)를 i+d로 계산
            j = i + d
            # i가 j와 같으면 dp[i][j]를 0으로 설정
            if i == j:
                dp[i][j] = 0
            # 그렇지 않으면 dp[i][j]를 무한대로 설정
            else:
                dp[i][j] = float('inf')
                # i에서 j-1까지 중간 행렬 인덱스(k)를 반복
                for k in range(i, j):
                    # 행렬 i를 k로 곱하고 k+1을 j로 곱하는 비용을 계산하고 결과 행렬을 곱하는 비용을 더합니다.
                    # 현재 값과 계산된 비용의 최소값으로 dp[i][j] 업데이트
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + nums[i] * nums[k + 1] * nums[j + 1])

    return dp[0][n - 1]

print(matrix_mlt(n, nums))




# N = int(input())
# matrix = []
# for _ in range(N):
#     matrix.append(list(map(int, input().split())))
# dp =[[0 for _ in range(N)] for _ in range(N)] 


# for i in range(1, N): #몇 번째 대각선?
#     for j in range(0, N-i): #대각선에서 몇 번째 열?
    
#         if i == 1: #차이가 1밖에 나지 않는 칸
#             dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
#             continue
        
#         dp[j][j+i] = 2**32 #최댓값을 미리 넣어줌
#         for k in range(j, j+i): 
#             dp[j][j+i] = min(dp[j][j+i], 
#                              dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])
                
    
# print(dp[0][N-1]) #맨 오른쪽 위