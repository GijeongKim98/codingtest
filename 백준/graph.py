# 알고리즘 수업 : DFS
''' https://www.acmicpc.net/problem/24479 '''
'''
import sys
sys.setrecursionlimit(10**6)
try:
    N, M ,R = tuple(map(int, sys.stdin.readline().split(' ')))
    edges = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]
    graph_ = {i:[] for i in range(1,N+1)}

    # 오름차순으로 방문 한다.
    # 각 list별 sort가 필요

    for tup_ in edges:
        graph_[tup_[0]].append(tup_[1])
        graph_[tup_[1]].append(tup_[0])

    visited = [0] * (N+1)

    for idx in graph_.keys():
        graph_[idx].sort()

    cnt = 1

    def dfs(x):
        global cnt
        visited[x] = cnt
        for v in graph_[x]:
            if visited[v] == 0:
                cnt += 1
                dfs(v)
    dfs(R)
    for i in range(1,N+1):
        print(visited[i])
        
except ValueError:
    print('Input Error')
'''

# 알고리즘 수업 DFS2
'''https://www.acmicpc.net/problem/24480'''
'''
import sys
sys.setrecursionlimit(10 ** 6)

try:
    N, M, R = tuple(map(int, sys.stdin.readline().split(' ')))
    edges = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]
    graph_ = {i: [] for i in range(1, N + 1)}

    # 오름차순으로 방문 한다.
    # 각 list별 sort가 필요

    for tup_ in edges:
        graph_[tup_[0]].append(tup_[1])
        graph_[tup_[1]].append(tup_[0])

    visited = [0] * (N + 1)

    for idx in graph_.keys():
        graph_[idx].sort(reverse=True)

    cnt = 1

    def dfs(x):
        global cnt
        visited[x] = cnt
        for v in graph_[x]:
            if visited[v] == 0:
                cnt += 1
                dfs(v)


    dfs(R)
    for i in range(1, N + 1):
        print(visited[i])

except ValueError:
    print('Input Error')
'''

# 알고리즘 수업 - BFS1
'''https://www.acmicpc.net/problem/24444'''
'''
import sys
from collections import deque
try:
    # input
    N,M,R = map(int,sys.stdin.readline().split(' '))
    edges = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]

    # graph init
    graph_ = {i : [] for i in range(1,N+1)}

    # graph 구성하기 dictionary이용
    for edge in edges:
        graph_[edge[0]].append(edge[1])
        graph_[edge[1]].append(edge[0])

    # 오름차순 정렬
    for vertex in graph_.keys():
        graph_[vertex].sort()

    # 빈 큐 생성
    queue = deque()

    # visited list
    visited = [0] * (N+1)

    # 방문 순서
    count = 1

    # Define bfs
    def bfs(x):
        global count
        queue.append(x)
        visited[x] = count
        while queue:
            pop_vertex = queue.popleft()
            for v in graph_[pop_vertex]:
                if not visited[v]:
                    queue.append(v)
                    count += 1
                    visited[v] = count

    # bfs(R) 실행
    bfs(R)

    # 출력
    for i in range(1,N+1):
        print(visited[i])

except ValueError:
    print('Input Error')
'''

# 알고리즘 수업 -BFS2
'''https://www.acmicpc.net/problem/24445'''
'''
import sys
from collections import deque
try:
    # input
    N,M,R = map(int,sys.stdin.readline().split(' '))
    edges = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]

    # graph init
    graph_ = {i : [] for i in range(1,N+1)}

    # graph 구성하기 dictionary이용
    for edge in edges:
        graph_[edge[0]].append(edge[1])
        graph_[edge[1]].append(edge[0])

    # 내림차순 정렬
    for vertex in graph_.keys():
        graph_[vertex].sort(reverse=True)

    # 빈 큐 생성
    queue = deque()

    # visited list
    visited = [0] * (N+1)

    # 방문 순서
    count = 1

    # Define bfs
    def bfs(x):
        global count
        queue.append(x)
        visited[x] = count
        while queue:
            pop_vertex = queue.popleft()
            for v in graph_[pop_vertex]:
                if not visited[v]:
                    queue.append(v)
                    count += 1
                    visited[v] = count

    # bfs(R) 실행
    bfs(R)

    # 출력
    for i in range(1,N+1):
        print(visited[i])

except ValueError:
    print('Input Error')
'''

# 바이러스
'''https://www.acmicpc.net/problem/2606'''
'''
import sys
from collections import deque
try:
    # Input
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    edges = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(E)]

    # initializing graph
    graph_ = {i : [] for i in range(1, V+1)}

    # graph append edge
    for edge in edges:
        graph_[edge[0]].append(edge[1])
        graph_[edge[1]].append(edge[0])

    # initializing visited list
    visited = [False] * (V+1)

    # initializing queue
    queue = deque()

    # Define bfs
    def bfs(x):
        visited[x] = True
        queue.append(x)
        while queue:
            u = queue.popleft()
            for v in graph_[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

    bfs(1)
    rlt = 0
    for i in range(2,V+1):
        if visited[i]:
            rlt += 1

    print(rlt)
except ValueError or IndexError:
    print('Input Error')
'''
# DFS & BFS
'''https://www.acmicpc.net/problem/1260'''

from collections import deque
import sys
sys.setrecursionlimit(10**6)
try:
    # Input
    V, E, R = map(int,sys.stdin.readline().split(' '))
    edges = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(E)]

    # Initializing graph
    graph_ = {i : [] for i in range(1,V+1)}

    # graph append edges
    for edge in edges:
        graph_[edge[0]].append(edge[1])
        graph_[edge[1]].append(edge[0])

    # graph_[idx] sort for idx = 1,...,V
    for idx in range(1,V+1):
        graph_[idx].sort()

    # Initializing visited list
    visited = [False] * (V+1)

    # Initializing result list
    result_dfs = []
    result_bfs = []

    # Define DFS
    def dfs(x):
        result_dfs.append(x)
        visited[x] = True
        for v in graph_[x]:
            if not visited[v]:
                dfs(v)

    # Initializing Queue
    queue = deque()

    # Define BFS
    def bfs(x):
        queue.append(x)
        visited[x] = True
        result_bfs.append(x)
        while queue:
            u = queue.popleft()
            for v in graph_[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
                    result_bfs.append(v)

    # execute DFS
    dfs(R)

    # Initializing visited list
    for i in range(1,V+1):
        visited[i] = False

    # execute BFS
    bfs(R)

    # output
    for vertex in result_dfs:
        print(vertex, end=' ')
    print()
    for vertex in result_bfs:
        print(vertex, end=' ')

except ValueError or IndexError:
    print('Input Error')







