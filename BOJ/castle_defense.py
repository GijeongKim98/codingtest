# 캐슬 디펜스
'''https://www.acmicpc.net/problem/17135'''

import sys
from collections import deque
from itertools import combinations

dx_dy = [(-1,0), (0,-1), (1,0)]


def move_the_enemy(g):
    return (g % (1 << (M*(N-1)))) * (1 << M)

def attack(g, c):
    set_ = set()
    for archer in c:
        x, y = bfs(g, archer)
        if x == -1 and y == -1:
            continue
        set_.add((x,y))
    
    return set_

def bfs(g, sx):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque([(sx, N-1)])
    visited[N-1][sx] = 1

    while queue:
        px, py = queue.popleft()
        if visited[py][px] > D:
            break
        
        if g & (1 << (py * M + px)):
            return px, py

        for dx, dy in dx_dy:
            nx, ny = px + dx, py + dy
            if 0 <= nx and nx < M and 0 <= ny and ny < N:
                if not visited[ny][nx]:
                    visited[ny][nx] = visited[py][px] + 1
                    queue.append((nx,ny))



    return -1, -1        
        


if __name__ == "__main__":
    try:
        N, M, D = map(int, sys.stdin.readline().split(" "))
        graph = 0
        for i in range(N):
            for j, v in enumerate(list(map(int, sys.stdin.readline().split(" ")))):
                if v:
                    graph += 1 << (i*M+j)

        # print(bin(graph))

        cases = combinations([i for i in range(M)], 3)

        answer = 0

        for c in cases:
            num = graph
            max_ = 0
            while num > 0:
                set_ = attack(num, c)
                max_ += len(set_)
                for x, y in list(set_):
                    num = num & ~(1 << (y*M+x))
                num = move_the_enemy(num)
            
            answer = max(max_, answer)

        
        print(answer)
    
    except ValueError or IndexError as e:
        print(e)