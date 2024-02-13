# 중량 제한
'''https://www.acmicpc.net/problem/1939'''

import sys
import heapq as hq
from collections import deque

INF = 1_000_000_000

def bfs(s):
    queue = deque([(s,INF)])
    visited = [0 for _ in range(N+1)]
    visited[s] = 1

    while queue:
        p, cost = queue.popleft()
        for new_node, new_cost in graph[p].items():
            if new_node == e:
                return min(cost, new_cost)
            
            if not visited[new_node]:
                visited[new_node] = 1
                queue.append((new_node, min(cost, new_cost)))
    
    return False

            


def find(x):
    if x == root[x]:
        return x
    
    root[x] = find(root[x])
    
    return root[x]


def union(x, y):
    x, y = find(x), find(y)

    if x == y:
        return False
    
    if rank[x] < rank[y]:
        x, y = y, x

    
    root[y] = x

    if rank[x] == rank[y]:
        rank[x] += 1

    
    return True
    

    

    
    


if __name__ == "__main__":
    try:
        N, M = map(int, sys.stdin.readline().split(" "))
        heap = []

        for _ in range(M):
            a, b, c = map(int, sys.stdin.readline().split(" "))
            hq.heappush(heap, (-c,a,b))

        root = [x for x in range(N+1)]
        rank = [0 for _ in range(N+1)]
        
        graph = {i : {} for i in range(1,N+1)}

        while heap:
            c, a, b = hq.heappop(heap)
            c *= -1
            if union(a, b):
                graph[a][b] = c
                graph[b][a] = c

        s, e = map(int, sys.stdin.readline().split(" "))

        answer =  bfs(s)


        print(answer)



    except ValueError or IndexError as e:
        print(e)