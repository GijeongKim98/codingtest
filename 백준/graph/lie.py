# 거짓말
"""https://www.acmicpc.net/problem/1043"""

import sys
from collections import deque

try:
    N, M = map(int, sys.stdin.readline().split(' '))
    number_truth, *start_nodes = list(map(int, sys.stdin.readline().split(" ")))
    parties = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
    
    # print(f"N = {N}  // M = {M}")
    # print(f"number_truth : {number_truth}")
    # print(f"start_nodes = {start_nodes}")
    
    # for idx, party in enumerate(parties):
    #     print(f"party : {idx} // {party}")
    
    if not number_truth:
        print(M)
    
    else:
        ## Initialize Graph
        graph = {i : set() for i in range(1, N+1)}
        
        for party in parties:
            if party[0] == 1:
                continue
            pre_node = party[1]
            for node in party[2:]:
                graph[pre_node].add(node)
                graph[node].add(pre_node)
                pre_node = node
        
        for key in graph:
            graph[key] = list(graph[key])
        
        
        ## BFS
        queue = deque(start_nodes)
        visited = [0 for _ in range(N+1)]
        for s_n in start_nodes:
            visited[s_n] = 1
        
        
        while queue:
            pop_node = queue.popleft()
            for new_node in graph[pop_node]:
                if not visited[new_node]:
                    visited[new_node] = 1
                    queue.append(new_node)
        
        lie_people = set()
        
        for node in range(1,N+1):
            if not visited[node]:
                lie_people.add(node)
                
        result = 0
    
        for party in parties:
            c = 0
            for node in party[1:]:
                if node not in lie_people:
                    c = 1
                    break
            if not c:
                result += 1

        print(result)
        
except ValueError or IndexError as e:
    print(e)