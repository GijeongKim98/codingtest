# 나무 재테크
'''https://www.acmicpc.net/problem/16235'''

import sys

MAX_AGE = 200
dx_dy = [(-1,-1),(1,-1),(-1,1),(1,1),(0,1),(0,-1),(1,0),(-1,0)]


if __name__  == "__main__":
    try:
        # N : 공간의 크기, M : 이미 심어져 있는 나무의 개수,  K: 시간
        N, M, K = map(int, sys.stdin.readline().split(" "))
        
        # A 배열
        A = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        # graph : 부동산 N * N의 크기의 칸이 존재 
        graph = [[[0 for _ in range(MAX_AGE)] for _ in range(N)] for _ in range(N)] 
        
        # 양분의 정보
        fertilizers = [[5 for _ in range(N)] for _ in range(N)]
        
        # 나무의 정보
        for _ in range(M):
            x, y, z = map(int, sys.stdin.readline().split(" "))
            graph[x-1][y-1][z-1] += 1
        
        
        # K년 동안 반복
        for _ in range(K):
            # Spring and Summer
            for x in range(N):
                for y in range(N):        
                    fertilizer = fertilizers[x][y]
            
                    for idx, num in enumerate(graph[x][y]):
                        fertilizer -= (idx+1) * num
                        
                        if fertilizer < 0:
                            fertilizer += (idx+1) * num
                            d_tree_age = idx + 1
                            l_tree_count, fertilizer = fertilizer//(idx+1), fertilizer%(idx+1)
                            break
                        
                        d_tree_age = idx+1 # 죽기 시작하는 나무의 나이
                        l_tree_count = num # 위의 나이에서 살수 있는 나무의 수 
                           
                    # 양분값 초기화
                    fertilizers[x][y] = fertilizer
                    
                    # 죽은 나무들의 양분 처리
                    # 만약 죽은 나무가 없어도 d_tree_age = MAX_AGE가 되어 실행되지 않음
                    fertilizers[x][y] += (graph[x][y][d_tree_age-1] - l_tree_count) * (d_tree_age//2)
                    graph[x][y][d_tree_age-1] = l_tree_count
                    
                    for age in range(d_tree_age+1,MAX_AGE+1):
                        fertilizers[x][y] += graph[x][y][age-1] * (age//2)
                        graph[x][y][age-1] = 0
                    
                    # 양분을 흡수한 나무들에 대한 처리
                    for age in range(d_tree_age, 0, -1):
                        if age == MAX_AGE:
                            if l_tree_count > 0:
                                print("Error 개수 최대값을 잘 못 계산함")
                            continue
                        graph[x][y][age] = graph[x][y][age-1]
                    
                    graph[x][y][0] = 0
                        
                        
            # Fall
            for x in range(N):
                for y in range(N):
                    count = 0
                    for age in range(5,MAX_AGE+1,5):
                        count += graph[x][y][age-1]
                    
                    for dx, dy in dx_dy:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx and nx < N and 0 <= ny and ny < N:
                            graph[nx][ny][0] += count

            
            # Winter
            for x in range(N):
                for y in range(N):
                    fertilizers[x][y] += A[x][y]
                    
        
        answer = 0
        
        for x in range(N):
            for y in range(N):
                answer += sum(graph[x][y])
        
        print(answer)
            
            
        
    except ValueError or IndexError as e:
        print(e)