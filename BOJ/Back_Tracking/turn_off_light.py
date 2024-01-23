# 불 끄기
'''https://www.acmicpc.net/problem/14939'''

import sys

# sys.setrecursionlimit(10**7)

CONST = 10
NUMBER_BOARD = 100
SELF, UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3, 4 
DIRECTIONS = [0, 10, -10, -1, 1]
IMPOSSIBLE = -1


def trans_light(p, board, directions):
    new_board = board
    for i, is_dir in enumerate(directions):
        if not is_dir:
            continue
        binary_num = (1 << p+DIRECTIONS[i])
        if binary_num & board: # 불이 켜진 경우
            new_board = ~binary_num & new_board
        else: # 불이 켜지지 않은 경우
            new_board = binary_num | new_board

    return new_board
    
def press(p, board):
    directions = [1 for _ in range(5)]
    
    if p > 90:
        directions[UP] = 0
    
    elif p < 10:
        directions[DOWN] = 0
    
    if p % 10 == 0:
        directions[LEFT] = 0
    
    elif p % 10 == 9:
        directions[RIGHT] = 0
    
    new_board = trans_light(p, board, directions)
    return new_board

def get_count(board):
    count = 0
    for place in range(CONST, NUMBER_BOARD):
        if (1 <<(place-CONST)) & board:
            count += 1
            board = press(place, board)
    
    for p in range(CONST):
        if (1 << (90+p)) & board:
            return IMPOSSIBLE
    
    return count
                
                
def dfs(step, board, c):
    global answer
    
    if step >= 10:
        pro_count = get_count(board)    
        if pro_count != IMPOSSIBLE:
            answer = min(answer, c+pro_count)
        
        return 

    dfs(step+1, board, c)
    dfs(step+1,press(step,board), c+1)
    
if __name__ == "__main__":
    try:
        lights_100 = [sys.stdin.readline().rstrip() for _ in range(CONST)]

        board = 0
        answer = 1000
        
        for i, lights_10 in enumerate(lights_100):
            for j, light in enumerate(lights_10):
                if light == "O":
                    board += (1 << (i*10 + j))
        
        dfs(0,board,0)
        
        print(answer)
            
    except ValueError or IndexError as e:
        print(e)