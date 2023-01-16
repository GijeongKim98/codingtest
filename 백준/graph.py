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
'''
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
'''
# 단자 번호 붙이기
'''https://www.acmicpc.net/problem/2667'''
'''
import sys
sys.setrecursionlimit(10**6)

try:
    # Input
    N = int(sys.stdin.readline())
    graph_ = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

    # connected_vectors_delta
    vectors = [(0,1),(1,0),(-1,0),(0,-1)]

    # Define dfs
    def dfs(x,y,count):
        visited[y][x] = True
        for vector in vectors:
            new_x, new_y = x-vector[0], y-vector[1]
            if 0 <= new_x < N and 0 <= new_y < N:
                if graph_[new_y][new_x] and not visited[new_y][new_x]:
                    count = dfs(new_x,new_y,count+1)
        return count

    # Initializing visited list
    visited = [[False]*N for _ in range(N)]

    # result
    result = []

    # main_code
    for row in range(N):
        for col in range(N):
            if graph_[row][col] == 1 and not visited[row][col]:
                result.append(dfs(col,row,0)+1)

    # Output
    result.sort()
    print(len(result))
    for c in result:
        print(c)
except ValueError or IndexError as e:
    print(e)
'''

# 유기농 배추
'''https://www.acmicpc.net/problem/1012'''
'''
import sys
from collections import deque

try:
    # connected_vector_delta
    vectors = [(1,0),(0,1),(-1,0),(0,-1)]

    # Define bfs
    def bfs(x,y):
        queue.append((x,y))
        visited[y][x] = True
        while queue:
            u,v = queue.popleft()
            for dx,dy in vectors:
                new_x, new_y = u+dx, v+dy
                if 0 <= new_x < M and 0 <= new_y < N:
                    if graph_[new_y][new_x] and not visited[new_y][new_x]:
                        queue.append((new_x,new_y))
                        visited[new_y][new_x] = True

    # Input
    number_of_test = int(sys.stdin.readline())

    # testcase execute
    for _ in range(number_of_test):
        # Input
        M,N,K = map(int,sys.stdin.readline().split(' '))
        points = [tuple(map(int,sys.stdin.readline().split(' '))) for _ in range(K)]

        # Initializing graph
        graph_ = [[0]*M for _ in range(N)]
        for x_,y_ in points:
            graph_[y_][x_] = 1

        # Initializing visited
        visited = [[False]*M for _ in range(N)]

        # Initializing Queue
        queue = deque()

        # main_code
        rlt = 0
        for i in range(N):
            for j in range(M):
                if graph_[i][j] and not visited[i][j]:
                    bfs(j,i)
                    rlt += 1

        # Output
        print(rlt)

except ValueError or IndexError as e:
    print(e)
'''

# 미로탐색
'''https://www.acmicpc.net/problem/2178'''
'''
import sys
from collections import deque

try:
    # Input
    N, M = map(int, sys.stdin.readline().split())
    graph_ = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]

    # Initializing visited
    visited = [[0] * M for _ in range(N)]

    # Initializing Queue
    queue = deque()

    # Delta_connected_vectors
    vectors = [(1,0),(0,1),(0,-1),(-1,0)]

    # Define bfs
    def bfs(x,y):
        visited[y][x] = 1
        queue.append((x,y))
        while queue:
            u,v = queue.popleft()
            for dx, dy in vectors:
                new_x, new_y = u+dx, v+dy
                # if new_x == M-1 and new_y == N-1:
                #     return visited[v][u] + 1

                if 0 <= new_x < M and 0 <= new_y < N:
                    if graph_[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                        queue.append((new_x,new_y))
                        visited[new_y][new_x] = visited[v][u] + 1

    bfs(0,0)
    print(visited[N-1][M-1])
except ValueError or IndexError as e:
    print(e)
'''
# 숨바꼭질
'''https://www.acmicpc.net/problem/1697'''
'''
import sys
from collections import deque

try:
    # Input
    N, K = map(int,sys.stdin.readline().split(' '))

    # special case : K < N
    if K <= N:
        print(N-K)
        sys.exit()


    # Initializing visited
    visited = [0] * (2*K+1)

    # Initializing queue
    queue = deque()

    # Define bfs
    def bfs(x):
        queue.append(x)
        while queue:
            u = queue.popleft()
            connected_points = [u+1,2*u,u-1]
            for new_x in connected_points:
                if 0 <= new_x <= 2*K and visited[new_x] == 0:
                    queue.append(new_x)
                    visited[new_x] = visited[u] + 1

            if visited[K] != 0:
                return
    # Execute bfs
    bfs(N)

    # Output
    print(visited[K])

except ValueError or IndexError as e:
    print(e)
'''
# 나이트의 이동
'''https://www.acmicpc.net/problem/7562'''
'''
import sys
from collections import deque

try:
    # Input
    number_of_test = int(sys.stdin.readline())

    # delta_vectors
    vectors = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

    # Define bfs
    def bfs(start,end):
        x,y = start
        visited[y][x] = 1
        queue.append(start)

        while queue:
            u, v = queue.popleft()
            for dx,dy in vectors:
                new_x, new_y = u+dx,v+dy
                if 0 <= new_x < I and 0 <= new_y < I and visited[new_y][new_x] == 0:
                    queue.append((new_x,new_y))
                    visited[new_y][new_x] = visited[v][u] + 1
            if visited[end[1]][end[0]] != 0:
                return


    # Execute testcase
    for _ in range(number_of_test):
        I = int(sys.stdin.readline())
        start_ = tuple(map(int,sys.stdin.readline().split(' ')))
        end_ = tuple(map(int,sys.stdin.readline().split(' ')))

        # Initializing visited
        visited = [[0] * I for __ in range(I)]

        # Initializing queue
        queue = deque()

        # Execute bfs
        bfs(start_,end_)

        # Output
        print(visited[end_[1]][end_[0]] - 1)
except ValueError or IndexError as e:
    print(e)

'''
# 토마토
'''https://www.acmicpc.net/problem/7576'''

import sys
from collections import deque

try:
    # Input
    M, N = map(int, sys.stdin.readline().split(' '))
    graph_ = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

    # Searching start point
    start_points = []
    for y in range(N):
        for x in range(M):
            if graph_[y][x] == 1:
                start_points.append((x,y))

    # delta_of_vector
    vectors = [(-1,0),(0,-1),(0,1),(1,0)]

    # Initializing Queue
    queue = deque()

    # Define bfs
    def bfs(starts):
        for point in starts:
            queue.append(point)
        while queue:
            u, v = queue.popleft()
            for dx, dy in vectors:
                new_x, new_y = u+dx, v+dy
                if 0 <= new_x < M and 0 <= new_y < N and graph_[new_y][new_x] == 0:
                    queue.append((new_x,new_y))
                    graph_[new_y][new_x] = graph_[v][u] + 1

    # Execute bfs
    bfs(start_points)

    # Define searching non ripens // max_
    def search_max():
        max_ = 0
        for row in graph_:
            for p in row:
                if p == 0:
                    return 0
                max_ = (max_ if max_ > p else p)
        return max_

    # Output
    result = search_max()
    print(result-1)

except ValueError or IndexError as e:
    print(e)





















