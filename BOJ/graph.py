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
'''
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
'''


# 연결 요소의 개수
'''https://www.acmicpc.net/problem/11724'''
'''
import sys
from collections import deque
try:
    # Input
    V, E = map(int, sys.stdin.readline().split(' '))
    edges = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(E)]

    # Initializing graph
    graph_ = {i:[] for i in range(1,V+1)}
    for u,v in edges:
        graph_[u].append(v)
        graph_[v].append(u)

    # Initializing visited
    visited = [False] * (V+1)

    # Initializing queue
    queue = deque()

    # Define BFS
    def bfs(start):
        visited[start] = True
        queue.append(start)
        while queue:
            u = queue.popleft()
            for new_x in graph_[u]:
                if not visited[new_x]:
                    visited[new_x] = True
                    queue.append(new_x)

    count = 0
    for x in range(1,V+1):
        if not visited[x]:
            bfs(x)
            count += 1

    print(count)

except ValueError or IndexError as e:
    print(e)
'''
# 적록색약
'''https://www.acmicpc.net/problem/10026'''
'''
import sys
sys.setrecursionlimit(10**6)

try:
    N = int(sys.stdin.readline())
    graph_ = [list(sys.stdin.readline()) for _ in range(N)]
    dx_dys = [(1,0),(0,1),(-1,0),(0,-1)]

    visited = [[0] * N for _ in range(N)]

    def dfs(x,y,start_colors):
        visited[y][x] = 1
        for dx, dy in dx_dys:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < N and 0 <= new_y < N:
                if not visited[new_y][new_x] and graph_[new_y][new_x] in start_colors:
                    dfs(new_x,new_y,start_colors)

    count1 = 0
    count2 = 0

    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                set_ = set(graph_[y][x])
                dfs(x,y,set_)
                count1 += 1
    set1, set2 = {'R','G'}, {'B'}
    visited = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                color = graph_[y][x]
                if color in set2:
                    dfs(x,y,set2)
                else:
                    dfs(x,y,set1)
                count2 += 1

    print(f'{count1} {count2}')
except ValueError or IndexError as e:
    print(e)
'''
# 연구소
'''https://www.acmicpc.net/problem/14502'''
'''
# module
import sys
from copy import deepcopy as copy
from collections import deque

# Setting
sys.setrecursionlimit(10**6)

# Define constant
VIRUS = 2
WALL = 1
EMPTY = 0

try:
    # Input
    N, M = map(int, sys.stdin.readline().split(' '))
    graph_ = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

    # Initializing virus_list, empty_list
    virus_list = []
    empty_list = []
    for y in range(N):
        for x in range(M):
            if graph_[y][x] == VIRUS:
                virus_list.append((x,y))
            elif graph_[y][x] == EMPTY:
                empty_list.append((x,y))
    # print(empty_list)

    # Initializing Queue
    queue = deque()

    # Initializing Delta x, y
    dx_dy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Result
    result = 0

    # Define BFS
    def bfs():
        visited = copy(graph_)
        for virus_point in virus_list:
            queue.append(virus_point)

        while queue:
            u, v = queue.popleft()
            for dx, dy in dx_dy:
                new_x, new_y = u+dx, v+dy
                if 0 <= new_x < M and 0 <= new_y < N and not visited[new_y][new_x]:
                    visited[new_y][new_x] = VIRUS
                    queue.append((new_x,new_y))

        global result
        count = 0

        for l in visited:
            count += l.count(EMPTY)

        result = max(result, count)

    # Define DFS
    def dfs(step):
        if step == 3:
            bfs()
            return
        for x_,y_ in empty_list:
            if graph_[y_][x_] == EMPTY:
                graph_[y_][x_] = WALL
                dfs(step+1)
                graph_[y_][x_] = EMPTY

    # Create WALL
    for i in range(2,len(empty_list)):
        for j in range(1,i):
            for k in range(j):
                x1, y1 = empty_list[i]
                x2, y2 = empty_list[j]
                x3, y3 = empty_list[k]

                graph_[y1][x1] = WALL
                graph_[y2][x2] = WALL
                graph_[y3][x3] = WALL

                bfs()

                graph_[y1][x1] = EMPTY
                graph_[y2][x2] = EMPTY
                graph_[y3][x3] = EMPTY


    # dfs(0)
    print(result)

except ValueError or IndexError as e:
    print(e)
'''
# 토마토 3차원
'''https://www.acmicpc.net/problem/7569'''
'''
from collections import deque
import sys
try:
    # Input
    M,N,H = map(int,sys.stdin.readline().split(' '))
    graph_ = [[list(map(int,sys.stdin.readline().split(' '))) for _ in range(N)] for __ in range(H)]
    # print(graph_)
    # Initializing Ripe_Tomato
    ripe_tomato = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if graph_[i][j][k] == 1:
                    ripe_tomato.append((k,j,i))
    # dx_dy_dz
    dx_dy_dz = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]

    # Define bfs
    def bfs():
        count = 0
        while queue:
            u,v,w = queue.popleft()
            for dx,dy,dz in dx_dy_dz:
                new_x, new_y, new_z = u+dx, v+dy, w+dz
                if 0<= new_x < M and 0 <= new_y < N and 0 <= new_z < H:
                    if not graph_[new_z][new_y][new_x]:
                        queue.append((new_x,new_y,new_z))
                        graph_[new_z][new_y][new_x] = 1 + graph_[w][v][u]

        return count

    queue = deque(ripe_tomato)

    answer = bfs()

    max_ = 1
    for metrix in graph_:
        for list_ in metrix:
            for x in list_:
                if not x:
                    print(-1)
                    sys.exit()
                max_ = max(max_, x)

    print(max_-1)

except ValueError or IndexError as e:
    print(e)
'''
# 안전 영역
'''https://www.acmicpc.net/problem/2468'''
'''
import sys
from collections import deque

try:
    N = int(sys.stdin.readline())
    graph_ = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(N)]

    dx_dy = [(1,0),(-1,0),(0,1),(0,-1)]

    def bfs(start,height):
        x,y = start
        queue = deque([start])
        visited[y][x] = True

        while queue:
            u,v = queue.popleft()
            for dx, dy in dx_dy:
                new_x, new_y = u+dx, v+dy
                if 0 <= new_x < N and 0 <= new_y < N:
                    if not visited[new_y][new_x] and graph_[new_y][new_x] > height:
                        queue.append((new_x,new_y))
                        visited[new_y][new_x] = True

    visited = [[False] * N for _ in range(N)]

    max_ = 0
    for h in range(101):
        count = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and graph_[i][j] > h:
                    bfs((j,i),h)
                    count += 1

        # print(f'h = {h} // c = {count}')

        if not count:
            break

        max_ = max(max_,count)
        visited = [[False] * N for _ in range(N)]

    print(max_)

except ValueError or IndexError as e:
    print(e)
'''

# 알파벳
'''https://www.acmicpc.net/problem/1987'''
'''
import sys
# sys.setrecursionlimit(10**6)

try:
    # Input
    R, C = map(int, sys.stdin.readline().split(' '))
    ord_A = ord('A')
    graph_ = [list(map(lambda x : ord(x) - ord_A, list(sys.stdin.readline().rstrip()))) for _ in range(R)]

    visited = [0] * 26

    dx_dy = [(1,0),(0,1),(-1,0),(0,-1)] # -> , <-, 위, 아래
    cnt = 0
    visited[graph_[0][0]] =1

    def dfs(n,x,y):
        for dx,dy in dx_dy:
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x < C and 0 <= new_y < R:
                ord_num = graph_[new_y][new_x]
                if not visited[ord_num]:
                    visited[ord_num] = 1
                    dfs(n+1,new_x,new_y)
                    visited[ord_num] = 0
        global cnt
        cnt = max(cnt, n)

    dfs(1,0,0)
    print(cnt)

except ValueError or IndexError as e:
    print(e)
'''

# 섬의 개수
'''https://www.acmicpc.net/problem/4963'''
'''
import sys
from collections import deque

try:
    # dx, dy
    dx_dy = [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

    # Define BFS()
    def bfs(start):
        x, y = start
        queue = deque([start])
        graph_[y][x] = 0
        while queue:
            u,v = queue.popleft()
            for dx,dy in dx_dy:
                new_x, new_y = u+dx, v+dy
                if 0 <= new_x < n and 0 <= new_y < m and graph_[new_y][new_x]:
                    queue.append((new_x,new_y))
                    graph_[new_y][new_x] = 0


    while True:
        # Input
        n, m = map(int, sys.stdin.readline().split(' '))
        graph_ = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(m)]

        if not n and not m:
            break

        # count
        cnt = 0

        # Searching graph_
        for i in range(m):
            for j in range(n):
                if graph_[i][j]:
                    bfs((j,i))
                    cnt += 1

        print(cnt)

except ValueError or IndexError as e:
    print(e)
'''

# 트리의 부모 찾기
'''https://www.acmicpc.net/problem/11725'''
'''
import sys
from collections import deque

try:
    # Input
    number_of_vertex = int(sys.stdin.readline())
    edges = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(number_of_vertex-1)]

    # Initializing Graph
    graph_ = {i : [] for i in range(1, number_of_vertex+1)}
    for u, v in edges:
        graph_[u].append(v)
        graph_[v].append(u)

    # result
    result = [0] * (number_of_vertex+1)

    # Define bfs()
    def bfs():
        queue = deque([1])
        result[1] = 1

        while queue:
            x = queue.popleft()
            for new_x in graph_[x]:
                if not result[new_x]:
                    result[new_x] = x
                    queue.append(new_x)

    # Output
    bfs()
    for p in result[2:]:
        print(p)

except ValueError or IndexError as e:
    print(e)
'''

# 숨바꼭질 2
'''https://www.acmicpc.net/problem/12851'''
'''
import sys
from collections import deque
try:
    N, K = map(int, input().split(' '))

    if N >= K:
        print(N-K)
        print(1)
        sys.exit()

    step = [100000] * 100001
    visited = [0] * 100001


    def bfs(start):
        count = 0
        queue = deque([start])
        step[start] = 1
        min_ = 0
        while queue:
            # print(f'queue = {queue}')
            u = queue.popleft()
            visited[u] = 1
            moving = [u-1, u+1, 2*u]

            if count:
                if step[u] == min_ and K in moving:
                    count += 1

            else:
                for new_x in moving:
                    if new_x == K:
                        count += 1
                        min_ = step[u]
                        # for i, x in enumerate(step[:2*K]):
                        #     print(f'i = {i} // step = {x}')
                        break
                    if 0 <= new_x < 100001 and not visited[new_x]:
                        if step[new_x] >= step[u] + 1:
                            step[new_x] = step[u] + 1
                            queue.append(new_x)

        return min_, count

    # output
    min_time, cnt = bfs(N)
    print(f'{min_time}\n{cnt}')

except ValueError or IndexError as e:
    print(e)
'''


# 경로찾기
'''https://www.acmicpc.net/problem/11403'''
'''
import sys
from collections import deque

try:
    N = int(sys.stdin.readline())
    metric = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

    graph_ = {i : [] for i in range(N)}
    for i, list_ in enumerate(metric):
        for j, exist_edge in enumerate(list_):
            if exist_edge:
                graph_[i].append(j)


    visited = [0] * N
    answer = {i : set() for i in range(N)}

    def bfs(start):
        pop_list = []
        queue = deque([start])
        visited[start] = 1
        while queue:
            u = queue.popleft()
            if graph_[u]:
                pop_list.append(u)
            for new_x in graph_[u]:
                if not visited[new_x]:
                    for pop_num in pop_list:
                        answer[pop_num].add(new_x)
                    visited[new_x] = 1
                    queue.append(new_x)
                else:
                    for pop_num in pop_list:
                        answer[pop_num].add(new_x)
                        answer[pop_num] = answer[pop_num].union(answer[new_x])

    for v in range(N):
        if not visited[v]:
            bfs(v)

    for set_ in answer.values():
        for j in range(N):
            if j in set_:
                print(1, end = ' ')
            else:
                print(0, end = ' ')
        print()


except ValueError or IndexError as e:
    print(e)
'''

# Floyd-Warshall Algorithm
'''
import sys
try:
    N = int(sys.stdin.readline())
    graph_ = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

    for through in range(N): # 거치는 점
        for start in range(N): # 시작점
            for end in range(N): # 끝나는 점
                if not graph_[start][end] and graph_[start][through] and graph_[through][end]:
                    graph_[start][end] = 1

    for l in graph_:
        for x in l:
            print(x, end = ' ')
        print()
except ValueError or IndexError:
    print('Input Error')
'''

# 영역 구하기
'''https://www.acmicpc.net/problem/2583'''


import sys
from collections import deque
'''
try:
    # Input
    M, N, K = map(int, sys.stdin.readline().split(' '))

    # Initailizing graph
    graph = [[0 for _ in range(N)] for __ in range(M)]

    for k in range(K):
        x1,y1,x2,y2 = map(int, sys.stdin.readline().split(' '))
        for y in range(y1,y2):
            for x in range(x1,x2):
                graph[y][x] = 1
    
    # print(graph)
    # Initializing Queue
    queue = deque()

    # dx_dy
    dx_dy = [(-1,0),(1,0),(0,1),(0,-1)]

    def bfs(start_node):
        queue.append(start_node)
        s_x, s_y = start_node
        graph[s_y][s_x] = 1
        rlt = 0
        while queue:
            u, v = queue.popleft()
            rlt += 1
            for dx, dy in dx_dy:
                new_x, new_y = u+dx, v+dy
                if (0 <= new_x and new_x < N) and (0 <= new_y and new_y < M) and not graph[new_y][new_x]:
                    queue.append((new_x, new_y))
                    graph[new_y][new_x] = 1
        return rlt
    
    rlt_list = []

    for y in range(M):
        for x in range(N):
            if not graph[y][x]:
                rlt_list.append(bfs((x,y))) 
    
    rlt_list.sort()

    print(len(rlt_list))
    print(*rlt_list)

except ValueError or IndexError as e:
    print(e)
'''


# 점프
'''https://www.acmicpc.net/problem/1890'''
'''
# 시간 초과 코드
import sys
sys.setrecursionlimit(10**6)

try:
    N = int(sys.stdin.readline())
    graph_ = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

    # visited = [[0]*N for _ in range(N)]
    # stack_ = []
    cnt = 0

    def dfs(x,y):
        global cnt
        if N-1 == x and N-1 == y:
            cnt += 1
            return

        jump_num = graph_[y][x]

        # 오른쪽
        if x + jump_num < N:
            dfs(x+jump_num,y)
        # 아래
        if y + jump_num < N:
            dfs(x, y+ jump_num)

    dfs(0,0)
    print(cnt)
except ValueError or IndexError as e:
    print(e)

'''

# MooTube
'''https://www.acmicpc.net/problem/15591'''
'''
import sys
from collections import deque

try:
    # Input N, Q
    N,Q = map(int,sys.stdin.readline().split(' '))
    
    # Initialize Graph
    graph = {i:[] for i in range(1,N+1)}
    
    # Input p,q,r 
    for _ in range(N-1):
        p,q,r = map(int,sys.stdin.readline().split(' '))
        graph[p].append([q,r])
        graph[q].append([p,r])
    
    USADO = [[] for _ in range(N)]

    #print(graph)

    # max_inf
    inf = 1000000001
  
    # get_count_point : bfs
    def get_count_point(node):
        visited = [inf for _ in range(N+1)]
        visited[node] = inf+1
        queue = deque([node])

        while queue:
            pop_node = queue.popleft()
            
            for new_node, weight in graph[pop_node]:
                if visited[new_node] == inf:
                    visited[new_node] = min(weight, visited[pop_node])
                    queue.append(new_node)
        # print(visited)
        USADO[node-1] = visited[1:]

    
    # result
    result = []
    

    for question in range(Q):
        k, v = map(int, sys.stdin.readline().split(' '))
        cnt = 0
        if not USADO[v-1]:
            get_count_point(v)
        
        # print(USADO)
        
        for distance in USADO[v-1]:
            if k <= distance:
                cnt += 1
        result.append(cnt-1)
    
    # Output
    for r in result:
        print(r)

except ValueError or IndexError as e:
    print(e)
'''


# 스타트 링크
'''https://www.acmicpc.net/problem/5014'''
'''
import sys
from collections import deque
try:
    F, S, G, U, D = map(int, sys.stdin.readline().split(' '))

    if S == G:
        print(0)
        sys.exit()
    

    dx_ =  [-D, U]
    visited = [0 for _ in range(F+1)]

    def bfs(start):
        visited[start] = 1
        queue = deque([start])

        while queue:
            pop_node = queue.popleft()
            for dx in dx_:
                new_node = pop_node + dx
                if 0 < new_node and new_node <= F and not visited[new_node]:
                    
                    if new_node == G:
                        return visited[pop_node]
                    
                    visited[new_node] = visited[pop_node] + 1
                    queue.append(new_node)
        
        return 0
    
    
    rlt = bfs(S)
    if not rlt:
        print('use the stairs')
    else:
        print(rlt)

except ValueError or IndexError as e:
    print(e)             
'''

# 그림
'''https://www.acmicpc.net/problem/1926'''

from collections import deque
import sys

try:
    n, m = map(int, sys.stdin.readline().split(' '))

    graph_ = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(n)]

    visited = [[0 for _ in range(m)] for __ in range(n)]

    queue = deque()

    dx_dy = [(-1,0),(1,0),(0,1),(0,-1)]

    def bfs(x,y):
        queue.append((x,y))
        graph_[y][x] = 0
        size_ = 0

        while queue:
            u, v = queue.popleft()
            size_ += 1
            for dx, dy in dx_dy:
                new_x, new_y = u+dx, v+dy
                if 0 <= new_x and new_x < m and 0 <= new_y and new_y < n:
                    if graph_[new_y][new_x]:
                        graph_[new_y][new_x] = 0
                        queue.append((new_x,new_y))
        return size_
    
    cnt = 0
    max_size = 0
    for y in range(n):
        for x in range(m):
            if graph_[y][x]:
                cnt += 1
                max_size = max(max_size, bfs(x,y))
    
    print(cnt)
    print(max_size)


except ValueError or IndexError as e:
    print(e)




