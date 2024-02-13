# 박성원
'''https://www.acmicpc.net/problem/1086'''

import sys
from collections import deque

MAX_DIGIT = 50


def next_s(s, x):
    return s | (1 << x)

def bfs(s):
    queue = deque([s])
    visited[s] = 1
    
    while queue:
        u = queue.popleft()
        for x in range(N):
            if not (u & (1 << x)):
                n_s = next_s(u, x)
                for r in dp[u].keys():
                    n_r = ((r * digit_r[digits[x]]) % K + numbers_mod_r[x]) % K
                    if n_r not in dp[n_s]:
                        dp[n_s][n_r] = dp[u][r]
                    else:       
                        dp[n_s][n_r] += dp[u][r]
                if not visited[n_s]:
                    queue.append(n_s)
                    visited[n_s] = 1
            

def gcd(a, b):
    r = a % b
    while r:
        a, b = b, r
        r = a % b

    return b

    

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        numbers = [int(sys.stdin.readline()) for _ in range(N)]
        
        digits = list(map(lambda x :len(str(x)), numbers))
        K = int(sys.stdin.readline())
        numbers_mod_r = list(map(lambda x : x % K, numbers))
        
        S = 2 ** N - 1
        
        dp = [dict() for _ in range(S+1)]
        dp[0] = {0 : 1}
        digit_r = [1]
        
        visited = [0 for _ in range(S+1)]
        
        mod_10_K = 10 % K
        
        for _ in range(MAX_DIGIT):
            digit_r.append((digit_r[-1]*mod_10_K) % K)
        

        bfs(0)
        
        if 0 not in dp[S]:
            print("0/1")
        else:
            count_0 = dp[S][0]
            count_all = sum(dp[S].values())
            gcd_ = gcd(count_0, count_all)
            print(f"{count_0//gcd_}/{count_all//gcd_}")
        
    except ValueError or IndexError as e:
        print(e)