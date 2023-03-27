# 그리디 (중) - 신입 사원

import sys

t = int(sys.stdin.readline())

def newRcrt():
    n = int(sys.stdin.readline())

    rcrt = [list(map(int, sys.stdin.readline().split()))  for _ in range(n)]

    p_sort = sorted(rcrt)
    top = 0
    result = 1

    for i in range(1, len(p_sort)):
        if p_sort[i][1] < p_sort[top][1]:
            top = i
            result += 1
    
    return(result)

for _ in range(t):
    print(newRcrt())

-----------

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    applicants = [0] * N
    hired = 0

    for i in range(N):
        first, second = map(int, input().split())
        applicants[i] = (first, second)
    
    applicants.sort()
    second_min = N+1

    for applicant in applicants:
        if applicant[1] < second_min:
            second_min = applicant[1]
            hired += 1
    
    print(hired)