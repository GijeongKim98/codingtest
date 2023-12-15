# 2048 (Easy)
'''https://www.acmicpc.net/problem/12100'''

import sys

LAST = 5

EMPTY = 0

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

directions = [LEFT, RIGHT, UP, DOWN]

# 이동함수
def move(board, direction):
    if direction == LEFT:
        new_board = []
        for i in range(N):
            list_ = []
            pre_number = board[i][0]
            for j in range(1, N): 
                if board[i][j] == EMPTY:
                    continue
                if not pre_number and board[i][j]:
                    pre_number = board[i][j]
                
                elif pre_number == board[i][j]:
                    list_.append(2*pre_number)
                    pre_number = 0
        
                else:
                    list_.append(pre_number)
                    pre_number = board[i][j]
            
            list_.append(pre_number)
                    
            count_add_empty = N - len(list_)
            
            new_board.append(list_ + [0]*count_add_empty)
    
    elif direction == RIGHT:
        new_board = []

        for i in range(N):
            list_ = []
            pre_number = board[i][N-1]
            for j in range(N-2, -1, -1): 
                if board[i][j] == EMPTY:
                    continue
                if not pre_number and board[i][j]:
                    pre_number = board[i][j]
                
                elif pre_number == board[i][j]:
                    list_.append(2*pre_number)
                    pre_number = 0
        
                else:
                    list_.append(pre_number)
                    pre_number = board[i][j]
            
            list_.append(pre_number)
                    
            count_add_empty = N - len(list_)
            
            list_.reverse()
            
            new_board.append([0]*count_add_empty + list_)
            
    elif direction == UP:
        new_board = [[] for _ in range(N)]
        for j in range(N):
            list_ = []
            pre_number = board[0][j]
            for i in range(1,N):
                if board[i][j] == EMPTY:
                    continue
                if not pre_number and board[i][j]:
                    pre_number = board[i][j]
                
                elif pre_number == board[i][j]:
                    list_.append(2*pre_number)
                    pre_number = 0
        
                else:
                    list_.append(pre_number)
                    pre_number = board[i][j]
            
            list_.append(pre_number)
            
            for idx in range(N):
                new_board[idx].append(list_[idx] if idx < len(list_) else 0)
    
    elif direction == DOWN:
        new_board = [[] for _ in range(N)]
        for j in range(N):
            list_ = []
            pre_number = board[N-1][j]
            for i in range(N-2,-1,-1):
                if board[i][j] == EMPTY:
                    continue
                if not pre_number and board[i][j]:
                    pre_number = board[i][j]
                
                elif pre_number == board[i][j]:
                    list_.append(2*pre_number)
                    pre_number = 0
        
                else:
                    list_.append(pre_number)
                    pre_number = board[i][j]
            
            list_.append(pre_number)
            
            for idx in range(N):
                new_board[N-1-idx].append(list_[idx] if idx < len(list_) else 0)
                
    return new_board

def find_max(board):
    max_ = 0
    for r in board:
        max_r = max(r)
        max_ = max(max_r, max_)
    return max_

def dfs(board, step):
    global answer
    if step == LAST:
        answer = max(answer, find_max(board))
        # print(answer)
        return
    # if (board, step) in dp:
    #     return 
    
    # dp[(board, step)] = True
    
    for dir in directions:
        dfs(move(board,dir), step+1)
    
    return
    
    

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        # dp = dict()
        
        answer = 0
        
        # # print(move(board, DOWN))
        # board = move(move(move(board, LEFT), LEFT), LEFT)
        
        # print(board)
        dfs(board, 0)
        print(answer)

    except ValueError or IndexError as e:
        print(e)
