import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin = [int(input()) for _ in range(n)]

val = 0
cnt = 0

while val <= k:
    for i in range(n-1, -1, -1):
        if coin[i] + val < k:
            cnt += 1
            val += coin[i]
            break
        elif coin[i] + val == k:
            print(cnt + 1)
            exit()
        else:
            continue

            