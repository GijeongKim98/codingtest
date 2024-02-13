# 임계 경로
'''https://www.acmicpc.net/problem/1948'''

from collections import deque
import sys

DIST, COUNT = 0, 1

if __name__ == "__main__":
    try:
        n, m = int(sys.stdin.readline()), int(sys.stdin.readline())
        
        graph = {i:dict() for i in range(1,n+1)}
        in_degree_list = [0 for _ in range(n+1)]
        
        for _ in range(m):
            s, e, w = map(int, sys.stdin.readline().split(" "))
            graph[s][e] = w
            in_degree_list[e] += 1
            
        
        start, end = map(int, sys.stdin.readline().split(" "))
        distances = [0 for _ in range(n+1)]
        reserve_graph = {i : [] for i in range(1,n+1)}

        queue = deque([start])
        
        while queue:
            pop = queue.popleft()
            pmw = distances[pop]
            
            for node, weight in graph[pop].items():
                # weight = 시작 노드로 부터 해당 노드까지의 거리
                weight += pmw
                # 해당 노드에 도달 했을 때 
                if weight > distances[node]: # 더 멀게 오는 경우
                    distances[node] = weight
                    reserve_graph[node] = [pop]
                elif weight == distances[node]: # 똑같은 거리로 오는 경우
                    reserve_graph[node].append(pop)
                
                in_degree_list[node] -= 1
                
                if not in_degree_list[node]:
                    queue.append(node)
        # 역추적
        queue.append(end)
        in_degree_list[end] = 1
        count = 0
        while queue:
            pop = queue.popleft()
            for new in reserve_graph[pop]:
                count += 1
                if not in_degree_list[new]:
                    queue.append(new)
                    in_degree_list[new] = 1
                    
        print(distances[end])    
        print(count)
        
        
    except ValueError or IndexError as e:
        print(e)