# 사다리 조작
'''https://www.acmicpc.net/problem/15684'''

# Method : brute force

import sys
from itertools import combinations

EMPTY, PAINTING, PAINTED = 0, 1, 2

def func(x):
    return int(x) - 1

def check():
    for col_idx in range(N):
        now = col_idx
        for row in range(H):
            if now > 0 and lines_info[row][now-1]:
                now -= 1
            elif now < N-1 and lines_info[row][now]:
                now += 1
        
        if now != col_idx:
            return False
    
    return True        
            
        

def delete_lines(c):
    for x, y in c:
        lines_info[y][x] = EMPTY

def add_lines(c):
    for x, y in c:
        lines_info[y][x] = PAINTING
    

def is_c_possible(c):
    for x, y in c:
        # 이미 그려진 경우
        if lines_info[y][x] == PAINTED:
            return False
        
        if N > 3:
            # x == 0 일때 = 가장 왼쪽 선
            if x == 0:
                if lines_info[y][x+1] == PAINTED:
                    return False
            
            # x == N-2 일때 = 가장 오른쪽 선
            elif x == N-2:
                if lines_info[y][x-1] == PAINTED:
                    return False
            
            # 그 외의 경우 
            else:
                if lines_info[y][x-1] == PAINTED or lines_info[y][x+1] == PAINTED:
                    return False
    
    return True
            

def coordinate_transformation(c):
    two_demensions = []
    for k in c:
        x, y = k%(N-1), k//(N-1)
        two_demensions.append((x,y))
    
    return two_demensions

if __name__ == "__main__":
    try:
        N, M, H = map(int, sys.stdin.readline().split(" "))

        possible_lines = [i for i in range((N-1)*H)]
        lines_info = [[EMPTY for _ in range(N-1)] for _ in range(H)]
        
        for _ in range(M):
            r, c = map(func, sys.stdin.readline().split(" "))
            lines_info[r][c] = PAINTED
        
        cases = []
        
        for number_of_lines in range(4):
            answer = number_of_lines
            if not number_of_lines:
                if check():
                    break
            else:
                break_temp = 0
                cases = combinations(possible_lines, number_of_lines)
                for c in cases:
                    c = coordinate_transformation(c)
                    if is_c_possible(c):
                        add_lines(c)
                        if check():
                            break_temp = 1
                            break
                        delete_lines(c)
                
                if break_temp:
                    break
            answer = -1
        
        print(answer)
        
        
    except ValueError or IndexError as e:
        print(e)

