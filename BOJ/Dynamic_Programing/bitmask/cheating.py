# 컨닝
'''https://www.acmicpc.net/problem/1014'''

# Method1:
# 위의 줄의 값에 의해 밑에 들어갈 최대의 개수는 정해져 있다. 즉 다시 조사할 필요가 없다.
'''
import sys

sys.setrecursionlimit(10**8)

EMPTY = ord(".")
NOT_EMPTY = ord("x")

def check_row_seat(row, pre_number):
    rlt = []
    for idx, v in enumerate(graph[row]):
        if v == NOT_EMPTY:
            continue
        
        if idx == 0:
            if pre_number & (1 << (idx+1)):
                continue
        elif idx == M-1:
            if pre_number & (1 << (idx-1)):
                continue
        else:
            if pre_number & (1 << (idx-1)) or pre_number & (1 << (idx-1)):
                continue
        
        for cur in rlt[:]:
            if idx > 0 and (cur & (1 << (idx-1))) == 0:
                rlt.append(cur | (1 << (idx)))
        
        rlt.append((1 << (idx)))    
            
    
    return rlt
    
# def get_new_number(step, number):
#     return number | (1 << step)

# def get_before_row_number(step, number):
#     k = step//M - 1
#     return k, number & (BIN_NUM << (k*M))

# def get_now_row_number(step, number):
#     k = step//M
#     return k, number & (BIN_NUM << (k*M))
    

def dfs(row, pre_number, value):
    if row == N:
        return value
    
    if row > 0:
        pre_row = row - 1, 
        if pre_number in dp[pre_row]:
            return dp[pre_row][pre_number] + value
        
    # 현재 줄에 대해 입력가능한 배치 탐색 윗줄에 의해 결정 # 경우의 수 # O(M**2)
    is_available_numbers = check_row_seat(row, pre_number)
    
    # 입력가능한 배치를 기준으로 아랫줄을 결정
    for number in is_available_numbers:
        k = number.bit_count()
        pro_value = dfs(row, number, value+k) - value
        dp[row][number] = pro_value
        
    return pro_value + value
    
if __name__ == "__main__":
    try:
        C = int(sys.stdin.readline())
        answer = []
        for _ in range(C):
            N, M = map(int, sys.stdin.readline().split(" "))
            graph = [list(map(ord, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
            # for _ in range(N):
            #     graph += list(map(ord, list(sys.stdin.readline().rstrip()))) 

            max_value = 0
            dp = [dict() for _ in range(N)]
            
            k = dfs(0,0,0)
            
            print(k)
            
            
    except ValueError or IndexError as e:
        print(e)
       ''' 
       
# Refer : https://suri78.tistory.com/282

import sys

EMPTY, NOT_EMPTY = 0, 1

# 기본함수 
def func(x):
    return EMPTY if x=="." else NOT_EMPTY

# row에 앉을 수 있는 모든 경우의 수를 저장하자
# 모든 것을 고려하지 않는다
# 부셔진 책상, 앞, 뒤 줄의 학생 등
# 아래 함수를 통해 모든 경우의 수를 구할 수 있다.
def get_all(m):
    all_cases = [0]
    
    for idx in range(m):
        for cur in all_cases[1:]:
            if idx > 0 and cur & (1<<(idx-1)):
                continue
            all_cases.append(cur | (1<<idx))
        all_cases.append(1 << idx)
        
    return all_cases

# row == 0 부터 case에 대한 1의 개수를 count해서 저장하자.
def check_seat(row):
    if row == N:
        return 
    
    for now in all_cases:
        if now & graph[row]:
            continue
        
        if row == 0:
            dp[row][now] = now.bit_count()
        
        elif row > 0:
            for pre in dp[row-1].keys():
                if (now >> 1) & pre or (now << 1) & pre:
                    continue
                dp[row][now] = max(dp[row][now], dp[row-1][pre]+now.bit_count())
        
    check_seat(row+1)
    

    
if __name__ == "__main__":
    try:
        C = int(sys.stdin.readline())
        for _ in range(C):
            N, M = map(int, sys.stdin.readline().split(" "))
            graph = []
            for _ in range(N):
                list_ = list(map(func, list(sys.stdin.readline().rstrip())))
                list_.reverse()
                bin_ = 0
                for idx, k in enumerate(list_):
                    if k:
                        bin_ += (1 << idx)
                graph.append(bin_)
            
            all_cases = get_all(M)

            dp = [{case : 0 for case in all_cases} for _ in range(N)]
            
            # for c in all_cases:
            #     print("0"*(5 - len(bin(c)[2:])),bin(c)[2:], sep="")
            
            check_seat(0)
            
            print(max(dp[N-1].values()))
            

    except ValueError or IndexError as e:
        print(e)