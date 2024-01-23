# 벽 부수고 이동하기 4
'''https://www.acmicpc.net/problem/16946'''

import sys
from collections import deque

# sys.setrecursionlimit(10**8)

WALL = 1
EMPTY = 0

dx_dys = [(1,0), (0,1), (-1,0), (0,-1)]

def bfs(s_x, s_y):
    count = 0
    queue = deque([(s_x, s_y)])
    visited[s_y][s_x] = 1
    
    while queue:
        p_x, p_y = queue.popleft()
        count += 1
        for dx, dy in dx_dys:
            n_x, n_y = p_x + dx, p_y + dy
            if 0 <= n_x and n_x < M and 0 <= n_y and n_y < N:
                if graph[n_y][n_x] == EMPTY and not visited[n_y][n_x]:
                    root[M*n_y+n_x] = M*p_y+p_x
                    visited[n_y][n_x] = 1
                    queue.append((n_x,n_y))
    
    return count

def find(num):
    if num == root[num]:
        return num
    
    root[num] = find(root[num])

    return root[num]

if __name__ == "__main__":
    
    try:
        N, M = map(int, sys.stdin.readline().split(" ")) 
        graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
        visited = [[0 for _ in range(M)] for _ in range(N)]
        
        root = [i for i in range(N*M)]
        counts = dict()
        walls = []
        
        for i in range(N):
            for j in range(M):
                if graph[i][j] == EMPTY and not visited[i][j]:
                    c = bfs(j,i)
                    counts[i*M+j] = c
        
        # print(root)
        # print(counts)
        
        # for row in range(M,M*N+1,M):
        #     print(root[row-M:row])
        
        for y in range(N):
            for x in range(M):
                if graph[y][x] == EMPTY:
                    print(EMPTY,end="")
                    continue
                set_ = set()
                a = 1
                for dx, dy in dx_dys:
                    n_x, n_y = x + dx, y + dy
                    if 0 <= n_x and n_x < M and 0 <= n_y and n_y < N and graph[n_y][n_x] == EMPTY:
                        num = find(M*n_y+n_x)
                        set_.add(num)
                        
                for num in list(set_):
                    a += counts[num]
                    a %= 10
                    
                print(a, end="")
            print()

    except ValueError or IndexError as e:
        print(e)
        