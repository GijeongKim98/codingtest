# 외판원 순회
'''https://www.acmicpc.net/problem/2098'''

# 필요함수 및 상수 정리

INF = float("inf")

# 방문여부 확인 함수
def is_visited(visited, node):
    return visited & (1<<node)

# 방문한 도시 활성화 함수
def activate_node(visited, node):
    return visited | (1<<node)

# 방문한 도시 해제 함수
def deactivate_node(visited, node):
    return visited & ~(1<<node)

# DFS 함수 
def dfs(now, visited):
    # 모든 노드를 전부 방문한 경우
    if visited == visited_all_node:
        # graph에 선이 존재하는 경우
        if graph[now][0]:
            return graph[now][0]
        else:
            return INF
    
    # 현재 까지의 경로와 일치하는 경우가 존재할 때 즉 DP에 값이 있을 때
    if (now, visited) in dp.keys(): # key에 존재하는지 확인 O(1)
        return dp[(now, visited)]
    
    min_ = INF
    
    for new_node in range(1,N):
        if not graph[now][new_node] or is_visited(visited, new_node):
            continue
        cost = dfs(new_node, activate_node(visited, new_node)) + graph[now][new_node]
        min_ = min(cost, min_)
        
        
    dp[(now, visited)] = min_
        
    return min_

import sys
sys.setrecursionlimit(10 ** 6)

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        visited_all_node = (1 << N) - 1
        
        dp = dict()
        
        # print(visited_all_node)
        
        answer = dfs(0, 1)

        # print(dp)

        print(answer)
    
    except ValueError or IndexError as e:
        print(e)
    


