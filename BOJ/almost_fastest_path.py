# 거의 최단 경로
'''https://www.acmicpc.net/problem/5719'''

import sys
import heapq as hq
from collections import deque

INF = float("inf")

def dijkstra(s, e):
    q = [(0,s)] # weight, node
    dist = [INF for _ in range(N)]
    dist[s] = 0
    pre_nodes = [[] for _ in range(N)]
    # pre_nodes[s] = []
    
    while q:
        w, u = hq.heappop(q)
        if dist[u] < w:
            continue
        
        for v, l in graph[u].items():
            nw = w + l
            if dist[v] > nw:
                pre_nodes[v] = [u]
                dist[v] = nw
                hq.heappush(q,(nw,v))
            elif dist[v] == nw:
                pre_nodes[v].append(u)
                # hq.heappush(q,(nw,v))
    
    visited = [0 for _ in range(N)]
    visited[e] = 1
    queue = deque([e])

    while queue:
        v = queue.popleft()
        for u in pre_nodes[v]:
            if v in graph[u]:
                graph[u].pop(v)
            if not visited[u]:
                queue.append(u)
                visited[u] = 1
    
    
    q = [(0,s)] # weight, node
    dist = [INF for _ in range(N)]
    dist[s] = 0
    
    while q:
        w, u = hq.heappop(q)
        if dist[u] < w:
            continue
        
        for v, l in graph[u].items():
            nw = w + l
            if dist[v] >= nw:
                dist[v] = nw
                hq.heappush(q,(nw,v))
    
    
    return dist[e] if dist[e] != INF else -1

if __name__ == "__main__":
    while True:
        try:
            N, M = map(int, sys.stdin.readline().split(" "))
            if not N and not M:
                break
            
            s, e = map(int, sys.stdin.readline().split(" "))
            
            graph = {i:{} for i in range(N)}
            
            for _ in range(M):
                u, v, p = map(int, sys.stdin.readline().split(" "))
                graph[u][v] = p
                
            
            answer = dijkstra(s,e)
            
            print(answer)
                
        except ValueError or IndexError as e:
            print(e)