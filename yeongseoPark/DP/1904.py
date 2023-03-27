n = int(input())

def count(n):
    if n == 1:
        print(1)
        return
    elif n == 2:
        print(2)
        return
    
    dp = [1, 2]
    for i in range(n-2):
        dp[0], dp[1] = dp[1], dp[0]
        # 모듈러 법칙 쓰지 않으면 숫자가 커져서 시간초과 발생
        dp[1] = ((dp[0] % 15746) + (dp[1] % 15746)) % 15746 
    
    print(dp[1]) 

count(n)