import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()) # 지원자의 숫자
    score = [list(map(int, input().split())) for _ in range(n)]
    score.sort(lambda x: x[0])

    ans = 1
    facial = score[0][1]
    for i in range(1, n):
        if score[i][1] < facial:
            facial = score[i][1]
            ans += 1
    
    print(ans)