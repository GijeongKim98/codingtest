# 최단 경로
'''https://www.acmicpc.net/problem/1753'''

import heapq
import sys

try:
    # Input
    V,E = map(int,sys.stdin.readline().split(' '))
    start_node = int(sys.stdin.readline())
    u_v_w_lists = [tuple(map(int,sys.stdin.readline().split(' '))) for _ in range(E)]

    # Initializing graph
    graph_ = {i:[] for i in range(1,V+1)}
    for u,v,w in u_v_w_lists:
        graph_[u].append((w,v))

    # Initializing visited
    visited = [False] * (V+1)

    # maximum distance
    Inf = E * 10 + 1

    # Initializing distance
    distance = [Inf] * (V+1)

    # Initializing heapq
    queue = []

    # dijkstra
    def dijkstra(start):
        distance[start] = 0
        heapq.heappush(queue, (distance[start], start))

        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if distance[current_node] < current_distance: # 이미 변화가 된 경우
                continue
            for new_distance, new_node in graph_[current_node]:
                # print(f'new_distance ={new_distance} // new_node = {new_node}')
                # print(f'current_distance = {current_distance}')
                # print(f'dis = {distance}')
                distance_ = current_distance + new_distance
                if distance_ < distance[new_node]:
                    distance[new_node] = distance_
                    heapq.heappush(queue, (distance_, new_node))
        return distance

    answer = dijkstra(start_node)
    for a in answer[1:]:
        if a == Inf:
            print('INF')
        else:
            print(a)

except ValueError or IndexError as e:
    print(e)
