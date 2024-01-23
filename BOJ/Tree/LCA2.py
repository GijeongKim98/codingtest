# LCA2
'''https://www.acmicpc.net/problem/11438'''

# 이미 구한 값을 구하지 않는 DP를 사용 => 메모리 초과
'''
import sys
from collections import deque
sys.setrecursionlimit(10**6)

EMPTY = -1

def func(x):
    return int(x) - 1

def dfs(x, y):
    if x < y:
        x, y = y, x
        
    if dp[x][y] != EMPTY:
        return dp[x][y]
    
    if rank[x] < rank[y]:
        dp[x][y] = dfs(x, root[y])
    
    elif rank[x] > rank[y]:
        dp[x][y] = dfs(root[x], y)
    
    else:
        dp[x][y] = dfs(root[x], root[y])
    
    return dp[x][y]
    
    
        

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        
        graph = [[] for node in range(N)]
        
        for _ in range(N-1):
            x, y = map(func, sys.stdin.readline().split(" "))
            graph[x].append(y)
            graph[y].append(x)
            
        root = [node for node in range(N)]
        rank = [0 for _ in range(N)]
        dp = [[EMPTY for _ in range(i+1)] for i in range(N)]
        
        
        
        queue = deque([0])
        rank[0] = 1
        
        while queue:
            pop = queue.popleft()
            dp[pop][pop] = pop
            dp[pop][0] = 0
            for new in graph[pop]:
                if not rank[new]:
                    rank[new] = rank[pop] + 1
                    root[new] = pop
                    queue.append(new)
        
        answer = []
        M = int(sys.stdin.readline())
        
        for _ in range(M):
            x, y = map(func, sys.stdin.readline().split(" "))
            answer.append(dfs(x,y) + 1)
        
        
        print(*answer, sep="\n")            
        
    except ValueError or IndexError as e:
        print(e)
'''

# LCA2
'''https://www.acmicpc.net/problem/11438'''

# 점프를 좀더 높게 뛰어보자.

import sys

sys.setrecursionlimit(10**6)

C = 17 # 2 ^ 17  > 100,000 

def make_tree(node, d):
    depth[node] = d
    for new in graph[node]:
        if not visited[new]:
            parents[new][0] = node 
            visited[new] = 1
            make_tree(new, d+1)
            

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
        
    for i in range(C-1,-1,-1):
        if depth[b] - depth[a] >= (1 << i):
            b = parents[b][i]
            
    if a == b:
        return a
    
    for i in range(C-1, -1, -1):
        if parents[a][i] != parents[b][i]:
            a, b = parents[a][i], parents[b][i]
    
    return parents[a][0]
    
    

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        graph = [[] for _ in range(N+1)]
        
        for _ in range(N-1):
            x, y = map(int, sys.stdin.readline().split(" "))
            graph[x].append(y)
            graph[y].append(x)
        
        parents = [[0 for _ in range(C)] for _ in range(N+1)]
        depth = [0 for _ in range(N+1)]
        visited = [0 for _ in range(N+1)]
        
        # initialize tree : depth, parents
        visited[1] = 1
        make_tree(1,0)
            
        for i in range(1,C):
            for j in range(1, N+1):
                parents[j][i] = parents[parents[j][i-1]][i-1]
        
            
        M = int(sys.stdin.readline())
        
        for _ in range(M):
            a, b = map(int, sys.stdin.readline().split(" "))
            print(lca(a,b))
        
    except ValueError or IndexError as e:
        print(e)
