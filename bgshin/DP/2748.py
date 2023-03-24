# DP (하) - 피보나치 수 2

import sys

def fib(n, memo):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] != -1:
        return memo[n]
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def fib_dp(n):
    # memo라는 리스트를 생성 리스트 크기 n+1 
    # 모든 값 -1로 초기화
    memo = [-1] * (n+1)
    # fib 호출 n번째 피보나치 수열을 구함
    return fib(n, memo)

n = int(sys.stdin.readline())

print(fib_dp(n))