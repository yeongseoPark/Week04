import sys, collections


N = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))
for _ in range(N-1):
    size.append(int(sys.stdin.readline().strip().split()[-1]))
print(N)
print(size)
matrix_num = len(size) - 1
dp = [[0]*len(size) for _ in range(len(size))]
print(dp)

if matrix_num == 1:
    print(0)
else:
    for j in range(2, matrix_num+1):
        print('LOOP J ', j)
        for i in range(1, matrix_num+2-j):
            print('LOOP i', i)
            dp[i][j] = min(dp[i][j-k] + dp[i+j-k][k] + size[i-1] * size[i+j-k-1] * size[i+j-1] for k in range(1, j))
            a = [dp[i][j-k] + dp[i+j-k][k] + size[i-1] * size[i+j-k-1] * size[i+j-1] for k in range(1, j)]
            print(a)

print(dp[1][N])