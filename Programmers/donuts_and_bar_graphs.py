# 도넛과 막대그래프

from collections import deque

G, D, B, E = 0,1,2,3

MAX_NODES = 1000000

def solution(edges):
    def bfs(s):
        queue = deque([s]) 
        visited[s] = 1
        
        while queue:
            p = queue.popleft()
            
            if out_degree[p] == 0: # 막대형 그래프의 마지막 노드는 out degree == 0
                return B
            
            elif in_degree[p] == 2: # 8자 형 그래프의 중심 노드는 다음을 만족
                return E
            
            for n in graph[p]:
                if not visited[n]:
                    queue.append(n)
                    visited[n] = 1

        return D 
    
    answer = [-1,0,0,0] # 생성정점, 도넛, 막대, 8자
    
    graph = {idx : [] for idx in range(1, MAX_NODES+1)}
    in_degree, out_degree = [0 for _ in range(MAX_NODES+1)], [0 for _ in range(MAX_NODES+1)]
    
    for s, e in edges:
        graph[s].append(e)
        in_degree[e] += 1
        out_degree[s] += 1
        
    visited = [0 for _ in range(MAX_NODES+1)]
    
    for node in range(MAX_NODES):
        if in_degree[node] == 0 and out_degree[node] > 0:
            generate_node = node
            break
        
    answer[G] = generate_node 
    
    for connected_node in graph[generate_node]:
        in_degree[connected_node] -= 1
        answer[bfs(connected_node)] += 1
        
    return answer


if __name__ == "__main__":
    edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
    edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
    edges = [[4, 9], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8], 
             [4,15], [13, 14], [14, 15], [15, 13],
             [4, 17], [16, 17]]
    
    # edges = [[1,4], [2,3], [3,2], [3,4], [4,3]]
    
    # edges = [[1,5], [2,3], [3,4], [4,5]]
    
    # edges = [[1,2],[2,2]]
    
    # edges = [[1,4],[2,3], [3,4], [4, 2]]
    
    # edges = [[1,5],[2,3], [3,4], [4, 2], [3,5], [5,6],[6,3]]
    
    # edges = [[1,2]]
    ans = solution(edges)
    print(ans)