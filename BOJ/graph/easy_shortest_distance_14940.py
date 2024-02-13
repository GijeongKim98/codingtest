# 백준 14940 : 쉬운 최단거리
'''https://www.acmicpc.net/problem/14940'''

import sys
from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in dx_dy:
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x and new_x < m and 0 <= new_y and new_y < n:
                if not visited[new_y][new_x] and graph[new_y][new_x]:
                    visited[new_y][new_x] = visited[y][x] + 1
                    queue.append((new_x, new_y))


try:
    n, m = map(int, sys.stdin.readline().split(' '))
    graph = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

    # dx_dy
    dx_dy = [(1,0), (0,1), (-1,0), (0,-1)]

    # search 2 : destination
    break_count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                destination = (j,i)
                break_count = 1
                break
        if break_count:
            break
    # print(j , i)


    # Initialize visited
    visited = [[0 for _ in range(m)] for __ in range(n)]

    # Initialize deque
    queue = deque([destination])

    bfs()

    

    for y in range(n):
        for x in range(m):
            if graph[y][x] and not visited[y][x]:
                visited[y][x] = -1

    visited[destination[1]][destination[0]] = 0

    for row in visited:
        print(*row)
    

except ValueError or IndexError as e:
    print(e)

