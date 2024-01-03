# 정점들의 거리
'''https://www.acmicpc.net/problem/1761'''

import sys
sys.setrecursionlimit(10**5)

def func(x):
    return int(x) - 1

def make_tree(node, d):
    depth[node] = d
    for new in graph[node]:
        if not depth[new]:
            parents[new] = node
            make_tree(new, d+1)
            
def lca(a, b):
    dist = 0
    
    if depth[a] > depth[b]:
        a, b = b, a
    
    while depth[a] < depth[b]:
        dist += graph[b][parents[b]]
        b = parents[b]
    
    while a != b:
        dist += graph[a][parents[a]] + graph[b][parents[b]]
        a, b = parents[a], parents[b]
    
    return dist
            
if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        graph = [dict() for _ in range(N)]
        for _ in range(N-1):
            x, y, d = map(func, sys.stdin.readline().split(" "))
            d += 1
            graph[y][x] = d
            graph[x][y] = d
            
        
        depth = [0 for _ in range(N)]
        parents = [0 for _ in range(N)]
        # visited = [0 for _ in range(N)]
        
        make_tree(0,1)
        
        M = int(sys.stdin.readline())
        
        for _ in range(M):
            a, b = map(func, sys.stdin.readline().split(" "))
            print(lca(a, b))
        
    except ValueError or IndexError as e:
        print(e)