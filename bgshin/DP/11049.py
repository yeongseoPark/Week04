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
for _ in range(n):
    r, c = map(int, sys.stdin.readline().split())
    if not nums:
        nums.append(r)
    nums.append(c)

def matrix_mlt(n, nums):
    dp = [[0] * (n+1) for _ in range(n+1)] 
     
    for d in range(n):
        for i in range(n - d):
            j = i + d
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + nums[i] * nums[k + 1] * nums[j + 1])

    return dp[0][n - 1]

result = matrix_mlt(n, nums)
print(result)


    