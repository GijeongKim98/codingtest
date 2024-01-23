# 파티
'''https://www.acmicpc.net/problem/1238'''

import sys
import heapq as hq

sys.setrecursionlimit
INF = 1000000

def dijkstra(node, graph, distance):
    heap_queue = []
    hq.heappush(heap_queue, (0, node))
    distance[node] = 0
    while heap_queue:
        pop_time, pop_node = hq.heappop(heap_queue)
        
        if distance[pop_node] < pop_time:
            continue

        for new_time, new_node in graph[pop_node]:
            dist = distance[pop_node] + new_time
            if dist < distance[new_node]:
                distance[new_node] = dist
                hq.heappush(heap_queue, (new_time, new_node))
        # print(distance)
        
    
try:
    N, M, X = map(int, sys.stdin.readline().split(" "))

    # Initialize graph
    graph1 = {i : [] for i in range(1, N+1)} # X로 갈 때의 그래프
    graph2 = {j : [] for j in range(1, N+1)} # X에서 올 때의 그래프

    for _ in range(M):
        start, end, time = map(int, sys.stdin.readline().split(" "))
        graph1[end].append((time, start))           
        graph2[start].append((time, end))
    
    distance1 = [INF for _ in range(N+1)]
    distance2 = [INF for _ in range(N+1)]
    
    dijkstra(X, graph1, distance1)
    dijkstra(X, graph2, distance2)
    
    result = 0
    
    for dist1, dist2 in zip(distance1[1:], distance2[1:]):
        result = max(result, dist1 + dist2)
    
    print(result)
     
    
except ValueError or IndexError as e:
    print(e)