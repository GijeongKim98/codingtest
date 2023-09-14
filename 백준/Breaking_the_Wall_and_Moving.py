# 벽 부시고 이동하기
'''https://acmicpc.net/problem/2206'''
# method1 시간초과
'''
import sys
from collections import deque

dx_dy = [(-1,0), (0,-1), (1,0), (0,1)]

def bfs(s_x, s_y):
    visited = [[0 for _ in range(M)] for __ in range(N)]
    visited[s_x][s_y] = 1
    queue = deque([(s_x, s_y)])
    
    while queue:
        u, v = queue.popleft()
        for dx, dy in dx_dy:
            new_x, new_y = u + dx, v + dy
            
            if new_x == M-1 and new_y == N-1:
                return visited[v][u] + 1
            
            if 0 <= new_x and new_x < M and 0 <= new_y and new_y < N:    
                if not visited[new_y][new_x] and not graph[new_y][new_x]:
                    visited[new_y][new_x] = visited[v][u] + 1
                    queue.append((new_x, new_y))
    
    return 0    

try:
    N, M = map(int, sys.stdin.readline().split(" "))
    graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
    
    # print(N, M)
    # print(graph)
    result = 0
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                graph[i][j] = 0
                dist = bfs(0, 0)
                graph[i][j] = 1
                
                if dist and (not result or dist < result):
                    result = dist
    
    print(-1 if not result else result) 
                
    
    
except ValueError or IndexError as e:
    print(e)
    
'''
# 벽 부시고 이동하기
'''https://acmicpc.net/problem/2206'''

import sys
from collections import deque

dx_dy = [(-1,0), (0,-1), (1,0), (0,1)]

def bfs(s_x, s_y):
    visited = [[[0]*2 for _ in range(M)] for __ in range(N)]
    visited[s_x][s_y][0] = 1
    queue = deque([(s_x, s_y, 0)])
    
    while queue:
        u, v, c = queue.popleft()
        for dx, dy in dx_dy:
            new_x, new_y = u + dx, v + dy
            
            if new_x == M-1 and new_y == N-1:
                return visited[v][u][c] + 1
            
            if 0 <= new_x and new_x < M and 0 <= new_y and new_y < N:
                
                if not c and graph[new_y][new_x]:
                    visited[new_y][new_x][1] = visited[v][u][c] + 1
                    queue.append((new_x, new_y, 1)) 
                    
                if not visited[new_y][new_x][c] and not graph[new_y][new_x]:
                    visited[new_y][new_x][c] = visited[v][u][c] + 1
                    queue.append((new_x, new_y, c))
    
    return -1    
try:
    N, M = map(int, sys.stdin.readline().split(" "))
    graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
    if N == 1 and M == 1:
        print(1)
    else:
        result = bfs(0,0)
        print(result)
    

except ValueError or IndexError as e:
    print(e)