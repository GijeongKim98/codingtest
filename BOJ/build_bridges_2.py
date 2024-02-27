# 다리 만들기
'''https://www.acmicpc.net/problem/17472'''

import sys
from collections import deque
import heapq as hq


R, C = 0, 1
S, I = 0, 1

dx_dy = [(-1,0), (0,-1), (1,0), (0,1)] # 좌 상 우 하

def bfs(sx, sy, idx):
    visited[sy][sx][R], visited[sy][sx][C] = idx, idx
    queue = deque([(sx,sy)]) 
    
    while queue:
        px, py = queue.popleft()
        island_info[idx].append((px, py))
        for dx, dy in dx_dy:
            nx, ny = px+dx, py+dy
            if 0 <= nx and nx < M and 0 <= ny and ny < N:
                if not visited[ny][nx][R] and graph[ny][nx] == I:
                    visited[ny][nx][R], visited[ny][nx][C] = idx, idx
                    queue.append((nx, ny))
    return

def search(x,y,d):
    rc = d % 2
    dist = 0
    idx = visited[y][x][rc]
    
    if d == 0:   # 좌
        for nx in range(x-1,-1,-1):
            if not visited[y][nx][rc]: # 바다이며 아직 다리가 건설 되지 않은 경우
                visited[y][nx][rc] = idx
                dist += 1
                
            elif idx == visited[y][nx][rc]: # 같은 섬일 경우
                break
            
            else: # 다른 섬 일 경우
                if graph[y][nx] == I and  dist > 1: # 다른 섬인데 거리가 1이상 만
                    return visited[y][nx][rc], dist
                else:
                    break
            
            
    elif d == 1: # 상
        for ny in range(y-1,-1,-1):
            if not visited[ny][x][rc]: # 바다이며 아직 다리가 건설 되지 않은 경우
                visited[ny][x][rc] = idx
                dist += 1
            elif idx == visited[ny][x][rc]: # 같은 섬일 경우
                break
            
            else: # 다른 섬 일 경우
                if graph[ny][x] == I and dist > 1: # 다른 섬인데 거리가 1이상 만
                    return visited[ny][x][rc], dist
                else:
                    break
            
            
               
    elif d == 2: # 우
        for nx in range(x+1,M):
            if not visited[y][nx][rc]: # 바다이며 아직 다리가 건설 되지 않은 경우
                visited[y][nx][rc] = idx
                dist += 1
            
            elif idx == visited[y][nx][rc]: # 같은 섬일 경우
                break
            
            else: # 다른 섬 일 경우
                if graph[y][nx] == I and  dist > 1: # 다른 섬인데 거리가 1이상 만
                    return visited[y][nx][rc], dist
                else:
                    break
            
                 
    else:        # 하
        for ny in range(y+1,N):
            if not visited[ny][x][rc]: # 바다이며 아직 다리가 건설 되지 않은 경우
                visited[ny][x][rc] = idx
                dist += 1
            elif idx == visited[ny][x][rc]: # 같은 섬일 경우
                break
            
            else: # 다른 섬 일 경우
                if graph[ny][x] == I and  dist > 1: # 다른 섬인데 거리가 1이상 만
                    return visited[ny][x][rc], dist
                else:
                    break
            
            
    return 0, dist # 범위를 넘어서는 경우

def find(x):
    if x == root[x]:
        return x
    
    root[x] = find(root[x])
    
    return root[x]

    
def union(n1, n2):
    n1, n2 = find(n1), find(n2)
    
    if n1 == n2:
        return False
    
    if rank[n1] < rank[n2]:
        n1, n2 = n2, n1
        
    root[n2] = n1
    
    if rank[n1] == rank[n2]:
        rank[n1] += 1
    
    return True    
    

def is_mst():
    for i in range(1, the_number_of_islands):
        for j in range(i+1, the_number_of_islands):
            if find(i) != find(j):
                return False        

    return True

if __name__ == "__main__":
    try:
        N, M = map(int, sys.stdin.readline().split(" "))
        graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        visited = [[[0,0] for _ in range(M)] for _ in range(N)]
        
        the_number_of_islands = 1
        
        island_info = dict()
        
        for i in range(N):
            for j in range(M):
                if graph[i][j] and not visited[i][j][R]:
                    island_info[the_number_of_islands] = []
                    bfs(j,i,the_number_of_islands)
                    the_number_of_islands += 1 
        
        heap = [] 
        
        for idx in range(1, the_number_of_islands):
            for x, y in island_info[idx]:
                for d in range(4):
                    new_island, dist = search(x,y,d)
                    if new_island:
                        hq.heappush(heap, (dist, idx, new_island))
        
        root = [idx for idx in range(the_number_of_islands)]
        rank = [0 for _ in range(the_number_of_islands)]
        
        answer = 0
        
        while heap:
            dist, i1, i2 = hq.heappop(heap)
            if union(i1, i2):
                answer += dist
        
        print(answer if is_mst() else -1)
                    
        
    except ValueError or IndexError as e:
        print(e)