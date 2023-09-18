# 치즈
'''https://www.acmicpc.net/problem/2638'''

import sys
from collections import deque

def print_graph():
    print()
    for i in range(N):
        for j in range(M):
            if not graph[i][j]:
                print(0, end=" ")
            else:
                print(experior[i][j], end=" ")
        print()
        
    print(queue)    

def inner_experior(s_x, s_y, count):
    queue_ex = deque([(s_x, s_y)])
    experior[s_y][s_x] = 1
    
    while queue_ex:
        u, v = queue_ex.popleft()
        for dx, dy in dx_dy:
            new_x, new_y = u + dx, v + dy
            if 0 <= new_x < M and 0 <= new_y < N:
                if graph[new_y][new_x]:
                    experior[new_y][new_x] += 1
                    if experior[new_y][new_x] == 2:
                        queue.append((new_x, new_y))
                        graph[new_y][new_x] = count + 1
                elif not experior[new_y][new_x]:
                    queue_ex.append((new_x, new_y))
                    experior[new_y][new_x] = 1
                

# queue -> 녹을 치즈들

dx_dy = [(-1,0),(0,-1),(1,0),(0,1)]

try:
    N, M = map(int, sys.stdin.readline().split(" "))
    graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    
    experior = [[0 for _ in range(M)] for _ in range(N)]
    
    queue = deque([(0,0)])
    experior[0][0] = 1
    while queue:
        u, v = queue.popleft()
        for dx, dy in dx_dy:
            new_x, new_y = u + dx, v + dy
            if 0 <= new_x < M and 0 <= new_y < N:
                if not experior[new_y][new_x] and not graph[new_y][new_x]:
                    experior[new_y][new_x] = 1
                    queue.append((new_x, new_y))
    
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                for dx, dy in dx_dy:
                    new_x, new_y = j + dx, i + dy
                    if 0 <= new_x < M and 0 <= new_y < N and not graph[new_y][new_x]: 
                        experior[i][j] += experior[new_y][new_x]
                        if experior[i][j] == 2:
                            queue.append((j,i))
                            break
            
    # print_graph()
    
    result = 0
    
    while queue:
        u, v = queue.popleft()
        
        # print(f"u = {u}, v = {v}")
        
        result = max(result, graph[v][u])
        
        for dx, dy in dx_dy:
            new_x, new_y = u + dx, v + dy
            if 0 <= new_x < M and 0 <= new_y < N:
                if graph[new_y][new_x]:
                    experior[new_y][new_x] += 1
                    if experior[new_y][new_x] == 2:
                        queue.append((new_x, new_y))
                        graph[new_y][new_x] = graph[v][u] + 1
                else:
                    if not experior[new_y][new_x]:
                        inner_experior(new_x, new_y, graph[v][u])
                
    print(result)        
    
except ValueError or IndexError as e:
    print(e)
    