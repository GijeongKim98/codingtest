# 낚시왕
'''https://www.acmicpc.net/problem/17143'''

import sys

UP, DOWN, RIGHT, LEFT = 1,2,3,4

directions = {1:(0,-1),2:(0,1),3:(1,0),4:(-1,0)}

def get_next_d(d):
    if d == 1:
        return 2
    elif d == 2:
        return 1
    elif d == 3:
        return 4
    else:
        return 3 

def get_next_p(r,c,s,d):
    dx, dy = directions[d]
    n_r, n_c = r+((dy*s)%(2*(R-1))), c+((dx*s)%(2*(C-1)))
    
    if n_r >= R:
        d = get_next_d(d)
        n_r = R - (n_r - R + 2) 
        if n_r < 0:
            d = get_next_d(d)
            n_r = -1 * n_r     # = 3
    elif n_r < 0: # -5 
        d = get_next_d(d)
        n_r = -1 * n_r # 5
        if n_r >= R:
            d = get_next_d(d)
            n_r = R - (n_r - R + 2)
            
    elif n_c >= C:
        d = get_next_d(d)
        n_c = C - (n_c - C + 2) # TODO
        if n_c < 0:
            d = get_next_d(d)
            n_c = n_c * -1 
    elif n_c < 0:
        d = get_next_d(d)
        n_c = n_c * -1
        if n_c >= C:
            d = get_next_d(d)
            n_c = C - (n_c - C + 2)
        
    return n_r, n_c, d
    

def move_sharks(board, sharks):
    for id, shark in enumerate(sharks):
        if not shark:
            continue
        
        r,c,s,d,z = shark
        
        if id == board[r][c]:
            board[r][c] = -1
        
        n_r, n_c, n_d = get_next_p(r,c,s,d)        
        
        if board[n_r][n_c] >= 0:
            another_shark_id = board[n_r][n_c]
            if sharks[another_shark_id][-1] < z:
                sharks[another_shark_id] = []
        
        board[n_r][n_c] = id
        
        sharks[id][0], sharks[id][1], sharks[id][3] = n_r, n_c, n_d
          
    
if __name__ == "__main__":
    
    try: 
        
        R, C, M = map(int, sys.stdin.readline().split(" "))
        sharks = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
        
        sharks.sort(key=lambda x: x[-1])
        
        board = [[-1 for _ in range(C)] for _ in range(R)]
        
        for id, shark in enumerate(sharks):
            r, c = shark[0] - 1, shark[1] - 1
            sharks[id][0], sharks[id][1] = r, c
            board[r][c] = id 
        
        answer = 0
        
        for col in range(C):
            for r in range(R):
                if board[r][col] >= 0:
                    id, board[r][col] = board[r][col], -1
                    answer += sharks[id][-1]
                    sharks[id] = []
                    break
            
            move_sharks(board, sharks)
        
        print(answer)
    
    except ValueError or IndexError as e:
        print(e)