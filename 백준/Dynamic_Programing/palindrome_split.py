# 팰린드롬 분할
"""https://www.acmicpc.net/problem/1509"""

import sys

try:
    s = sys.stdin.readline().rstrip()
    n = len(s) # length of s
    
    p = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        p[i][i] = 1
        if i < n-1 and s[i] == s[i+1]:
            p[i][i+1] = 1
    
    # n = 4
    for i in range(n-1,-1,-1): # 3,     2,     1,    0
        for j in range(i+2,n): # x      x      3     2,3
            if s[i] == s[j] and p[i+1][j-1]:
                p[i][j] = 1

    
    # for p_ in p:
    #     print(p_)
        
    dp = [n for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    
    for end in range(1,n+1): # 0         # 1        # 2
        for start in range(1,end+1): # 0     # 0        # 0 1
            if p[start-1][end-1]:
                dp[end] = min(dp[end], dp[start-1] + 1)
    
    print(dp[n])
    
except ValueError or IndexError as e:
    print(e)