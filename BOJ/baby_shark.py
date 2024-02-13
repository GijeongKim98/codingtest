# 아기 상어
'''https://www.acmicpc.net/problem/16236'''

import sys
from collections import deque
import heapq as hq

SHARK = 9
X, Y, SIZE, EXP = 0,1,2,3

EMPTY = 0

dx_dy = [(0,-1), (-1,0), (1,0), (0,1)]



# def bfs(s_x, s_y):
#     visited = [[0 for _ in range(N)]for _ in range(N)]
#     queue = deque([(s_x, s_y)])
#     visited[s_y][s_x] = 1

#     while queue:
#         p_x, p_y = queue.popleft()
#         t = visited[p_y][p_x]
#         for dx, dy in dx_dy:
#             n_x, n_y = p_x + dx, p_y+dy
#             if 0 <= n_x and n_x < N and 0 <= n_y and n_y < N and not visited[n_y][n_x]:
#                 if graph[n_y][n_x] == EMPTY or graph[n_y][n_x] == shark_info[SIZE]:
#                     visited[n_y][n_x] = t+1
#                     queue.append((n_x, n_y))

#                 elif graph[n_y][n_x] < shark_info[SIZE]:
#                     graph[n_y][n_x] = EMPTY
#                     shark_info[X], shark_info[Y] = n_x, n_y
#                     shark_info[EXP] += 1
#                     if shark_info[EXP] == shark_info[SIZE]:
#                         shark_info[SIZE], shark_info[EXP] = shark_info[SIZE]+1, 0
#                     return t
    
#     return 0

def bfs(s_x, s_y):
    visited = [[0 for _ in range(N)]for _ in range(N)]
    queue = deque([(s_x, s_y)])
    visited[s_y][s_x] = 1
    heap = []
    t = 1000
    while queue:
        p_x, p_y = queue.popleft()
        for dx, dy in dx_dy:
            n_x, n_y = p_x + dx, p_y+dy
            if 0 <= n_x and n_x < N and 0 <= n_y and n_y < N and not visited[n_y][n_x]:
                if graph[n_y][n_x] == EMPTY or graph[n_y][n_x] == shark_info[SIZE]:
                    if not heap: 
                        visited[n_y][n_x] = visited[p_y][p_x]+1
                        queue.append((n_x, n_y))

                elif graph[n_y][n_x] < shark_info[SIZE]:
                    visited[n_y][n_x] = visited[p_y][p_x]+1
                    if visited[p_y][p_x] <= t:
                        t = visited[p_y][p_x]
                        hq.heappush(heap, (n_y, n_x))
    
    if not heap:
        return 0
    
    y, x = hq.heappop(heap)

    while heap:
        ny, nx = hq.heappop(heap)
        if y < ny:
            break
        elif x > nx:
            x = nx

    graph[y][x] = EMPTY
    shark_info[X], shark_info[Y] = x, y
    shark_info[EXP] += 1
    if shark_info[EXP] == shark_info[SIZE]:
        shark_info[SIZE], shark_info[EXP] = shark_info[SIZE]+1, 0

    return t

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

        shark_info = [0,0,2,0]
        
        # find start 
        for i in range(N):
            for j in range(N):
                if graph[i][j] == SHARK:
                    shark_info[X], shark_info[Y] = j, i
                    graph[i][j] = EMPTY
        
        answer = 00
        while True:
            k = bfs(shark_info[X], shark_info[Y])
            if not k:
                break
            answer += k

        print(answer)

    except ValueError or IndexError as e:
        print(e)