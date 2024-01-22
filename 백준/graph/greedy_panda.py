# 욕심쟁이 판다
'''https://www.acmicpc.net/problem/1937'''

import sys
sys.setrecursionlimit(10**6)

dx_dy = [(-1,0), (0,-1), (0,1), (1,0)]

def dfs(x,y):
    if visited[y][x]:
        return visited[y][x]
    
    visited[y][x] = 1
    
    for dx, dy in dx_dy:
        nx, ny = x+dx, y+dy
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if graph[y][x] < graph[ny][nx]:
                visited[y][x] = max(dfs(nx,ny) + 1, visited[y][x])
            
    return visited[y][x]
    

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        visited = [[0 for _ in range(N)] for _ in range(N)]
        
        answer = 0
        
        for y in range(N):
            for x in range(N):
                if not visited[y][x]:
                    answer = max(answer, dfs(x,y))
        
        print(answer)

    except ValueError or IndexError as e:
        print(e)