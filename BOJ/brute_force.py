'''
# 블랙잭

# numbers => list => sort

def quick_sort_v1(a):
    len_a = len(a)
    if len_a <= 1:
        return a

    pivot = a[len_a // 2]
    lower, high, equal = [],[],[]

    for num in a:
        if pivot > num:
            lower.append(num)
        elif pivot < num:
            high.append(num)
        else:
            equal.append(num)

    return quick_sort_v1(lower) + equal + quick_sort_v1(high)

# 입력 : N(숫자의 개수), M(원하는 값)
# 3 loop
# loop 1 : 0 ~ N-2 => i
# loop 2 : i+1 ~ N-1 => j // 정지조건 i + j > M => loop1 이동
# loop 3 : j+1 ~ N => k // 정지조건 i + j + k = M => 종료
#                       //     &   i + j + k > M
try:
    N, M = tuple(map(int, input().split(' ')))
    list_ = list(map(int, input().split(' ')))

    max_sum = 0
    b_p = 0

    for i in range(0,N-2):
        for j in range(i+1,N-1):
            for k in range(j+1, N):
                sum_ = list_[i] + list_[j] + list_[k]
                if sum_ == M:
                    max_sum = M
                    b_p = 1
                    break
                elif max_sum < sum_ < M:
                    max_sum = sum_
            if b_p == 1:
                break
        if b_p == 1:
            break
    print(max_sum)
except ValueError or IndexError:
    print('Input Error')

# 분해합
def get_dsum(n):
    list_ = list(map(int, str(n)))
    result = n
    for i in list_:
        result += i
    return result

try:
    N = int(input())
    if 1 <= N <= 1000000:
        number = (N-54 if N-54 > 1 else 1)
        while number < N:
            if get_dsum(number) == N:
                break
            number += 1
        if number == N:
            print(0)
        else:
            print(number)
    else:
        print("Input Error")
except ValueError:
    print("Input Error")

# 덩치
# 160, 60  150, 70  149, 65

try:
    N = int(input())
    if 2 <= N <= 50:
        list_ = []
        result = []
        for i in range(N):
            tup_ = tuple(map(int, input().split(' ')))
            list_.append(tup_)

        for i, tup_ in enumerate(list_):
            j = 0
            count = 0
            while j < N:
                if i != j and (list_[j][0] > tup_[0] and list_[j][1] > tup_[1]):
                    count += 1
                j += 1
            result.append(count+1)
        for num in result:
            print(num, end=' ')

    else:
        print("Input Error")
except ValueError:
    print("Input Error")
'''

# 체스판 칠하기

# count 함수
# a : 8 * 8 list
# output : count
'''def get_count(a):
    count_ = 0
    first = a[0][0]
    second = ('B' if first == 'W' else 'W')

    for i_ in range(8):
        for j_ in range(8):
            if j_ % 2 == 1 and a[i_][j_] != second:
                count_ += 1
            elif j_ % 2 == 0 and a[i_][j_] != first:
                count_ += 1
        first, second = second, first
    result = (count_ if 64 > count_ * 2 else 64 - count_)
    return result

# count를 구해주는 함수를 사용하려면 slicing이 되어야한다.
# 함수를 사용하지 않고 반복문을 추가적으로 돌렸다
# 체스판 다시 색칠하기
try:
    N, M = tuple(map(int, input().split(' ')))
    if 8 <= N <= 50 and 8 <= M <= 50:
        list_ = []
        for i in range(N):
            str_ = input()
            list_.append(list(str_))
        min_count = 64
        for i in range(0,N-7):
            for j in range(0,M-7):

                count_ = 0
                first = list_[i][j]
                second = ('B' if first == 'W' else 'W')

                for i_ in range(i,8+i):
                    for j_ in range(j,8+j):
                        if j_ % 2 == 1 and list_[i_][j_] != second:
                            count_ += 1
                        elif j_ % 2 == 0 and list_[i_][j_] != first:
                            count_ += 1
                    first, second = second, first
                result = (count_ if 64 > count_ * 2 else 64 - count_)

                if min_count > result:
                    min_count = result
                if min_count == 0:
                    break
            if min_count == 0:
                break
        print(min_count)
    else:
        print("Input Error")
except ValueError:
    print("Input Error")

'''

# 영화감독 숌
# 666 부터 count로 개수 세기
# 
def is_eschatology_num(m):
    number = m - 666
    while number % 1000 != 0:
        m = m // 10
        number = m - 666

        if number < 0:
            return False
    return True

# print(is_eschatology_num(66610000))
try:
    N = int(input())
    count = 1
    i = 666
    if 1 <= N <= 10000:
        while count <= N:
            if is_eschatology_num(i):
                count += 1
            i += 1
        i -= 1
        print(i)
    else:
        print("Input Error")

except ValueError:
    print("Input Error")
