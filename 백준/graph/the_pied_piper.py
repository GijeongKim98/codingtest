# 피리부는 사나이
'''https://www.acmicpc.net/problem/16724'''

import sys

sys.setrecursionlimit(10**7)

directions = {"U":0,"D":1,"L":2,"R":3}

directs = [(0,-1), (0,1), (-1,0), (1,0)]

def dfs(c, x, y):
    global answer
    
    if visited[y][x]:
        if visited[y][x] == c:
            answer += 1
        return 
            
    visited[y][x] = c
    dx, dy = directs[graph[y][x]]
    dfs(c, x+dx, y+dy)


if __name__ == "__main__":
    try:
        N, M = map(int, sys.stdin.readline().split())
        graph = [list(map(lambda x : directions[x], list(sys.stdin.readline().rstrip()))) for _ in range(N)]
        
        visited = [[0 for _ in range(M)] for _ in range(N)]
        answer = 0
        count = 1
        
        for i in range(N):
            for j in range(M):
                if not visited[i][j]:
                    dfs(count, j, i) 
                    count += 1
        
        print(answer)
        
    except ValueError or IndexError as e:
        print(e)