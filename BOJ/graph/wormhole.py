# 웜홀
'''https://www.acmicpc.net/problem/1865'''

# 벨만포드로 접근 만약 음의 사이클이 존재한다면 YES를 출력하자.
'''
import sys

INF = 100000000

def bellman_ford(graph, s, N, distances):
    
    distances[s] = 0
    
    for _ in range(N-1):
        for node in graph.keys():
            if distances[node] == INF:
                continue
            for ne_node, t in graph[node]:
                distances[ne_node] = min(distances[ne_node], distances[node] + t)
            
    for node in graph.keys():
        for ne_node, t in graph[node]:
            if distances[ne_node] > distances[node] + t:
                return 1

    for node, distance in enumerate(distances[1:]):
        if distance == INF:
            return bellman_ford(graph, node+1, N, distances)
    
    return 0

try:
    TC = int(sys.stdin.readline())
    result = []
    for _ in range(TC):
        N, M, W = map(int, sys.stdin.readline().split(" "))
        edges = dict()
        
        for i in range(M+W):
            S, E, T = map(int, sys.stdin.readline().split(" "))
            if i < M:
                if (S,E) not in edges.keys():
                    edges[(S,E)] = T
                    edges[(E,S)] = T
                else:
                    edges[(S,E)] = min(T, edges[(S,E)])
                    edges[(E,S)] = min(T, edges[(E,S)])
            else:
                if (S,E) not in edges.keys():
                    edges[(S,E)] = -T
                else:
                    edges[(S,E)] = min(-T, edges[(S,E)])
                    
        graph = {node: [] for node in range(1,N+1)}
        
        for (s, e), t in edges.items():
            graph[s].append((e,t))
            
        
        distances = [INF for _ in range(N+1)]

        is_containing_neg_cyc = bellman_ford(graph, 1, N, distances)
        
        result.append(is_containing_neg_cyc)
    
    for rlt in result:
        if rlt:
            print("YES")
        else:
            print("NO")        
        
        

except ValueError or IndexError as e:
    print(e)

'''

# 웜홀
'''https://www.acmicpc.net/problem/1865'''

# 벨만포드로 접근 만약 음의 사이클이 존재한다면 YES를 출력하자.

import sys

INF = 100000000

def bellman_ford(graph, s, N, distances):
    
    distances[s] = 0
    
    for _ in range(N-1):
        for node in graph.keys():
            for ne_node, t in graph[node]:
                distances[ne_node] = min(distances[ne_node], distances[node] + t)
            
    for node in graph.keys():
        for ne_node, t in graph[node]:
            if distances[ne_node] > distances[node] + t:
                return 1
    
    return 0

try:
    TC = int(sys.stdin.readline())
    result = []
    for _ in range(TC):
        N, M, W = map(int, sys.stdin.readline().split(" "))
        graph = {node: [] for node in range(1,N+1)}
        
        for i in range(M+W):
            S, E, T = map(int, sys.stdin.readline().split(" "))
            if i < M:
                graph[S].append((E,T))
                graph[E].append((S,T))
            else:
                graph[S].append((E,-T))
                    
        
        distances = [INF for _ in range(N+1)]

        is_containing_neg_cyc = bellman_ford(graph, 1, N, distances)
        
        result.append(is_containing_neg_cyc)
    
    for rlt in result:
        if rlt:
            print("YES")
        else:
            print("NO")        
        
        

except ValueError or IndexError as e:
    print(e)

