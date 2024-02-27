# 산 모양 타일링

# 중점 끝나는 모양이 삼각형인지 사다리꼴인지 체크

T, Q = 0, 1 # 삼각형으로 끝나는지 사다리꼴로 끝나는지

CONST = 10007

def solution(n,tops):
    
    dp = [[0,0] for _ in range(n+1)]
    dp[0][T], dp[0][Q] = 1, 0
    
    for i in range(1,n+1):
        if tops[i-1]:
            dp[i][T] = ((dp[i-1][T] * 3) % CONST + (dp[i-1][Q] * 2) % CONST) % CONST
            dp[i][Q] = (dp[i-1][T] + dp[i-1][Q]) % CONST
        else:
            dp[i][T] = ((dp[i-1][T] * 2) % CONST + dp[i-1][Q]) % CONST
            dp[i][Q] = (dp[i-1][T] + dp[i-1][Q]) % CONST
        
    
    answer = (dp[n][T] + dp[n][Q]) % CONST
    return answer


if __name__ == "__main__":
    n, tops = 4, [1,1,0,1]
    n, tops = 2, [0,1]
    n, tops = 10, [0 for _ in range(10)]
    ans = solution(n,tops)
    print(ans)