# 게임
"""https://www.acmicpc.net/problem/1103"""

"""
import sys
from collections import deque

dx_dy = [(-1,0), (0,-1), (1,0), (0,1)]

def dfs(step):
    global max_time
    max_time = max(max_time, step)
    x, y = stack[-1]
    X = graph[y][x]
    for dx, dy in dx_dy:
        new_x, new_y = x + dx * X, y + dy * X
        if 0 <= new_x < M and 0 <= new_y < N and graph[new_y][new_x]:
            if (new_x, new_y) in stack:
                max_time = -1
                return -1
            stack.append((new_x, new_y))
            fun_r = dfs(step + 1) 
            stack.pop()
            if fun_r == -1:
                return -1
            
             

def bfs(s_x, s_y):
    queue = deque([(s_x, s_y)])
    visited[s_y][s_x] = 1
    max_time = 1
    
    while queue:
        u, v = queue.popleft()
        X = graph[v][u]
        max_time = max(max_time, visited[v][u])
        if not X:
            continue
        for dx, dy in dx_dy:
            new_x, new_y = u + dx * X, v + dy* X
            if 0 <= new_x < M and 0 <= new_y < N and graph[new_y][new_x]:
                if visited[new_y][new_x]:
                    return -1
                else:
                    queue.append((new_x, new_y))
                    visited[new_y][new_x] = visited[v][u] + 1
    
    return max_time
            

def func(x):
    return int(x) if x.isnumeric() else 0
    

try:
    N, M = map(int, sys.stdin.readline().split(" "))
    graph = [list(map(func, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    max_time = 1
    stack = [(0,0)]
    # result = bfs(0,0)
    dfs(1)
    print(max_time)
    

except ValueError or IndexError as e:
    print(e)
    
"""
    

# 게임
"""https://www.acmicpc.net/problem/1103"""

import sys
sys.setrecursionlimit(10 ** 6)

dx_dy = [(-1,0), (0,-1), (1,0), (0,1)]

def dfs(step):
    # dp_arr에 넣고 싶은 것은 해당 점에서 몇 스탭을 더 갈 수 있을지 남기고 싶음 다시 조사 안하도록
    # 처음 과정에서 dp_arr의 값이 있다면 그 점은 방문한 점 이므로 최대의 값을 return
    # 만약 stack에 있는 점을 다시 방문 가능하다면 -1을 return하고 상황을 종료
    x, y = stack[-1]
    X = graph[y][x]
    max_step = step
    
    if dp_arr[y][x]:
        return step + dp_arr[y][x]
    
    
    for dx, dy in dx_dy:
        new_x, new_y = x+dx*X, y+dy*X
        if 0 <= new_x and new_x < M and 0 <= new_y and new_y < N and graph[new_y][new_x]:
            
            if (new_x, new_y) in stack:
                return -1
            
            stack.append((new_x, new_y))
            
            k = dfs(step+1)
            
            if k == -1:
                return -1
            
            max_step = max(max_step, k)
            
            stack.pop()

    dp_arr[y][x] = max_step - step
    
    return max_step
    
    
def func(x):
    return int(x) if x.isnumeric() else 0
    

try:
    N, M = map(int, sys.stdin.readline().split(" "))
    graph = [list(map(func, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
    
    # 해당 점에서 몇 스탭을 더 갈 수 있는지 조사
    dp_arr = [[0 for _ in range(M)] for _ in range(N)]
    
    stack = [(0,0)]
    
    print(dfs(1))
    

except ValueError or IndexError as e:
    print(e)