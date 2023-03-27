import sys
input = sys.stdin.readline

n = int(input())

meet = [list(map(int, input().split())) for _ in range(n)]

meet.sort(lambda x: (x[1], x[0])) # 빨리끝나는 순으로 정렬, 끝나는 시간이 같다면 빨리 시작하는 순서대로 정렬 

ans = end = 0
for start, fin in meet:
    if start >= end:
        ans += 1
        end = fin

print(ans)
