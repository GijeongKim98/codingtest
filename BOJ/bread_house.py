# 빵집
'''https://www.acmicpc.net/problem/3109'''

import sys

EMPTY, BUILDING = ord("."), ord("x")
PIPE = 0

drs = [-1,0,1]

def dfs(c, r):
    if c == C-1:
        return 1
    
    result = 0
    
    for dr in drs:
        nr = r + dr
        if 0 <= nr and nr < R:
            if graph[nr][c+1] == EMPTY:
                graph[nr][c+1] = PIPE
                result = dfs(c+1,nr)
                if result:
                    return result
    
    return result


if __name__ == "__main__":
    try:
        R, C = map(int, sys.stdin.readline().split(" "))
        graph = [list(map(ord, list(sys.stdin.readline().rstrip()))) for _ in range(R)]

        # rows = [[0 for _ in range(R)] for r in range(C)]
        
        # rows[0] = [1 for _ in range(R)]

        answer = 0
        
        for r in range(R):
            # visited = [[0 for _ in range(C)] for _ in range(R)]
            answer += dfs(0,r)
            
        print(answer)
           
    except ValueError or IndexError as e:
        print(e)