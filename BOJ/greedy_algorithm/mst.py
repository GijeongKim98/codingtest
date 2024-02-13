# 백준 1197 최소 스패닝 트리
"""https://www.acmicpc.net/problem/1197"""

import sys

try:
    def find(x):
        if x == root[x]:
            return x
        else:
            root[x] = find(root[x])
            return root[x]
    
    def union(x, y, w):
        x = find(x)
        y = find(y)
        
        if x == y:
            return 0
        
        if rank[x] < rank[y]:
            root[x] = y
        else:
            root[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        return w
    V,E = map(int, sys.stdin.readline().split(" "))
    edge_list = [list(map(int, sys.stdin.readline().split(" ")))
                 for _ in range(E)]
    
    
    edge_sort_list = sorted(edge_list, key=lambda x : x[2])
    
    sum_of_weight = 0
    not_visited_count = V
    
    root = [i for i in range(V+1)]
    rank = [0] * (V+1)
    
    for x,y,w in edge_sort_list:
        sum_of_weight += union(x,y,w)
    
    print(sum_of_weight)
    
except ValueError or IndexError as e:
    print(e)
