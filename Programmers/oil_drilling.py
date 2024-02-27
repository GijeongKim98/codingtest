# 석유 시추

from collections import deque

dx_dy = [(-1,0), (0,-1), (1,0), (0,1)]

EMPTY, OIL = 0, 1

def solution(land):
    def bfs(sx, sy):
        col_set = set()
        count = 0
        
        queue = deque([(sx,sy)])
        visited[sy][sx] = 1
        
        while queue:
            px, py = queue.popleft()
            count += 1
            col_set.add(px)
            
            for dx, dy in dx_dy:
                nx, ny = px+dx, py+dy
                if 0 <= nx  and nx < M and 0 <= ny and ny < N:
                    if land[ny][nx] == OIL and not visited[ny][nx]:
                        queue.append((nx,ny))
                        visited[ny][nx] = 1
        
        return col_set, count 
        
    
    N, M = len(land), len(land[0])
    
    visited = [[0 for _ in range(M)] for _ in range(N)]
    cols = [0 for _ in range(M)]
    
    for i in range(N):
        for j in range(M):
            if land[i][j] == OIL and not visited[i][j]:
                col_info, count = bfs(j,i)
                for idx in list(col_info):
                    cols[idx] += count
    
    return max(cols)    
    
    
if __name__ == "__main__":
    land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
    land = [[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]

    ans = solution(land)
    
    print(ans)
    
    # 9 16