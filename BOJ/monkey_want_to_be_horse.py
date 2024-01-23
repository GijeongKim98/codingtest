# 말이 되고픈 원숭이
'''https://www.acmicpc.net/problem/1600'''

import sys
from collections import deque

EMPTY, WALL = 0, 1
INF = 100000

MOVE_COUNT, K_COUNT = 0, 1

horse_dx_dy = [(-2,-1), (-1,-2), (1,-2), (2,-1), (-2,1), (-1,2), (1,2), (2,1)]
dx_dy = [(-1,0), (1,0), (0,1), (0,-1)]

def bfs(s_x, s_y):
    if s_x == W-1 and s_y == H-1:
        return 0
    queue = deque([(s_x, s_y, 0)])
    visited[s_y][s_x][MOVE_COUNT] = 1
    visited[s_y][s_x][K_COUNT] = 0
    
    while queue:
        px, py, pk = queue.popleft()
        if pk < K:
            npk = pk + 1
            for hdx, hdy in horse_dx_dy:
                hnx, hny = px + hdx, py + hdy
                if 0<=hnx and hnx<W and 0<=hny and hny<H and graph[hny][hnx] == EMPTY:
                    if hnx == W-1 and hny == H-1:
                        return visited[py][px][MOVE_COUNT]
                    
                    if visited[hny][hnx][K_COUNT] > npk:
                        visited[hny][hnx][MOVE_COUNT] = visited[py][px][MOVE_COUNT] + 1
                        visited[hny][hnx][K_COUNT] = npk
                        queue.append((hnx,hny,npk))

                    
                    
        for dx, dy in dx_dy:
            nx, ny = px+dx, py+dy
            if 0<=nx and nx<W and 0<=ny and ny<H and graph[ny][nx] == EMPTY:
                if nx == W-1 and ny == H-1:
                    return visited[py][px][MOVE_COUNT]
                
                if visited[ny][nx][K_COUNT] > pk:
                    visited[ny][nx][MOVE_COUNT] = visited[py][px][MOVE_COUNT] + 1
                    visited[ny][nx][K_COUNT] = pk
                    queue.append((nx,ny,pk))
    
    return -1
                

    
    

if __name__ == "__main__":
    try:
        K = int(sys.stdin.readline())
        W, H = map(int, sys.stdin.readline().rstrip().split(" "))
        graph = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for _ in range(H)]
        
        visited = [[[0, K+1] for _ in range(W)] for _ in range(H)]
        
        print(bfs(0,0))
    
    except ValueError or IndexError as e:
        print(e)
