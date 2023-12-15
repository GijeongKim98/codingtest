# 팰린드롬?
'''https://www.acmicpc.net/problem/10942'''

import sys

def func(x):
    return int(x) - 1

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        numbers = list(map(int, sys.stdin.readline().split(" ")))

        M = int(sys.stdin.readline())
        questions = [tuple(map(func, sys.stdin.readline().split(" "))) for _ in range(M)]
        
        dp = [[False for i in range(N)] for j in range(N)]        
        
        for i in range(N):
            dp[i][i] = True
            if i > 0 and numbers[i-1] == numbers[i]:
                dp[i-1][i] = True
                
        # print(f'INIT DP')
        # print(*dp , sep="\n", end="\n\n")
    
        
        
        for dif in range(2,N):
            for idx in range(N-dif):
                i, j = idx, idx+dif
                if dp[i+1][j-1] and numbers[i] == numbers[j]:
                    dp[i][j] = True
        
        # print(f'Complete making DP')
        # print(*dp , sep="\n", end="\n\n")
    
        
        answer = []
        
        for s, e in questions:
            answer.append((1 if dp[s][e] else 0))
        
        print(*answer, sep="\n")
            
    except ValueError or IndexError as e:
        print(e)