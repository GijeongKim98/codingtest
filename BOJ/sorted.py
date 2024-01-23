# 수 정렬하기
# 선택정렬
def check_sort(a):
    for i in range(1,len(a)):
        if a[i-1] > a[i]:
            return False
    return True

def selection_sort(a):
    len_a = len(a)
    for i in range(len_a):
        max_index = i
        for j in range(i,len_a):
            if a[max_index] > a[j]:
                max_index = j
        a[max_index], a[i] = a[i], a[max_index]
        # print(a)
    return a

# 버블정렬

def bouble_sort(a):
    len_a = len(a)
    for i in range(len_a-1):
        for j in range(len_a - 1 - i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            # print(a)
        # print()
    return a

# 삽입정렬
# index기준 1부터 n 까지 i
# i-1부터 0까지 j  j와 i를 비교해서 i가 크면 이동
def insertion_sort(a):
    len_a = len(a)
    for i in range(1,len_a):
        select = a[i]
        j = i - 1
        while select < a[j] and j >= 0:
            a[j+1] = a[j]
            print(f'a = {a}, j = {j}')
            j -= 1
        a[j+1] = select
        print(a)
    return a

#print(insertion_sort([5,4,3,2,1]))

# 힙 정렬
# 힙 구조 : 높이가 가장 작은 이진 트리
# 부모 노드 : m // 2
# 자식 노드 : m*2 , m*2 + 1

class DownHeap:
    def __init__(self):
        self.list_ = [None]

    def get_list(self):
        # print('1111111111111')
        return self.list_

    def is_empty(self):
        if self.list_ == [None]:
            return True
        return False

    def insert(self, m):
        if self.is_empty():
            self.list_.append(m)
        else:
            self.list_.append(m)
            c = len(self.list_) - 1
            p = c // 2
            while p > 0 and self.list_[c] < self.list_[p]:
                self.list_[p], self.list_[c] = self.list_[c], self.list_[p]
                c, p = p, p//2


    def pop(self):
        if self.is_empty():
            return -1
        result = self.list_[1]
        self.list_[1] = self.list_[-1]
        len_h = len(self.list_) - 1

        self.list_ = self.list_[:len_h]

        p = 1
        if len_h > p*2 + 1:
            c = (p*2 if self.list_[p*2] < self.list_[p*2 + 1] else p*2 + 1)
        elif len_h == p * 2 + 1:
            c = p * 2
        else:
            return result

        while self.list_[c] < self.list_[p] and c < len_h:
            self.list_[p], self.list_[c] = self.list_[c], self.list_[p]
            p = c
            if len_h > p * 2 + 1:
                c = (p * 2 if self.list_[p * 2] < self.list_[p * 2 + 1] else p * 2 + 1)
            elif len_h == p * 2 + 1:
                c = p * 2
            else:
                break
        # print(f'result = {result}')
        return result

def heap_sort(a):
    len_a = len(a)
    min_heap = DownHeap()
    for i in a:
        min_heap.insert(i)
    for i in range(len_a):
        k = min_heap.pop()
        a[i] = k

    return a

# print(heap_sort([5,3,4,1,2]))

# merge_sort

def merge_sort(a, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(a,l,m)
        merge_sort(a,m+1,r)
        merge(a,l,m,r)

def merge(a,l,m,r):
    i, j = l, m+1
    temp = []
    while i <= m and j <= r:
        if a[i] > a[j]:
            temp.append(a[j])
            j += 1
        else:
            temp.append(a[i])
            i += 1

    if i <= m:
        temp += a[i:]

    elif j <= r:
        temp += a[j:]

    k = 0
    for i in range(l,r+1):
        a[i] = temp[k]
        k += 1

# A = [5,4,3,2,1]
# merge_sort(A,0,4)
# print(A)

def merge_sort2(a):
    len_a = len(a)
    if len_a <= 1:
        return a
    half = len_a // 2
    left_list = merge_sort2(a[:half])
    right_list = merge_sort2(a[half:])

    return merge2(left_list, right_list)

def merge2(a,b):
    result = []
    len_a, len_b = len(a), len(b)
    i, j = 0, 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    while i < len_a:
        result.append(a[i])
        i += 1

    while j < len_b:
        result.append(b[j])
        j += 1

    return result



# quick_sort 실행속도 3.6

def partition(a, l, r):
    pivot = a[l]
    low = l+1
    high = r

    while l < r:
        while low <= r and a[low] < pivot:
            low += 1
        while high >= l and a[high] > pivot:
            high -= 1
        if low >= high:
            break
        a[low], a[high] = a[high], a[low]
        # print(f'a = {a}')

    a[high] ,a[l] = a[l], a[high]

    return high

def quick_sort(a,l,r):
    if l < r:
        q = partition(a, l, r)
        quick_sort(a,l,q-1)
        quick_sort(a,q+1,r)

# quick_sort Version2 실행속도 2.9
def quick_sort2(a):
    len_a = len(a)
    if len_a <= 1:
        return a

    pivot = a[len_a // 2]
    lesser_list, equal_list, greater_list = [],[],[]

    for num in a:
        if num < pivot:
            lesser_list.append(num)
        elif num > pivot:
            greater_list.append(num)
        else:
            equal_list.append(num)
    return quick_sort2(lesser_list) + equal_list + quick_sort2(greater_list)


def quick_sort3(a,l,r):
    def partition2(l, r):
        pivot = a[r]
        low = l
        for high in range(l,r):
            if a[high] < pivot:
                a[low], a[high] = a[high], a[low]
                low += 1
        a[low], a[r] = a[r], a[low]
        return low
    if l < r:
        pivot = partition2(l,r)
        quick_sort3(a,l,pivot-1)
        quick_sort3(a,pivot+1,r)



# 3 1 2
'''#
import random
import time

N = 1000000

list_ = list(range(1,N+1))

random.shuffle(list_)

start = time.time()
# quick_sort3(list_,0,N-1)
list_ = merge_sort2(list_)
end = time.time()
if check_sort(list_):
    print(end - start)
else:
    print('실패')
'''












#a = [5,4,2,8,1,9,3,7,6]
#quick_sort(a,0,8)
#print(a)
# 5 3 8 4 9 1 6 2 7 // p = 5
# 5 // 3 8 4 9 1 6 2 7
# 5 // 3 8 4 9 1 6 2 7
# 5 // 3 2 4 9 1 6 8 7
# 5 // 3 2 4 1 9 6 8 7
# 1 3 2 4 // 5 // 9 6 8 7
'''
# 수 정렬하기 -1

try:
    N = int(input())
    if 1 <= N <= 1000:
        list_ = []
        for i in range(N):
            list_.append(int(input()))

        quick_sort(list_)

        for num in list_:
            print(num)
    else:
        print('Input Error')
except ValueError:
    print('Input Error')

# 수 정렬 하기 2
import sys

try:
    N = int(input())
    if 1 <= N <= 1000000:
        list_ = []
        for i in range(N):
            list_.append(int(sys.stdin.readline()))

        list_ = merge_sort2(list_)
        # print(list_)
        for num in list_:
            print(num)
    else:
        print('Input Error')
except ValueError:
    print('Input Error')
'''

# 수 정렬하기 - 3

def counting_sort(a, max_):
    len_a = len(a) + 1
    a = [-1] + a

    sum_list = [0] * (max_ + 1)
    result = [-1] + [0] * (len_a - 1)

    for num in a[1:]:
        sum_list[num] += 1

    sum_ = sum_list[0]
    for i in range(1,max_+1):
        if sum_list[i] == 0:
            sum_list[i] = -1
        else:
            sum_list[i] += sum_
            sum_ = sum_list[i]
    # print(sum_list)  확인용

    for i in range(len_a-1,0,-1):
        num = a[i]
        if sum_list[num] != -1:
            result[sum_list[num]] = num
            sum_list[num] -= 1

    return result[1:]
'''
import sys

try:
    N = int(input())
    max_ = 10000
    list_ = []
    if 1<= N <= 10000000:
        for i in range(N):
            list_.append(int(sys.stdin.readline()))
        rst = counting_sort(list_, max_)

        for i in rst:
            print(i)

    else:
        print('Input Error')

except ValueError:
    print('Input Error')

import sys

try:
    N = int(input())
    max_ = 10000
    list_ = []
    sum_list = [0] * (max_+1)
    if 1<= N <= 10000000:
        for i in range(N):
            sum_list[int(sys.stdin.readline())] += 1

        for number, count in enumerate(sum_list):
            if count > 0:
                for i in range(count):
                    print(number)

    else:
        print('Input Error')

except ValueError:
    print('Input Error')



# a = [5,5,3,4,5,1,0,4,1,3,0,2,4,2,3,0]

# print(counting_sort(a,5))


# 커트 라인

try:
    str_ = input()
    N, k = tuple(map(int, str_.split(' ')))
    scores = input()
    scores = list(map(int, scores.split(' ')))

    if len(scores) == N:
        scores = quick_sort2(scores)
        print(scores[N-k])

    else:
        print('Input Error')
except ValueError:
    print('Input Error')



# 통계학

def trans_integer(m):
    if m[0] == '-':
        return (-1) * int(m[1:])
    else:
        return int(m)

import sys

try:
    N = int(input())
    list_ = []
    if (1 <= N <= 500000) and N % 2 == 1:
        for i in range(N):
            list_.append(trans_integer(sys.stdin.readline()))

        # print(list_)
        numbers = quick_sort2(list_)
        # print(numbers)

        max_ = numbers[-1]
        min_ = numbers[0]
        sum_ = 0
        count = 1
        max_count = 0
        mode = N-1, 1
        pre_mode = N-1, 1

        for i in range(N-1,-1,-1):
            sum_ += numbers[i]

            if 0 < i < N and numbers[i] == numbers[i-1]:
                count += 1
            else:
                if count >= max_count:
                    max_count = count
                    pre_mode = mode
                    mode = i, count
                count = 1

        # print(f'mode = {mode}')
        # print(f'pre_mode = {pre_mode}')

        # print('***********************************')
        print(round(sum_ / N))
        print(numbers[N//2])

        print((numbers[mode[0]] if mode[1] != pre_mode[1] else numbers[pre_mode[0]]))
        print(max_ - min_)

    else:
        print('Input Error')

except ValueError:
    print('Input Error')


# 소트 인사이드

try:
    str_ = input()
    numbers = []
    for char in str_:
        numbers.append(int(char))

    #print(numbers)

    numbers = quick_sort2(numbers)
    numbers.reverse()
    for num in numbers:
        print(num, end='')

except ValueError:
    print('Input Error')
'''

# 좌표 정렬하기 - 1
'''
# quick sort 변형하기
def quick_sort_v2(a, axis = 0):  # axis = 0, x // axis = 1, y
    len_a = len(a)
    if len_a <= 1:
        return a

    pivot = a[len_a // 2][axis]
    lesser_list, equal_list, greater_list = [],[],[]

    for i in range(len_a):
        if a[i][axis] < pivot:
            lesser_list.append(a[i])
        elif a[i][axis] > pivot:
            greater_list.append(a[i])
        else:
            equal_list.append(a[i])
    return quick_sort_v2(lesser_list, axis) + quick_sort_v2(equal_list, 1) + quick_sort_v2(greater_list, axis)

def trans_integer(m):
    if m[0] == '-':
        return (-1) * int(m[1:])
    else:
        return int(m)

try:
    N = int(input())
    list_ = []
    for i in range(N):
        list_.append(tuple(map(trans_integer, input().split(' '))))
    result = quick_sort_v2(list_)
    for tup in result:
        print(f'{tup[0]} {tup[1]}')
except ValueError:
    print('Input Error')

# 좌표 정렬하기 - 2
def trans_integer(m):
    if m[0] == '-':
        return (-1) * int(m[1:])
    else:
        return int(m)

try:
    N = int(input())
    list_ = []
    for i in range(N):
        list_.append(tuple(map(trans_integer, input().split(' '))))
    result = quick_sort_v2(list_, 1)
    for tup in result:
        print(f'{tup[0]} {tup[1]}')
except ValueError:
    print('Input Error')

# 단어 정렬

# 단어의 길이가 짧은 순서 부터 사전 순서 대로

# 같은 길이의 단어 정렬
# 입력 : 같은 길이의 단어들의 list
# 출력 : 정렬된 list

def same_len_word_sort(a, n): # a는 list n의 단어의 n번째 알파벳
    len_a = len(a)
    if len_a <= 1:
        return a

    len_word = len(a[0])
    if n == len_word:
        return [a[0]]

    pivot = ord(a[0][n])
    # print(f'pivot word = {a[0]}, pivot = {a[0][n]}, n = {n}')
    lower_list, equal_list, high_list = [],[],[]

    for word in a:
        if pivot > ord(word[n]):
            lower_list.append(word)
        elif pivot < ord(word[n]):
            high_list.append(word)
        else:
            equal_list.append(word)

    # print(lower_list)
    # print(equal_list)
    # print(high_list)

    return same_len_word_sort(lower_list,n) + same_len_word_sort(equal_list,n+1) + same_len_word_sort(high_list,n)

# list_ = ['no','it','ie','it','ia','ib']

# print(same_len_word_sort(list_,0))

# 단어 각각의 길이로 단어 정렬
# 입력 : a = 단어 리스트
# 출력 : 정렬된 리스트

def quick_sort_v3(a):
    len_a = len(a)
    if len_a <= 1:
        return a

    pivot = len(a[0])
    lower_list, equal_list, high_list = [], [], []

    for word in a:
        len_word = len(word)
        if len_word < pivot:
            lower_list.append(word)
        elif len_word > pivot:
            high_list.append(word)
        else:
            equal_list.append(word)

    return quick_sort_v3(lower_list) + same_len_word_sort(equal_list,0) + quick_sort_v3(high_list)

try:
    N = int(input())
    if 1 <= N <= 20000:
        list_ = []
        for i in range(N):
            word = input()
            if 1 <= len(word) <= 50 and word.islower():
                list_.append(word)
            else:
                print('Input Error')

        result = quick_sort_v3(list_)

        for word in result:
            print(word)

except ValueError:
    print('Input Error')

# 나이순 정렬

# 퀵 정렬을 변형
# 입력 : tuple = (나이, 이름) 들의 list
# 출력 : 정렬된 list

def quick_sort_v4(a):
    len_a = len(a)
    if len_a <= 1:
        return a

    pivot = a[0][0]
    lower_list, equal_list, high_list = [], [], []

    for tup in a:
        if pivot > tup[0]:
            lower_list.append(tup)
        elif pivot < tup[0]:
            high_list.append(tup)
        else:
            equal_list.append(tup)

    return quick_sort_v4(lower_list) + equal_list + quick_sort_v4(high_list)

try:
    N = int(input())
    if 1 <= N <= 100000:
        list_ = []
        for i in range(N): 
            l = input().split(' ')
            tup_ = int(l[0]), l[1]

            list_.append(tup_)

        result = quick_sort_v4(list_)

        for tup in result:
            print(f'{tup[0]} {tup[1]}')

    else:
        print('Input Error')
except ValueError:
    print('Input Error')

'''


# 좌표 압축
# 처음 입력 받은 숫자 리스트 저장 + copy
# copy list 정렬
# copy list => dictionary
# 기존의 리스트 => loop => 출력
'''
# 정렬 -> quick sort -> 같은수 삭제
def quick_sort_v1(a):
    len_a = len(a)
    if len_a <= 1:
        return a

    pivot = a[len_a//2]
    lower_list, equal_list, high_list = [], [], []

    for num in a:
        if num < pivot:
            lower_list.append(num)
        elif num > pivot:
            high_list.append(num)
        else:
            if not equal_list:
                equal_list.append(num)

    return quick_sort_v1(lower_list) + equal_list + quick_sort_v1(high_list)

try:
    N = int(input())
    if 1 <= N <= 1000000:
        str_ = input()
        numbers = list(map(int, str_.split(' ')))
        if len(numbers) == N:
            copy_list = numbers[:]

            copy_list = quick_sort_v1(copy_list)

            dictionary = dict()

            for i, number in enumerate(copy_list):
                dictionary[number] = i

            for num in numbers:
                print(dictionary[num], end=' ')
        else:
            print('Input Error')
    else:
        print('Input Error')

except ValueError:
    print('Input Error')
'''

# 대표값2
'''https://www.acmicpc.net/problem/2587'''

import sys

try:
    numbers = [int(sys.stdin.readline()) for _ in range(5)]
    numbers.sort()
    print(sum(numbers) // 5)
    print(numbers[2])

except ValueError or IndexError:
    print('Input Error')

