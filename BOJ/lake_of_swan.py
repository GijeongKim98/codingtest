# 백조의 호수
'''https://www.acmicpc.net/problem/3197'''

import sys
from collections import deque

LAKE = ord(".")
ICE = ord("X")
SWAN = ord("L")

dx_dy = [(-1,0),(0,-1),(1,0),(0,1)]

def bfs(sx,sy,idx):
    visited[sy][sx] = idx
    queue = deque([(sx,sy)])

    while queue:
        px, py = queue.popleft()
        temp = False
        for dx, dy in dx_dy:
            nx, ny = px+dx, py+dy
            if 0 <= nx and nx < C and 0 <= ny and ny < R:
                if not visited[ny][nx]:
                    if graph[ny][nx] != ICE:
                        visited[ny][nx] = idx
                        queue.append((nx,ny))

                    else:
                        temp = True

        if temp:
            start_nodes.append((px, py))

def find(x):
    if x == root[x]:
        return x
    
    root[x] = find(root[x])

    return root[x]

def union(x, y):
    x, y = find(x), find(y)

    if x == y:
        return 
    
    if rank[x] < rank[y]:
        x, y = y, x

    root[y] = x

    if rank[x] == rank[y]:
        rank[x] + 1

    return



if __name__ == "__main__":
    try:
        R, C = map(int, sys.stdin.readline().split(" "))

        graph = [list(map(ord, list(sys.stdin.readline().rstrip()))) for _ in range(R)]

        the_number_of_lake = 1

        visited = [[0 for _ in range(C)] for _ in range(R)]
        dist = [[0 for _ in range(C)] for _ in range(R)]

        start_nodes = []

        swans = []

        for y in range(R):
            for x in range(C):
                if not visited[y][x] and graph[y][x] != ICE:
                    bfs(x,y,the_number_of_lake)
                    the_number_of_lake += 1

                if graph[y][x] == SWAN:
                    swans.append(visited[y][x])
                    graph[y][x] = LAKE
        

        root = [idx for idx in range(the_number_of_lake)]
        rank = [0 for idx in range(the_number_of_lake)]

        queue = deque(start_nodes)
        answer = 0

        if swans[0] != swans[1]:
            while queue:
                px, py = queue.popleft()
                for dx, dy in dx_dy:
                    nx, ny = px+dx, py+dy
                    if 0 <= nx and nx < C and 0 <= ny and ny < R:
                        if graph[ny][nx] == ICE:
                            graph[ny][nx] = LAKE
                            visited[ny][nx], dist[ny][nx] = visited[py][px], dist[py][px] + 1
                            queue.append((nx, ny))

                        else:
                            if visited[py][px] != visited[ny][nx]:
                                union(visited[py][px], visited[ny][nx])

                                if find(swans[0]) == find(swans[1]):
                                    answer = max(dist[ny][nx], dist[py][px])
                                    break
                
                if answer:
                    break

        print(answer)


    except ValueError or IndexError as e:
        print(e)