# 비숍
'''https://www.acmicpc.net/problem/1799'''

import sys

BISHOP = 2

# 필요 함수 정리
def is_available_place(x,y):
    if not graph[y][x]:
        return False
    
    new_x, new_y = x-1, y-1
    while 0 <= new_x and new_x < N and 0 <= new_y and new_y < N:
        if graph[new_y][new_x] == BISHOP:
            return False
        new_x, new_y = new_x-1, new_y-1
    return True

def dfs(step, count, k=0):
    global max_value
    if step+k == N:
        max_value[k] = max(max_value[k], count)
        return 

    constant = step * 2 + k
    
    if constant >= N:
        x,y = N-1, constant % N + 1
    else:
        x,y = constant, 0
    
    dfs(step+1,count, k)
    
    for new_x, new_y in zip(range(x, -1,-1), range(y,N)):
        if is_available_place(new_x, new_y):
            graph[new_y][new_x] = BISHOP
            dfs(step+1, count+1, k)
            graph[new_y][new_x] = 1

        

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        graph = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        max_value = [0,0]
        dfs(0,0,0)
        dfs(0,0,1)
        
        print(sum(max_value))
        # print(max_value)
    except ValueError or IndexError as e:
        print(e)

