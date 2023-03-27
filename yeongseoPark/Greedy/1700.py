import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 구멍개수, 사용횟수
sequence = list(map(int, input().split()))

concent = set()
ans = 0
# 뭘 뽑느냐가 중요
for i in range(k):
    cur = sequence[i]
    if len(concent) == n:
        if cur not in concent:
            removed = False
            for j in concent: # 일단 현재기준으로 뒤에 다시 쓸일 없는 애 뽑는게 최우선
                if j not in sequence[i:]:
                    concent.remove(j)
                    removed = True
                    break
            if not removed: # 뒤에 다시 쓸일 없는 애가 없으면, 최대한 늦게 사용하는 애 뽑아줘야 함 
                max_j = -1
                max_idx = -1
                for j in concent:
                    if sequence[i:].index(j) > max_idx:
                        max_j = j
                        max_idx = sequence[i:].index(j)
                concent.remove(max_j)
            
            ans += 1
    
    concent.add(cur)

print(ans)
