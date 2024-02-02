# 스타트 택시
'''https://www.acmicpc.net/problem/19238'''

import sys
from collections import deque

X, Y, FUEL = 0,1,2
MIN_IDX = 2
EMPTY, WALL = 0, 1

dx_dy = [(0,-1), (-1,0), (1,0), (0,1)]

def search_passenger(sx, sy, fuel):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque([(sx,sy)])
    visited[sy][sx] = 1

    mx, my = -1, -1

    while queue:
        px, py = queue.popleft()

        if graph[py][px] >= MIN_IDX:
            mx, my = px, py
            break

        if visited[py][px] > fuel+1: # 승객이 있는지 없는 지 모르지만 연료가 부족한 경우
            return 0
        
        for dx, dy in dx_dy:
            nx, ny = px+dx, py+dy
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if not visited[ny][nx] and graph[ny][nx] != WALL:
                    visited[ny][nx] = visited[py][px] + 1
                    queue.append((nx,ny))

    while queue:
        px, py = queue.popleft()
        if visited[py][px] == visited[my][mx]:     
            if graph[py][px] >= MIN_IDX:
                if py < my:
                    mx, my = px, py
                
                elif py == my:
                    if px < mx:
                        mx, my = px, py
            
        else:
            break

    if mx == -1 and my == -1: # 연료는 충분하나 승객이 없는 경우
        return 0
    
    driver_info[X], driver_info[Y], driver_info[FUEL] = mx, my, fuel - visited[my][mx] +1
    
    return graph[my][mx]


def get_dist(destination_idx, sx, sy, fuel): 
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque([(sx,sy)])
    visited[sy][sx] = 1

    ex, ey = destinations[destination_idx]

    while queue:
        px, py = queue.popleft()

        if visited[py][px] >= fuel+1:
            return 0

        for dx, dy in dx_dy:
            nx, ny = px+dx, py+dy
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if nx == ex and ny == ey:
                    driver_info[X], driver_info[Y], driver_info[FUEL] = ex, ey, fuel - visited[py][px]
                    graph[sy][sx] = EMPTY
                    return visited[py][px]

                if not visited[ny][nx] and graph[ny][nx] != WALL:
                    visited[ny][nx] = visited[py][px] + 1
                    queue.append((nx,ny))
    
    return 0



if __name__ == "__main__":
    try:
        N, M, fuel = map(int, sys.stdin.readline().split(" "))

        graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

        destinations = dict()

        sy, sx = map(int, sys.stdin.readline().split(" "))

        for idx in range(M):
            start_y, start_x, end_y, end_x = map(int, sys.stdin.readline().split(" "))
            graph[start_y-1][start_x-1] = idx+2
            destinations[idx+2] = [end_x-1, end_y-1]

        driver_info = [sx-1, sy-1, fuel]

        while True:
            idx = search_passenger(*driver_info)
            if not idx:
                break

            dist = get_dist(idx, *driver_info)

            if not dist:
                break
            
            driver_info[FUEL] += dist*2

        for y in range(N):
            for x in range(N):
                if graph[y][x] >= MIN_IDX: # 승객을 찾지 못했는데 승객이 있으면.. 
                    driver_info[FUEL] = -1
        

        print(driver_info[FUEL])
                
    
    except ValueError or IndexError or TypeError as e:
        print(e)