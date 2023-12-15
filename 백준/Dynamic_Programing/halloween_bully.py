# 할로윈의 양아치
'''https://www.acmicpc.net/problem/20303'''
'''
import sys
from collections import deque

def func(x):
    return int(x) - 1

def bfs(start):
    visited[start] = True
    queue = deque([start])
    
    number_of_child, number_of_candy = 0, 0
    
    while queue:
        u = queue.popleft()
        number_of_child += 1 
        number_of_candy += candy_info[u]
        
        for new in graph[u]:
            if not visited[new]:
                visited[new] = True
                queue.append(new)
    
    return number_of_child, number_of_candy 
    
        

if __name__ == "__main__":
    try:
        N, M, K = map(int, sys.stdin.readline().split(" "))

        candy_info = list(map(int, sys.stdin.readline().split(" ")))
        
        relations = [tuple(map(func, sys.stdin.readline().split(" "))) for _ in range(M)]
        
        graph = {i: [] for i in range(N)}
        
        for x, y in relations:
            graph[x].append(y)
            graph[y].append(x)
            
        
        visited = [False for _ in range(N)]
        
        group_info_list = []
        
        for child in range(N):
            if not visited[child]:
                group_info = bfs(child)
                group_info_list.append(group_info)
        
        len_of_groups = len(group_info_list)
        
        dp = [[0 for _ in range(K)] for _ in range(len_of_groups+1)]
        
        for idx, (weight, value) in enumerate(group_info_list, start=1):
            for k in range(1, K):
                dp[idx][k] = dp[idx-1][k]
                if k >= weight:
                    dp[idx][k] = max(dp[idx][k], dp[idx-1][k-weight] + value)
                    
        print(dp[-1][-1])
                
        
    except ValueError or IndexError as e:
        print(e)
'''

# Method 2 : union_find 

import sys

def func(x):
    return int(x) - 1

def find(x):
    if x == root[x]:
        return x
    root[x] = find(root[x])
    
    return root[x]

def union(x,y):
    x, y = find(x), find(y)
    
    if x == y:
        return

    if rank[x] < rank[y]:
        x, y = y, x
    
    root[y] = x
    rank[x] += rank[y]
    candys[x] += candys[y]

if __name__ == "__main__":
    try:
        N, M, K = map(int, sys.stdin.readline().split(" "))
        candys = list(map(int, sys.stdin.readline().split(" ")))
        relations = [tuple(map(func, sys.stdin.readline().split(" "))) for _ in range(M)]
        
        root = [child for child in range(N)]
        rank = [1 for _ in range(N)]
        
        for x, y in relations:
            union(x,y)
            
        groups = []
            
        for child in range(N):
            if child == root[child]:
                groups.append((rank[child], candys[child]))
        
        dp = [[0 for _ in range(K)] for _ in range(len(groups)+1)]
        
        for idx, (w, v) in enumerate(groups, start=1):
            for k in range(1,K):
                dp[idx][k] = dp[idx-1][k]
                if k >= w:
                    dp[idx][k] = max(dp[idx][k], dp[idx-1][k-w]+v)
        
        
        print(dp[-1][-1])
                    
    
    except ValueError or IndexError as e:
        print(e)

 