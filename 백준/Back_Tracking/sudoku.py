# 스도쿠
'''https://www.acmicpc.net/problem/2239'''

import sys

NUMBERS = [1,2,3,4,5,6,7,8,9]

MAX_NUM = 9

def dfs(step):
    if step == N:
        print_board()
        sys.exit()
    
    now = located_0[step]
    for number in NUMBERS:
        if is_possible_location(number, now):
            board[now] = number
            dfs(step+1)
            board[now] = 0
    return

def is_possible_location(number, place):
    q = place // MAX_NUM
    r = place % MAX_NUM
    
    # 가로
    for l in range(q*MAX_NUM, q*MAX_NUM+MAX_NUM):
        if board[l] == number:
            return False    
    
    # 세로
    for l in range(r, MAX_NUM * MAX_NUM, MAX_NUM):
        if board[l] == number:
            return False
    
    # 칸
    s = (q//3) * 3 * MAX_NUM + (r//3) * 3
    
    for l in range(s, s+3):
        for c in range(0,27,9):
            if board[l+c] == number:
                return False
    
    return True

def print_board():
    for idx, number in enumerate(board):
        if (idx+1) % 9 == 0:
            print(number)
        else:
            print(number, end="")

if __name__ == "__main__":
    try:
        board = []
        located_0 = []
        
        for i in range(MAX_NUM):
            input_numbers = list(sys.stdin.readline().rstrip())
            for j, num in enumerate(input_numbers):
                board.append(int(num))
                if not int(num):
                    located_0.append(i * MAX_NUM + j)
        
        N = len(located_0)
        dfs(0)
                    
    except ValueError or IndexError as e:
        print(e)