# 플로이드
"""https://www.acmicpc.net/problem/11404"""

import sys

INF = 100000000

try:
    n, m = [int(sys.stdin.readline()) for _ in range(2)]
    dist = [[0 if i==j else INF for i in range(n)] for j in range(n)]
    
    for _ in range(m):
        s, e, c = map(int, sys.stdin.readline().split(" "))
        dist[s-1][e-1] = min(dist[s-1][e-1], c)
    
    
    for k in range(n):
        for i in range(n):
            if i == k : continue
            for j in range(n):
                if j == k or j == i : continue
                
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    
    for row in dist:
        for i in range(n):
            if row[i] == INF:
                row[i] = 0
        print(*row)
    
    
except ValueError or IndexError as e:
    print(e)