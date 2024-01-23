'''# 팩토리얼

def factorial(a):
    if a == 0:
        return 1
    return a * factorial(a-1)

try:
    N = int(input())
    if 0 <= N <= 12:
        print(factorial(N))
    else:
        print('Input Error')

except ValueError:
    print('Input Error')
'''
'''# 피보나치 수열

try:
    n = int(input())
    p = [0,1] + [0] * (n-1)
    for i in range(2, n+1):
        p[i] = p[i-1] + p[i-2]
    print(p[n])

except ValueError:
    print('Input Error')
''''''
def pi(n): # 2^n
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return pi(n-1) + pi(n-2)

print(pi(20))
# 재귀의 귀재
def recursion(s, l, r):
    if l >= r:
        return 1, l+1
    elif s[l] != s[r]:
        return 0, l+1
    else:
        return recursion(s, l+1, r-1)

def is_palindrome(s):
    return recursion(s, 0, len(s) - 1)

try:
    T = int(input())
    if 1 <= T <= 1000:
        for test in range(T):
            str_ = input()
            if 1 <= len(str_) <= 1000:
                a, b = is_palindrome(str_)
                print(f'{a} {b}')
            else:
                print('Input Error')
    else:
        print('Input Error')
except ValueError or IndexError:
    print('Input Error')



# 알고리즘 수업 병합 정렬1
# 4 5 1 3 2
# *4 5 1 3 2
# 4 *5 1 3 2


def merge_sort(A, p, r):  # 0 4
    if p == 1 and r == len(A) - 1:
        A.append(0)
        # print(A)

    if p < r:
        q = (p + r) // 2 # 2
        merge_sort(A, p, q) # 0 2
        merge_sort(A, q+1, r) # 3 4
        merge(A, p, q, r)

def merge(A, p, q, r):
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    if i <= q:
        tmp += A[i:q+1]
    elif j <= r:
        tmp += A[j:r+1]
    i = p
    for t in tmp:
        A[i] = t
        i += 1
        A[-1] += 1
        if A[-1] == A[0]:
            print(t)
    if p == 1 and r == len(A) - 2 and A[0] > A[-1]:
        print(-1)

try:
    str_ = input()
    N, K = tuple(map(int, str_.split(' ')))

    if 5 <= N <= 500000 and 1 <= K <= 100000000:
        numbers = input()
        A = list(map(int, numbers.split(' ')))
        if len(A) == N:
            A.insert(0,K)
            merge_sort(A,1,len(A)-1)
        else:
            print('Input Error')
    else:
        print('Input Error')

except ValueError or IndexError:
    print('Input Error')

'''
# 별 찍기 - 10
'''for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(' ', end ='')
        else:
            print('*', end='')
    print()


# 별찍기 - 10

def is_space(j,k,l):
    t = 3 ** j
    if t // 3 <= k % t < 2 * t // 3 and t // 3 <= l % t < 2 * t // 3:
        return True
    else:
        return False
def get_star(n,k): # 3 0 0
    for k in range(n):
        for l in range(n):
            if n-1 == l:
                print('*')
            elif n >= 3 ** 8 and is_space(8,k,l):
                print(' ', end='')
            elif n >= 3 ** 7 and is_space(7,k,l):
                print(' ', end='')
            elif n >= 3 ** 6 and is_space(6,k,l):
                print(' ', end='')
            elif n >= 3 ** 5 and is_space(5,k,l):
                print(' ', end='')
            elif n >= 3 ** 4 and is_space(4,k,l):
                print(' ', end='')
            elif n >= 3 ** 3 and is_space(3,k,l):
                print(' ', end='')
            elif n >= 3 ** 2 and is_space(2,k,l):
                print(' ', end='')
            elif n >= 3 ** 1 and is_space(1,k,l):
                print(' ', end='')
            else:
                print('*', end='')

'''

# ***
def get_star(n):
    if n == 1:
        return ['*']
    star_list = get_star(n//3)
    result_list = []
    for stars in star_list:
        result_list.append(stars*3)
    for stars in star_list:
        result_list.append(stars + ' '*(n//3) + stars)
    for stars in star_list:
        result_list.append(stars * 3)

    return result_list
# print(get_star(9))
# print('\n'.join(get_star(9)))

try:
    N = int(input())
    N1 = N
    i = 0
    while N1 != 1:
        if N1 % 3 != 0:
            i = 1
            break
        N1 = N1 // 3

    if i == 0:
        print('\n'.join(get_star(N)))
    else:
        print('Input Error')
except ValueError:
    print('Input Error')

# 하노이 탑 이동 순서
# n이 홀, 짝에 따라 순서가 바뀜

def hanoi(n, start, end):
    if n == 1:
        print(f'{start} {end}')
        return
    hanoi(n-1, start, 6-start-end)
    print(f'{start} {end}')
    hanoi(n-1, 6-start-end, end)

try:
    N = int(input())
    print(2**N - 1)
    hanoi(N,1,3)
except ValueError:
    print('Input Error')



# 수 정렬하기



