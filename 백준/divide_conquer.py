# 색종이 만들기
'''https://www.acmicpc.net/problem/2630'''
'''
import sys
try:

    def divide(point, n):
        x, y = point

        if n > 1:
            n = n//2
            b1,w1 = divide((x,y),n)
            b2,w2 = divide((x+n,y),n)
            b3,w3 = divide((x,y+n), n)
            b4,w4 = divide((x+n,y+n), n)

            b = b1 + b2 + b3 + b4
            w = w1 + w2 + w3 + w4

            if b + w == 4 and abs(b-w) == 4:
                return (1,0) if b > w else (0,1)

            return b, w

        else:
            if board[y][x] == 0:
                return 0,1
            return 1,0

    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

    blue, white = divide((0,0), N)
    print(white)
    print(blue)

except ValueError or IndexError:
    print('Input Error')
'''

# 쿼드트리
'''https://www.acmicpc.net/problem/1992'''
'''
import sys
try:
    def dc(point,n):
        x, y = point
        if n == 1:
            return board[y][x]

        n = n // 2

        q1 = dc((x,y), n)
        q2 = dc((x+n, y), n)
        q3 = dc((x, y+n), n)
        q4 = dc((x+n,y+n), n)

        try:
            q = q1 + q2 + q3 + q4
            if q == 4:
                return 1
            elif q == 0:
                return 0
            else:
                return [q1,q2,q3,q4]

        except TypeError:
            return [q1,q2,q3,q4]


    N = int(sys.stdin.readline())
    board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]

    rlt = dc((0,0),N)
    print(str(rlt).replace('[','(').replace(']',')').replace(', ', ''))

except ValueError or IndexError:
    print('Input Error')
'''

# 종이의 개수
'''https://www.acmicpc.net/problem/1780'''
'''
# r g b = -1, 0, 1

import sys
try:

    def divide(point, n):
        x, y = point

        if n == 1:
            if board[y][x] == -1:
                return 1, 0, 0
            elif board[y][x] == 0:
                return 0, 1, 0
            return 0, 0, 1

        n = n//3
        r, g, b = 0,0,0

        for i in range(3):
            for j in range(3):
                rgb = divide((x+j*n,y+i*n),n)
                r += rgb[0]
                g += rgb[1]
                b += rgb[2]

        if r + g + b == 9:
            if r == 9:
                return 1,0,0
            elif g == 9:
                return 0,1,0
            elif b == 9:
                return 0,0,1

        return r,g,b



    N = int(sys.stdin.readline())
    board = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

    rlt = divide((0,0), N)
    for k in range(3):
        print(rlt[k])

except ValueError or IndexError:
    print('Input Error')

'''
# 곱셈
'''https://www.acmicpc.net/problem/1629'''
'''
import sys
try:
    def devide(a,b,c):
        if b <= 1:
            return a % c


        if b % 2 == 1:
            b = b // 2
            rlt1 = devide(a, b, c)
            rlt2 = devide(a,b+1,c)
            return (rlt1 * rlt2) % c

        b = b // 2
        rlt1 = devide(a, b, c)

        return (rlt1 * rlt1) % c


    A, B, C = tuple(map(int, sys.stdin.readline().split(' ')))
    print(devide(A,B,C))

except ValueError or IndexError:
    print('Input Error')
'''

# 이항계수 3
'''https://www.acmicpc.net/problem/11401'''
'''
import sys
try:
    N, K = tuple(map(int, sys.stdin.readline().split(' ')))
    p = 1000000007

    if N == K or K == 0:
        print(1)
        sys.exit()


    denominator = 1  # 분모
    molecule = 1  # 분자
    
    def factorial(a, p_):
        ans = 1
        for i in range(2,a+1):
            ans = (ans * i) % p_
        return ans
    
    for i in range(2,N+1):
        molecule = (molecule * i) % p
        if i == K or i == N-K:
            denominator = (denominator * molecule) % p

    def square(a, b, c):
        if b == 0:
            return 1
        elif b == 1:
            return a % c

        rlt_ = square(a,b//2,c)

        if b % 2 == 1:
            return (rlt_ * rlt_ * a) % c
        return (rlt_ * rlt_) % c

    denominator = square(denominator,p-2,p)
    
    n1, n2 = factorial(N,p), factorial(N-K,p)*factorial(K,p)
    
    rlt = (molecule * denominator) % p

    print(rlt)
except ValueError:
    print('Input Error')
'''
# 이항계수 3
'''https://www.acmicpc.net/problem/11401'''
'''
import sys

try:
    N, K = tuple(map(int, sys.stdin.readline().split(' ')))
    p = 1000000007

    if N == K or K == 0:
        print(1)
        sys.exit()



    def factorial(a, p_):
        ans = 1
        for i in range(2, a+1):
            ans = (ans * i) % p_
        return ans


    def square(a, b, c):
        if b == 0:
            return 1
        elif b == 1:
            return a % c

        rlt_ = square(a, b // 2, c)

        if b % 2 == 1:
            return (rlt_ * rlt_ * a) % c
        return (rlt_ * rlt_) % c



    n1, n2 = factorial(N, p), (factorial(N - K, p) * factorial(K, p))%p

    rlt = (n1*square(n2,p-2,p)) % p

    print(rlt)
except ValueError:
    print('Input Error')
'''
# 행렬 곱셈
'''https://www.acmicpc.net/problem/2740'''
'''
import sys
try:
    N,M = tuple(map(int, sys.stdin.readline().split(' ')))
    A = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
    M_,K = tuple(map(int, sys.stdin.readline().split(' ')))

    if M_ != M:
        print('Input Error')

    else:
        B = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(M_)]

        rlt = []
        for i in range(N):
            for j in range(K):
                sum_ = 0
                for k in range(M):
                    sum_ += A[i][k]*B[k][j]

                print(sum_, end=' ')
            print()

except ValueError or IndexError:
    print('Input Error')
'''
# 행렬 제곱
'''https://www.acmicpc.net/problem/10830'''
'''
import sys
try:
    def scalar_product(a,b,n):
        rlt = []
        for i in range(n):
            list_ = []
            for j in range(n):
                sum_ = 0
                for k in range(n):
                    sum_ += a[i][k]*b[k][j]
                    sum_ = sum_ % 1000
                list_.append(sum_)
            rlt.append(list_)
        return rlt

    def square(a,n,m):
        if m == 1:
            return a
        result = square(a,n,m//2)
        if m % 2 == 0:
            return scalar_product(result,result,n)
        return scalar_product(result,scalar_product(result,a,n),n)

    N, B = tuple(map(int,sys.stdin.readline().split(' ')))
    metrix = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(N)]

    s_metrix = square(metrix,N,B)

    for i in range(N):
        for j in range(N):
            print(s_metrix[i][j] % 1000, end=' ')
        print()

except ValueError or IndexError:
    print('Input Error')
'''
# 피보나치 수 6
'''https://www.acmicpc.net/problem/11444'''
'''
# [F_n, F_n-1] = a^(n-1) * [1,0]
# a = [[1,1],[0,1]]

import sys
try:
    n = int(sys.stdin.readline())
    if n == 1:
        print(1)
        sys.exit()
    metrix = [[1,1],[1,0]]
    p = 1000000007

    def scalar_product(a,b,__=2):
        rlt = []
        for i in range(2):
            list_ = []
            for j in range(__):
                sum_ = 0
                for k in range(2):
                    sum_ += a[i][k]*b[k][j]
                    sum_ = sum_ % p
                list_.append(sum_)
            rlt.append(list_)
        return rlt

    def square(a,m):
        if m == 1:
            return a
        result = square(a,m//2)
        if m % 2 == 0:
            return scalar_product(result,result)
        return scalar_product(result,scalar_product(result,a))

    value_s = square(metrix,n-1)
    result = scalar_product(value_s,[[1],[0]],1)
    print(result[0][0]%p)

except ValueError:
    print('Input Error')
'''
'''
# segment tree
arr = [1,2,3,4,5,6,7,8,9,10]
tree = [0] * (len(arr)*4)

# < segment 트리를 배열의 각 구간 합으로 채워주기 >
# start : 배열의 시작 인덱스, end : 배열의 마지막 인덱스
# index : 세그먼트 트리의 인덱스 (무조건 1부터 시작)

def init(start,end,index):
    # 가장 끝에 도달했으면 arr 삽입
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    # 좌측 노드와 우측 노드를 채워주면서 부모노드의 값도 채워준다.
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index * 2 + 1)
    return tree[index]

print(f'트리 초기화 전 : {tree}')
init(0,9,1)
print(f'트리 초기화 후 : {tree}')

# sum of interval
# start : 시작 인덱스, end : 마지막 인덱스
# left, right : 구간의 합을 구하고자 하는 범위

def interval_sum(start,end,index,left,right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) //2
    return interval_sum(start,mid,index*2,left,right) + interval_sum(mid+1,end,index*2 + 1,left,right)

print(f'6~9 구간의 합 : {interval_sum(0,9,1,6,9)}')

# 특정 원소의 값을 수정하는 함수
# start : 시작 인덱스, end : 마지막 인덱스
# what : 구간의 합을 수정하고자 하는 노드
# value : 수정할 값

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)


print(f'update 전 : {tree}')
update(0,9,1,6,5)
print(f'update 후(7 -> 10) : {tree}')

'''

# 히스토그램에서 가장 큰 직사각형
'''https://www.acmicpc.net/problem/6549'''
'''
# sol 1 : divide and conquer and segment tree
# 먼저 최소값을 찾기 위한 segment tree 구현(각 값은 인덱스)

import sys
import math
sys.setrecursionlimit(10**6)
try:
    def init(start, end, index):
        if start == end:
            s_tree[index] = start
            return start
        mid = (start + end) // 2
        left_ = init(start, mid, index * 2)
        right_ = init(mid + 1, end, index * 2 + 1)
        idx = (left_ if numbers[left_] <= numbers[right_] else right_)
        s_tree[index] = idx
        return idx


    def get_min(start, end, index, left, right):
        if right < start or end < left:
            return -1
        if left <= start and end <= right:
            return s_tree[index]
        mid = (start + end) // 2
        left_ = get_min(start, mid, index * 2, left, right)
        right_ = get_min(mid + 1, end, index * 2 + 1, left, right)

        if left_ == -1:
            return right_

        if right_ == -1:
            return left_

        return left_ if numbers[left_] <= numbers[right_] else right_

    def get_max_area(left, right):
        width = right - left + 1
        if width == 1:
            return numbers[right]

        high_idx = get_min(0, N - 1, 1, left, right)
        area = width * numbers[high_idx]
        # print(area)

        if left <= high_idx - 1:
            area = max(area, get_max_area(left, high_idx - 1))
        if right >= high_idx + 1:
            area = max(area, get_max_area(high_idx + 1, right))
        # print(f'left = {left}, right = {right}, area = {area}')
        return area


    while True:
        list_ = list(map(int, sys.stdin.readline().split(' ')))
        N, numbers = list_[0], list_[1:]
        if N == 0:
            break
        s_tree = [0] * (pow(2,math.ceil(math.log(N,2))+1)-1)
        max_area = 0


        init(0,N-1,1)
        print(get_max_area(0,N-1))

except ValueError or IndexError:
    print('Input Error')

'''
# sol 2 : stack

import sys
try:
    while True:
        list_ = list(map(int,sys.stdin.readline().split(' ')))
        n, numbers = list_[0], list_[1:]

        if n == 0:
            break

        stack_ = []
        i = 0
        max_area = 0
        while i < n:
            while stack_ and numbers[stack_[-1]] > numbers[i]:
                height = numbers[stack_.pop()]
                width = (i if not stack_ else i - stack_[-1] - 1)
                max_area = max(max_area, height*width)
            stack_.append(i)
            i+=1
        while stack_:
            height = numbers[stack_.pop()]
            width = (i if not stack_ else i - stack_[-1] - 1)
            max_area = max(max_area, height*width)
        print(max_area)
except ValueError or IndexError:
    print('Input Error')




