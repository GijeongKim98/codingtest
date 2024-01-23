# 백준 : 21736 헌내기는 친구가 필요해
'''https://www.acmicpc.net/problem/21736'''

import sys
from collections import deque

try:
    dx_dy = [(1,0), (0,1), (0,-1), (-1,0)]
    
    def bfs(start_node):
        
        global result
        
        u, v = start_node
        visited[v][u] = 1
        queue = deque([(u,v)])
        
        while queue:
            x, y  = queue.popleft()
            for dx, dy in dx_dy:
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x and new_x < M and  0 <= new_y and new_y < N:
                    if not visited[new_y][new_x]:  
                        if graph[new_y][new_x] == "O":
                            visited[new_y][new_x] = 1
                            queue.append((new_x, new_y))
                        elif graph[new_y][new_x] == "P":
                            visited[new_y][new_x] = 1
                            queue.append((new_x, new_y))
                            result += 1
                            
        
    
    N, M = map(int, sys.stdin.readline().split(' '))
    graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
    
    start_node = None
    break_count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "I":
                start_node = j, i
                break_count = 1
                break
        if break_count:
            break

    visited = [[0 for _ in range(M)] for __ in range(N)]
    
    result = 0
    bfs(start_node)
    if result:
        print(result)
    else:
        print("TT")

except ValueError or IndexError as e:
    print(e)