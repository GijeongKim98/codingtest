# 다리 만들기
'''https://www.acmicpc.net/problem/2146'''

from collections import deque
import sys

# 바다, 섬 구분
SEA, ISLAND = 0, 1

# dx_dy : 인접 노드와의 관계
dx_dy = [(-1,0), (0,-1), (0,1), (1,0)]

# bfs : 너비 우선 탐색
def bfs(sx,sy,idx):
    queue = deque([(sx,sy)])
    visited[sy][sx] = idx
    
    while queue:
        px, py = queue.popleft()
        cond = False
        for dx, dy in dx_dy:
            nx, ny = px+dx, py+dy
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if graph[ny][nx] == ISLAND: # 섬일 경우
                    if not visited[ny][nx]:
                        visited[ny][nx] = idx
                        queue.append((nx, ny))
                
                else: # 바다 일 경우
                    cond = True
        
        if cond:
            start_nodes.append((px, py))
            
            
                 
        

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        # 방문 여부
        visited = [[0 for _ in range(N)] for _ in range(N)]
        
        # 섬과의 거리
        # 섬인 곳은 0으로 표현
        distances = [[0 for _ in range(N)] for _ in range(N)]
        
        # 섬의 노드마다 idx값 색인
        # 1번 섬 부터 시작
        idx = 1
        
        # 바다와 맞다아 있는 섬의 노드를 시작 노드로 지정
        start_nodes = []
        
        for y in range(N):
            for x in range(N):
                if not visited[y][x] and graph[y][x] == ISLAND:
                    bfs(x,y,idx)
                    idx += 1
                    

        # 바다와 맞닿아 있는 노드들로 부터 너비우선탐색을 다시 실시
        # BFS
        queue = deque(start_nodes)
        answer = 100000
        while queue:
            px, py = queue.popleft()
            for dx, dy in dx_dy:
                nx, ny = px + dx, py + dy
                if 0 <= nx and nx < N and 0 <= ny and ny < N:
                    if not visited[ny][nx]:
                        # 아직 방문하지 않았다면
                        # px, py의 섬 번호를 색인시키고 거리를 1 증가 시켜 저장
                        visited[ny][nx], distances[ny][nx] = visited[py][px], distances[py][px] + 1
                        queue.append((nx, ny))
                    
                    elif visited[ny][nx] != visited[py][px]:
                        # 이미 방문한 노드인데 이어진 섬과 다른 경우
                        answer = min(distances[ny][nx] + distances[py][px] + 1, answer) 
                        
            
            
        print(answer-1)
                     
    except ValueError or IndexError as e:
        print(e)