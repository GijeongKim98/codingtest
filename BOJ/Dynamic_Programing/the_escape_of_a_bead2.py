# 구슬 탈출2
'''https://www.acmicpc.net/problem/13460'''
'''
import sys
from collections import deque

WALL = ord("#")
EMPTY = ord(".")
RED = ord("R")
BLUE = ord("B")
HOLE = ord("O")
MAX_STEP = 10

LEFT, RIGHT, UP, DOWN = 1,2,3,4
directions = {LEFT:(-1,0), RIGHT:(1,0), UP:(0,-1), DOWN:(0,1)}

# 기울리기 함수
# def tilting_two_bead(r_x, r_y, b_x, b_y, direction):
#     if direction == LEFT:
#         bool_ = r_x < b_x
    
#     elif direction == RIGHT:
#         bool_ = b_x < r_x
    
#     elif direction == UP:
#         bool_ = r_y < b_y
    
#     elif direction == DOWN:
#         bool_ = b_y < r_y
        
    
#     if bool_:
#         n_r_x, n_r_y, is_hole = tilting_one_bead(r_x,r_y,direction)
#         if not is_hole:
#             board[r_y][r_x], board[n_r_y][n_r_x] = board[n_r_y][n_r_x], board[r_y][r_x]
#         else:
#             board[n_r_y][n_r_x], board[r_y][r_x] = HOLE, EMPTY
#         n_b_x, n_b_y, is_hole = tilting_one_bead(b_x,b_y,direction)
#         if not is_hole:
#             board[n_b_y][n_b_x], board[b_y][b_x] = board[b_y][b_x], board[n_b_y][n_b_x]
#         else:
#             board[n_b_y][n_b_x], board[b_y][b_x] = HOLE, EMPTY
#     else:
#         n_b_x, n_b_y, is_hole = tilting_one_bead(b_x,b_y,direction)
#         if not is_hole:
#             board[n_b_y][n_b_x], board[b_y][b_x] = board[b_y][b_x], board[n_b_y][n_b_x]
#         else:
#             board[n_b_y][n_b_x], board[b_y][b_x] = HOLE, EMPTY
            
#         n_r_x, n_r_y, is_hole = tilting_one_bead(r_x,r_y,direction)
#         if not is_hole:
#             board[n_r_y][n_r_x], board[r_y][r_x] = board[r_y][r_x], board[n_r_y][n_r_x]
#         else:
#             board[n_r_y][n_r_x], board[r_y][r_x] = HOLE, EMPTY
    
#     return n_r_x, n_r_y, n_b_x, n_b_y


def tilting_two_bead(r_x, r_y, b_x, b_y, direction):
    if direction == LEFT:
        bool_ = r_x < b_x
    
    elif direction == RIGHT:
        bool_ = b_x < r_x
    
    elif direction == UP:
        bool_ = r_y < b_y
    
    elif direction == DOWN:
        bool_ = b_y < r_y
        
    
    if bool_:
        n_r_x, n_r_y, is_hole = tilting_one_bead(r_x,r_y,direction)
        if not is_hole:
            board[r_y][r_x], board[n_r_y][n_r_x] = board[n_r_y][n_r_x], board[r_y][r_x]
        else:
            board[n_r_y][n_r_x], board[r_y][r_x] = HOLE, EMPTY
        n_b_x, n_b_y, is_hole = tilting_one_bead(b_x,b_y,direction)
        if not is_hole:
            board[n_b_y][n_b_x], board[b_y][b_x] = board[b_y][b_x], board[n_b_y][n_b_x]
        else:
            board[n_b_y][n_b_x], board[b_y][b_x] = HOLE, EMPTY
    else:
        n_b_x, n_b_y, is_hole = tilting_one_bead(b_x,b_y,direction)
        if not is_hole:
            board[n_b_y][n_b_x], board[b_y][b_x] = board[b_y][b_x], board[n_b_y][n_b_x]
        else:
            board[n_b_y][n_b_x], board[b_y][b_x] = HOLE, EMPTY
            
        n_r_x, n_r_y, is_hole = tilting_one_bead(r_x,r_y,direction)
        if not is_hole:
            board[n_r_y][n_r_x], board[r_y][r_x] = board[r_y][r_x], board[n_r_y][n_r_x]
        else:
            board[n_r_y][n_r_x], board[r_y][r_x] = HOLE, EMPTY
    
    return n_r_x, n_r_y, n_b_x, n_b_y       
            
def tilting_one_bead(x, y, direction):
    n_x, n_y = x, y
    next_x, next_y = n_x+directions[direction][0], n_y+directions[direction][1] 
    while board[next_y][next_x] == EMPTY:
        n_x, n_y = next_x, next_y
        next_x, next_y = n_x+directions[direction][0], n_y+directions[direction][1] 
        
    if board[next_y][next_x] == HOLE:
        return next_x, next_y, True
    
    return n_x, n_y, False
    
    

def dfs(red_x, red_y, blue_x, blue_y, step):
    global answer
    if step == MAX_STEP:
        return False
    
    if dp[red_y][red_x][blue_y][blue_x][step]:
        return False
    
    dp[red_y][red_x][blue_y][blue_x][step] = 1
    
    for direction in directions.keys():
        n_r_x, n_r_y, n_b_x, n_b_y = tilting_two_bead(red_x, red_y, blue_x, blue_y, direction)
        
        if n_r_x == hole_x and n_r_y == hole_y:
            if not (n_b_x != hole_x or n_b_y != hole_y):
                answer = min(answer, step+1)
                return True
            else:
                board[red_y][red_x], board[blue_y][blue_x] = RED, BLUE
                continue
        
        if n_r_x == red_x and n_r_y == red_y and n_b_x == blue_x and n_b_y == blue_y:
            continue
        
        if dfs(n_r_x, n_r_y, n_b_x, n_b_y, step+1):
            return True
        
        
        board[red_y][red_x], board[blue_y][blue_x] = RED, BLUE
        board[n_r_y][n_r_x], board[n_b_y][n_b_x] = EMPTY, EMPTY
    
    return False

def move_two_beads(r_x, r_y, b_x, b_y, direction):
    if direction == LEFT:
        bool_ = r_x < b_x
    
    elif direction == RIGHT:
        bool_ = b_x < r_x
    
    elif direction == UP:
        bool_ = r_y < b_y
    
    elif direction == DOWN:
        bool_ = b_y < r_y
        
    if bool_:
        # RED먼저 이동
        n_r_x, n_r_y = move_a_bead(r_x, r_y, b_x, b_y, direction)
        n_b_x, n_b_y = move_a_bead(b_x, b_y, n_r_x, n_r_y, direction)
        
    else:
        # BLUE 먼저 이동
        n_b_x, n_b_y = move_a_bead(b_x, b_y, r_x, r_y, direction)
        n_r_x, n_r_y = move_a_bead(r_x, r_y, n_b_x, n_b_y, direction)
        
    return n_r_x, n_r_y, n_b_x, n_b_y

def move_a_bead(x, y, another_x, another_y, direction):
    n_x, n_y = x, y
    next_x, next_y = n_x + directions[direction][0], n_y + directions[direction][1]
    while (next_x != another_x or next_y != another_y) and board[next_y][next_x] == EMPTY:
        n_x, n_y = next_x, next_y
        next_x, next_y = n_x + directions[direction][0], n_y + directions[direction][1]
    
    if board[next_y][next_x] == HOLE:
        return next_x, next_y
    
    return n_x, n_y
        

def bfs(red_x, red_y, blue_x, blue_y):
    queue = deque([(red_x, red_y, blue_x, blue_y)])
    dp[red_x][red_y][blue_x][blue_y] = 1
    while queue:
        p_r_x, p_r_y, p_b_x, p_b_y = queue.popleft()
        for direction in directions:
            n_r_x, n_r_y, n_b_x, n_b_y = move_two_beads(p_r_x, p_r_y, p_b_x, p_b_y, direction)
            if n_r_x == hole_x and n_r_y == hole_y:
                if n_b_x != hole_x or n_b_y != hole_y:
                    return dp[p_r_x][p_r_y][p_b_x][p_b_y]
                continue
            
            if not dp[n_r_x][n_r_y][n_b_x][n_b_y]:
                queue.append((n_r_x, n_r_y, n_b_x, n_b_y))
                dp[n_r_x][n_r_y][n_b_x][n_b_y] = dp[p_r_x][p_r_y][p_b_x][p_b_y] + 1
    
    return -1
    


if __name__ == "__main__":
    try:
        N, M = map(int, sys.stdin.readline().split(" "))
        board = [list(map(ord, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
        dp = [[[[0 for _ in range(N)]for _ in range(M)]for _ in range(N)]for _ in range(M)]
        
        for i in range(N):
            for j in range(M):
                if board[i][j] == RED:
                    red_x, red_y = j, i
                    board[i][j] = EMPTY
                    
                elif board[i][j] == BLUE:
                    blue_x, blue_y = j, i
                    board[i][j] = EMPTY
                    
                elif board[i][j] == HOLE:
                    hole_x, hole_y = j, i            
        
        # tilting_two_bead(red_x, red_y, blue_x, blue_y,RIGHT)
        
        # print(*board,sep="\n")
        
        # answer = MAX_STEP+1
        # if dfs(red_x, red_y, blue_x, blue_y, 0):
        #     print(answer)
        # else:
        #     print(-1)
        
        print(bfs(red_x, red_y, blue_x, blue_y))
        
    except ValueError or IndexError as e:
        print(e)
        
        '''
        
# 구슬 탈출2
'''https://www.acmicpc.net/problem/13460'''

import sys
from collections import deque

WALL = ord("#")
EMPTY = ord(".")
RED = ord("R")
BLUE = ord("B")
HOLE = ord("O")
MAX_STEP = 10

LEFT, RIGHT, UP, DOWN = 1,2,3,4
directions = {LEFT:(-1,0), RIGHT:(1,0), UP:(0,-1), DOWN:(0,1)}

def move_two_beads(r_x, r_y, b_x, b_y, direction):
    if direction == LEFT:
        bool_ = r_x < b_x
    
    elif direction == RIGHT:
        bool_ = b_x < r_x
    
    elif direction == UP:
        bool_ = r_y < b_y
    
    elif direction == DOWN:
        bool_ = b_y < r_y
        
    if bool_:
        # RED먼저 이동
        n_r_x, n_r_y = move_a_bead(r_x, r_y, b_x, b_y, direction)
        n_b_x, n_b_y = move_a_bead(b_x, b_y, n_r_x, n_r_y, direction)
        
    else:
        # BLUE 먼저 이동
        n_b_x, n_b_y = move_a_bead(b_x, b_y, r_x, r_y, direction)
        n_r_x, n_r_y = move_a_bead(r_x, r_y, n_b_x, n_b_y, direction)
        
    return n_r_x, n_r_y, n_b_x, n_b_y

def move_a_bead(x, y, another_x, another_y, direction):
    n_x, n_y = x, y
    next_x, next_y = n_x + directions[direction][0], n_y + directions[direction][1]
    while (next_x != another_x or next_y != another_y) and board[next_y][next_x] == EMPTY:
        n_x, n_y = next_x, next_y
        next_x, next_y = n_x + directions[direction][0], n_y + directions[direction][1]
    
    if board[next_y][next_x] == HOLE:
        return next_x, next_y
    
    return n_x, n_y
        

def bfs(red_x, red_y, blue_x, blue_y):
    queue = deque([(red_x, red_y, blue_x, blue_y)])
    dp[red_x][red_y][blue_x][blue_y] = 1
    while queue:
        p_r_x, p_r_y, p_b_x, p_b_y = queue.popleft()
        
        if dp[p_r_x][p_r_y][p_b_x][p_b_y] > 10:
            return -1
        
        for direction in directions:
            n_r_x, n_r_y, n_b_x, n_b_y = move_two_beads(p_r_x, p_r_y, p_b_x, p_b_y, direction)
            if n_r_x == hole_x and n_r_y == hole_y:
                if n_b_x != hole_x or n_b_y != hole_y:
                    return dp[p_r_x][p_r_y][p_b_x][p_b_y]
            
            if n_b_x == hole_x and n_b_y == hole_y:
                continue
            
            if not dp[n_r_x][n_r_y][n_b_x][n_b_y]:
                queue.append((n_r_x, n_r_y, n_b_x, n_b_y))
                dp[n_r_x][n_r_y][n_b_x][n_b_y] = dp[p_r_x][p_r_y][p_b_x][p_b_y] + 1
    
    return -1
    


if __name__ == "__main__":
    try:
        N, M = map(int, sys.stdin.readline().split(" "))
        board = [list(map(ord, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
        dp = [[[[0 for _ in range(N)]for _ in range(M)]for _ in range(N)]for _ in range(M)]
        
        for i in range(N):
            for j in range(M):
                if board[i][j] == RED:
                    red_x, red_y = j, i
                    board[i][j] = EMPTY
                    
                elif board[i][j] == BLUE:
                    blue_x, blue_y = j, i
                    board[i][j] = EMPTY
                    
                elif board[i][j] == HOLE:
                    hole_x, hole_y = j, i
        
        print(bfs(red_x, red_y, blue_x, blue_y))
        
    except ValueError or IndexError as e:
        print(e)