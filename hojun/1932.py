import sys
input= sys.stdin.readline
n_triangle = int(input())
triangle = [[]]
for _ in range(n_triangle):
    triangle.append(list(map(int, input().split())))
print(triangle)

# dp테이블을 똑같이 만들기
dp = [[]]
if n_triangle == 1:
    print(triangle[1][0])

if n_triangle >= 2:
    dp.append([max(triangle[1])])
    dp.append([max(triangle[1])+ triangle[2][0], 
               max(triangle[1])+ triangle[2][1]])
    print(max(dp[2]))

# else:
#     for i in range(n_triangle)
