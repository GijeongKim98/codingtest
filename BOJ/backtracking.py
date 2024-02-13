'''
# N과 M - 1

def get_seq(list_,M):
    len_ = len(list_)
    if M == 1:
        for i in range(len_):
            list_[i] = [list_[i]]
        return list_
    result = []
    for j in range(len_):
        part = list_[:j] + list_[j+1:]
        sub_result = get_seq(part,M-1)
        for k in range(len(sub_result)):
            sub_result[k] = [list_[j]] + sub_result[k]
        result += sub_result
    return result


try:
    N, M = tuple(map(int, input().split(' ')))
    list_ = list(range(1,N+1))
    result = get_seq(list_,M)
    for p in result:
        for q in p:
            print(q,end=' ')
        print()
except ValueError or IndexError:
    print('Input Error')

# 다른 풀이

n, m = tuple(map(int, input().split(' ')))
list_ = []
visited = [False] * (n+1)
def dfs(num):
    if len(list_) == m:
        print(list_)
        return

    for i in range(1,n+1):
        if visited[i]:
            continue

        visited[i] = True
        list_.append(i)
        dfs(i)
        list_.pop()
        visited[i] = False
dfs(1)


# N과 M - 2

def get_seq_v2(list_,M):
    len_ = len(list_)
    if M == 1:
        for i in range(len_):
            list_[i] = [list_[i]]
        return list_
    result = []
    for j in range(len_):
        part = list_[j+1:]
        sub_result = get_seq_v2(part,M-1)
        for k in range(len(sub_result)):
            sub_result[k] = [list_[j]] + sub_result[k]
        result += sub_result
    return result

# print(get_seq_v2([1,2,3,4],3))

try:
    N, M = tuple(map(int, input().split(' ')))
    list_ = list(range(1,N+1))
    result = get_seq_v2(list_,M)
    for p in result:
        for q in p:
            print(q,end=' ')
        print()
except ValueError or IndexError:
    print('Input Error')

# 다른 풀이

n, m = tuple(map(int, input().split(' ')))
list_ = []
visited = [False] * (n+1)
def dfs(num):
    if len(list_) == m:
        print(list_)
        return

    for i in range(num,n+1):
        if visited[i]:
            continue

        visited[i] = True
        list_.append(i)
        dfs(i)
        list_.pop()
        visited[i] = False
dfs(1)

# N과 M - 3

def get_seq_v3(list_,m):
    len_ = len(list_)
    if m == 1:
        for i in range(len_):
            list_[i] = [list_[i]]
        return list_
    result_ = []
    for j in range(len_):
        part = list_[:]
        sub_result = get_seq_v3(part,m-1)
        for k in range(len(sub_result)):
            sub_result[k] = [list_[j]] + sub_result[k]
        result_ += sub_result
    return result_


try:
    N, M = tuple(map(int, input().split(' ')))
    list_ = list(range(1,N+1))

    result = get_seq_v3(list_,M)

    for p in result:
        for q in p:
            print(q,end=' ')
        print()
except ValueError or IndexError:
    print('Input Error')

# 다른 풀이
try:
    n, m = tuple(map(int, input().split(' ')))
    list_ = []
    def dfs(num):
        if len(list_) == m:
            print(' '.join(map(str,list_)))
            return

        for i in range(1,n+1):

            list_.append(i)
            dfs(i)
            list_.pop()
    dfs(1)
except ValueError or IndexError:
    print("Input Error")

'''

'''
# N과 M -4

try:
    n, m = tuple(map(int, input().split(' ')))
    list_ = []
    def dfs(num):
        if len(list_) == m:
            print(' '.join(map(str,list_)))
            return

        for i in range(num,n+1):

            list_.append(i)
            dfs(i)
            list_.pop()
    dfs(1)
except ValueError or IndexError:
    print("Input Error")

'''
# N - Queen
'''
try:
    N = int(input())
    board = [0] + [-1] * (N**2)
    result = 0
    queen_index = [] # queen이 놓인 위치 x, y => x*N+y

    # board 초기화
    def init_board(index, count): # 지금 놓은 퀸의 위치, queen의 개수
        r = index % N
        r = (r if r != 0 else N)
        for i in range(index, index+N-r+1):
            if board[i] < 0:
                board[i] = count
        k = 1
        for j in range(index+N,N*N+1,N):
            if board[j] < 0:
                board[j] = count
            if k < r and board[j-k] < 0:
                board[j-k] = count
            if k <= N-r and board[j+k] < 0:
                board[j+k] = count
            k += 1

    # 이전 보드로 되돌리기
    def pre_board(start,count):
        for i in range(start,N**2+1):
            if board[i] > count:
                board[i] = -1

    # 백트래킹 코드
    def dfs(num):
        global result
        if len(queen_index) == N:
            result += 1
            # print(queen_index)
            return

        for i in range(num,N*N+1):
            if board[i] == -1:
                queen_index.append(i)
                # print(queen_index)
                init_board(i,len(queen_index))
                dfs(i)
                pre_index = queen_index.pop()
                # print(f'pre_index : {pre_index} // i : {i}')
                # print(queen_index)
                pre_board(i,len(queen_index))
                board[pre_index] = len(queen_index)
    dfs(1)
    print(result)
except ValueError:
    print('Input Error')



# N - Queen

try:
    N = int(input())
    board = [0] + [N+1] * (N**2)
    result1 = 0
    queen_index = [] # queen이 놓인 위치 x, y => x*N+y

    # board 초기화
    def init_board(index, count): # 지금 놓은 퀸의 위치, queen의 개수
        r = index % N
        r = (r if r != 0 else N)
        for i in range(index, index+N-r+1):
            if board[i] > count:
                board[i] = count
        k = 1
        for j in range(index+N,N*N+1,N):
            if board[j] > count:
                board[j] = count
            if k < r and board[j-k] > count:
                board[j-k] = count
            if k <= N-r and board[j+k] > count:
                board[j+k] = count
            k += 1

    # 이전 보드로 되돌리기
    def pre_board(start,count):
        for i in range(start,N**2+1):
            if board[i] > count:
                board[i] = N

    # 백트래킹 코드
    def dfs(num):
        global result1
        if len(queen_index) == N:
            result1 += 1
            # print(queen_index)
            return

        for i in range(num,N*N+1):
            if board[i] > len(queen_index):
                queen_index.append(i)
                # print(queen_index)
                init_board(i,len(queen_index))
                dfs(i)
                pre_index = queen_index.pop()
                # print(f'pre_index : {pre_index} // i : {i}')
                # print(queen_index)
                # pre_board(i,len(queen_index))
                board[pre_index] = len(queen_index)
    dfs(1)
    print(result1)
except ValueError:
    print('Input Error')
# n_queen 문제 해결
# 백트래킹
# nxn 에 n개의 퀸을 배치 서로 공격 불가

try:
    N = int(input())
    row = [0] * N
    result = 0

    def is_promising(x):
        for i in range(x):
            if row[i] == row[x] or abs(row[x] - row[i]) == abs(x - i):
                return False
        return True

    def dfs(x):
        global result
        if x == N:
            result += 1
            return
        for i in range(N):
            row[x] = i
            if is_promising(x):
                dfs(x+1)

    dfs(0)
    print(result)
except ValueError:
    print('Input Error')


# 스도쿠
#
import sys
try:
    sudoku = []
    rlt = []
    for i in range(9):
        str_ = input().split(' ')
        for j, char in enumerate(str_):
            num = int(char)
            if num == 0:
                rlt.append(i*9 + j)
            sudoku.append(num)

    depth = len(rlt)

    def is_promising(index,n):
         r = index // 9
         c = index % 9

         q = 3 * (r // 3)
         p = 3 * (c // 3)
         k = q * 9 + p

         for row in range(r*9,r*9+9):
             if n == sudoku[row]:
                 return False

         for col in range(c,81,9):
             if n == sudoku[col]:
                 return False

         for i in range(k,k+19,9):
             for j in range(i,i+3):
                 if n == sudoku[j]:
                     return False

         return True

    def print_sudoku():
        for i in range(9):
            for j in range(9):
                print(sudoku[i*9+j], end = ' ')
            print()


    def dfs(number):
        # print(f'number = {number}')
        # print(depth)
        if number == depth:
            print_sudoku()
            sys.exit()

        for num in range(1,10):
            if is_promising(rlt[number],num):
                sudoku[rlt[number]] = num

                # print(f'num = {num}')
                # print(sudoku[rlt[number]])
                dfs(number+1)
                sudoku[rlt[number]] = 0
    dfs(0)

except ValueError or IndexError:
    print("Input Error")


# 연산자 끼워 넣기

try:
    N = int(input())
    numbers = list(map(int,input().split(' ')))
    operator_ = list(map(int, input().split(' ')))

    max_ = -1000000000
    min_ = 1000000000
    rlt = 0

    def division(x,y):
        if x < 0:
            x *= -1
            return (x // y) * -1
        return x // y



    def dfs(number):
        global rlt, max_, min_
        if number == N-1:
            max_ = (max_ if max_ > rlt else rlt)
            min_ = (min_ if min_ < rlt else rlt)
            return


        a = (numbers[0] if number == 0 else rlt)
        b = numbers[number+1]
        for j in range(4):
            if operator_[j] > 0:
                if j == 0:
                    rlt = a + b
                elif j == 1:
                    rlt = a - b
                elif j == 2:
                    rlt = a * b
                else:
                    rlt = division(a,b)

                operator_[j] -= 1
                dfs(number+1)
                operator_[j] += 1

    dfs(0)
    print(max_)
    print(min_)

except ValueError or IndexError or ZeroDivisionError:
    print("Input Error")

'''
'''

# 스타트와 링크
# 절반을 나눠서 하면 start 14 link 23 // start23 link 14는 같은 결과
# 따라서 첫번째 선수를 스타트에 넣고 진행 중복을 방지함
import sys

try:
    N = int(input())

    s_list = []

    for i in range(N):
        s_i = list(map(int, input().split(' ')))
        s_list.append(s_i)

    delta = 1000
    start_ = {0}
    u = set(range(N))

    # 팀 점수 계산하는 함수
    def cal_score(l):
        sum_ = 0
        for i in l:
            for j in l:
                sum_ += s_list[i][j]
        return sum_

    # 링크팀 추출하는 함수
    def get_link(start):
        set_ = set(start)
        l_set_ = set(range(N)) - set_
        return list(l_set_)

    def dfs(number):
        global delta
        if number == N//2:
            link_ = u - start_
            num_d = abs(cal_score(list(start_)) - cal_score(list(link_)))
            if num_d == 0:
                print(0)
                sys.exit()
            elif delta > num_d:
                delta = num_d
            return

        for i in range(number,N):
            start_.add(i)
            dfs(number+1)
            start_.remove(i)

    dfs(1)
    print(delta)

except ValueError or IndexError:
    print("Input Error")
'''

# 다른 풀이

# visited list = true, false list

import sys
try:
    N = int(input())
    s_list = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(N)]


    delta = 2000
    visited = [True] + [False] * (N - 1)


    def dfs(idx, number):
        global delta
        if number == N//2:
            link_ = 0
            start_ = 0
            for i in range(N):
                for j in range(i+1,N):
                    if visited[i] and visited[j]:
                        start_ += s_list[i][j] + s_list[j][i]
                    elif not visited[i] and not visited[j]:
                        link_ += s_list[i][j] + s_list[j][i]

            delta = min(delta, abs(start_ - link_))
            return

        for i in range(idx,N):
            if not visited[i]:
                visited[i] = True
                dfs(i+1,number+1)
                visited[i] = False

    dfs(1,1)
    print(delta)
except ValueError or IndexError:
    print("Input Error")









