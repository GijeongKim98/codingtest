# 열쇠
'''https://www.acmicpc.net/problem/9328'''

import sys
from collections import deque

# 상수
WALL = ord("*")
EMPTY = ord(".")
CONSTANT = abs(ord("A") - ord("a"))
DOCUMENT = ord("$")
COUNT = ord("Z") - ord("A") + 1

dx_dy = [(-1,0),(0,-1),(1,0),(0,1)]

# 필요 함수 정리
def is_wall(node):
    if 0 <= node - ord("A") < COUNT:
        return True
    return False

def is_key(node):
    if 0 <= node - ord("a") < COUNT:
        return True
    return False

def have_key(door):
    if (door + CONSTANT) in keys:
        return True
    return False

def is_available_node(x,y):
    if x < 0 or w <= x or y < 0 or h <= y:
        return False
    
    if visited[y][x]:
        return False
    
    node = graph[y][x]
    
    if node == EMPTY:
        return True
    
    elif node == WALL:
        return False
    
    elif is_wall(node):
        if have_key(node):
            return True
        
        else:
            if node in doors:
                doors[node].append((x,y))
            else:
                doors[node] = [(x,y)]
            
            return False
    
    elif is_key(node):
        keys.add(node)
        return True
    
    else:
        global answer
        answer += 1
        return True
        

def find_start_node(graph, h, w):
    start_nodes = []
    for x in range(w):
        for y in [0, h-1]:
            if is_available_node(x,y):
                start_nodes.append((x,y))
                visited[y][x] = 1
                if (graph[y][x] - CONSTANT) in doors:
                    for door_x, door_y in doors[graph[y][x] - CONSTANT]:
                        if not visited[door_y][door_x]:
                            start_nodes.append((door_x,door_y))
                            visited[door_y][door_x] = 1
                            
                    doors[graph[y][x] - CONSTANT] = []
                    
    for y in range(1,h-1):
        for x in [0, w-1]:
            if is_available_node(x,y):
                start_nodes.append((x,y))
                visited[y][x] = 1
                if (graph[y][x] - CONSTANT) in doors:
                    for door_x, door_y in doors[graph[y][x] - CONSTANT]:
                        if not visited[door_y][door_x]:
                            start_nodes.append((door_x,door_y))
                            visited[door_y][door_x] = 1
                    doors[graph[y][x] - CONSTANT] = []
    
    return start_nodes


def bfs(start_nodes):
    queue = deque(start_nodes)
    while queue:
        u, v = queue.popleft()
        for dx, dy in dx_dy:
            new_x, new_y = u+dx, v+dy
            if is_available_node(new_x, new_y):
                queue.append((new_x, new_y))
                visited[new_y][new_x] = 1
                
                if (graph[new_y][new_x] - CONSTANT) in doors:
                    for door_x, door_y in doors[graph[new_y][new_x] - CONSTANT]:
                        if not visited[door_y][door_x]:
                            queue.append((door_x,door_y))
                            visited[door_y][door_x] = 1
                    doors[graph[new_y][new_x] - CONSTANT] = []
             
        
        


if __name__ == "__main__":
    try:
        T = int(sys.stdin.readline())
        for _ in range(T):
            h, w = map(int, sys.stdin.readline().split(" "))
            graph = [list(map(ord, list(sys.stdin.readline().rstrip()))) for _ in range(h)]
            keys = set(map(ord, list(sys.stdin.readline().rstrip())))
            visited = [[0 for _ in range(w)] for __ in range(h)]
            doors = dict()
            answer = 0
            
            s_n = find_start_node(graph, h, w)
            bfs(s_n)
            
            print(answer)
        
    except ValueError or IndexError as e:
        print(e)