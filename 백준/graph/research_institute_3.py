# 연구소 3
'''https://www.acmicpc.net/problem/17142'''

import sys
from collections import deque
from itertools import combinations

EMPTY, WALL, VIRUS = 0, 1, 2
IMPOSSIBLE = 10000

dx_dy = [(-1,0), (0,-1), (1,0), (0,1)]

def bfs(activate_virus_idx):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    for idx in activate_virus_idx:
        x, y = virus_list[idx]
        visited[y][x] = 1
        queue.append((x,y))
    
    while queue:
        px, py = queue.popleft()
        for dx ,dy in dx_dy:
            nx, ny = px+dx, py+dy
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if not visited[ny][nx]: 
                    if graph[ny][nx] == WALL:
                        continue
                    queue.append((nx,ny))
                    visited[ny][nx] = visited[py][px] + 1
    
    max_ = 0    
    
    for y in range(N):
        for x in range(N):
            if graph[y][x] == EMPTY:
                if not visited[y][x]:
                    return IMPOSSIBLE
                else:
                    max_ = max(max_, visited[y][x]-1)
    
    return max_
        
    

if __name__ == "__main__":
    try:
        N, M = map(int, sys.stdin.readline().split(" "))
        graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
    
        # find location virus
        virus_list = []
        for i in range(N):
            for j in range(N):
                if graph[i][j] == VIRUS:
                    virus_list.append((j,i))
        
        answer = IMPOSSIBLE
        
        cases = combinations(list(range(len(virus_list))), M)
        
        for c in cases:
            answer = min(answer, bfs(c))
        
        print(answer if answer != IMPOSSIBLE else -1)
        
                
       
    except ValueError or IndexError as e:
        print(e)