# 트리의 지름
'''https://www.acmicpc.net/problem/1167'''

import sys
sys.setrecursionlimit(10**8)

def bfs(node):
    max_length = 0
    furthest_node = node
    visited[node] = 1
    for connected_node, weight in graph[node]:
        if not visited[connected_node]:    
            length, f_node = bfs(connected_node)
            length += weight
            if max_length < length:
                furthest_node = f_node
                max_length = length
            
    return max_length, furthest_node
        


try:
    V = int(sys.stdin.readline())
    graph = {node : [] for node in range(1,V+1)}
    
    for node in range(1, V+1):
        node_info = list(map(int, sys.stdin.readline().split(" ")))
        for idx in range(1,len(node_info)-1,2):
            graph[node_info[0]].append((node_info[idx], node_info[idx+1]))
    
    max_length = 0
    visited = [0 for _ in range(V+1)]
    l1, n1 = bfs(1)
    visited = [0 for _ in range(V+1)]
    l2, n2 = bfs(n1)
    
    print(l2)
    
    
except ValueError or IndexError as e:
    print(e)
