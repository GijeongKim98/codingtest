# 트리의 지름
'''https://www.acmicpc.net/problem/1967'''

import sys
sys.setrecursionlimit(10**8)


def dfs(node):
    visited[node] = 1
    max_dist, max_node = 0, node
    
    for new_node in graph[node]:
        if not visited[new_node]:
            f_d, f_n = dfs(new_node)
            f_d += graph[node][new_node]
            if max_dist < f_d:
                max_dist, max_node = f_d, f_n
        
    return max_dist, max_node
        
    
try:
    n = int(sys.stdin.readline())
    
    graph = {i : dict() for i in range(1,n+1)}
    
    for _ in range(n-1):
        p, c, w = map(int, sys.stdin.readline().split(" "))
        graph[p][c] = w
        graph[c][p] = w

    visited = [0 for _ in range(n+1)]
    dist, node = dfs(1)
    
    visited = [0 for _ in range(n+1)]
    result, _ = dfs(node)
    
    print(result)
        
except ValueError or IndexError as e:
    print(e)
    