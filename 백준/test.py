'''N = 5

list_ = [5, 17, 23, 14, 83]

r = 0

min_ = 5 # N

result = []

# 공약수 구하기
# 공약수 = 최대 공약수의 약수


    for num in list_:  # N
        if num % k != r:
            break
        count += 1
    if count == N:
        result.append(k)
    r += 1

print(result)

''''''
sudoku = [0, 3, 5, 4, 6, 9, 2, 7, 8,
            7, 8, 2, 1, 0, 5, 6, 0, 9,
            0, 6, 0, 2, 7, 8, 1, 3, 5,
            3, 2, 1, 0, 4, 6, 8, 9, 7,
            8, 0, 4, 9, 1, 3, 5, 0, 6,
            5, 9, 6, 8, 2, 0, 4, 1, 3,
            9, 1, 7, 6, 5, 2, 0, 8, 0,
            6, 0, 3, 7, 0, 1, 9, 5, 2,
            2, 5, 8, 3, 9, 4, 7, 6, 0]

result = []
for i, num in enumerate(sudoku):
    if num == 0:
        print(f'index = {i}')
        result.append(i)
print(result)
'''

'''
def scalar_product(a, b, __=2):
    rlt = []
    for i in range(2):
        list_ = []
        for j in range(__):
            sum_ = 0
            for k in range(2):
                sum_ += a[i][k] * b[k][j]
                sum_ = sum_ % 100000
            list_.append(sum_)
        rlt.append(list_)
    return rlt


print(scalar_product([[1,1],[1,0]],[[1],[0]],1))
'''
'''
import sys
N, M, K = tuple(map(int, sys.stdin.readline().split(' ')))
numbers = [int(sys.stdin.readline()) for _ in range(N)]
s_tree = [0] * (len(numbers) * 4)


def init(start, end, index):
    # 끝에 도달 했을 경우
    if start == end:
        s_tree[index] = numbers[start]
        return s_tree[index]
    # 그 외 경우 한 단계 더 밑으로 진행
    mid = (start + end) // 2
    s_tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return s_tree[index]


def sum_interval(start, end, index, left, right):
    # 범위안에 없을 때
    if start > right or end < left:
        return 0
    # 범위안에 완전 포함 될 때
    if left <= start and end <= right:
        return s_tree[index]
    # 범위에 부분 포함 될 때 부분을 나눠 진행한다.
    mid = (start + end) // 2
    return sum_interval(start, mid, index * 2, left, right) + sum_interval(mid + 1, end, index * 2 + 1, left, right)


def update(start, end, index, idx, value):
    # 범위 안에 없을때
    if start > idx or end < idx:
        return
    # 범위에 있을때
    s_tree[index] += value
    if start == end:  # 끝 노드면 마침
        return
    # 끝 노드가 아닐 경우 밑으로 계속 진행
    mid = (start + end) // 2
    update(start, mid, index * 2, idx, value)
    update(mid + 1, end, index * 2 + 1, idx, value)


print(f'초기화 전 : {s_tree}')
init(0, 4, 1)
print(f'초기화 후 : {s_tree}')
print(f'2~5까지의 구간 합 : {sum_interval(0, 4, 1, 1, 4)}')
print(f'3번째 값 6으로 변경')
update(0, 4, 1, 2, 6 - numbers[2])
print(f'2~5까지의 구간 합(변경후) : {sum_interval(0, 4, 1, 1, 4)}')
'''
'''
a = 6
b = 3
print(f'a = {a}, b = {b}')
print(f'a/b = {a/b}\na//b = {a//b}')
'''
'''
list_ = [0,1,3,5,7,9,11]


def binary_search(k):
    low, high = 1, len(list_) - 1
    while low <= high:
        mid = (low + high) // 2
        if list_[mid] == k:
            return mid

        if list_[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return low


print(binary_search(5))
'''

# Queue
class Queue:
    def __init__(self):
        self.list_ = []
        self.tail = -1
        self.head = -1

    def get_queue(self):
        return self.list_[self.tail + 1 : self.head]

    def push(self, x):
        self.list_.append(x)
        self.head += 1

    def empty(self):
        if self.head == self.tail:
            return 1
        return 0

    def size(self):
        return self.head - self.tail

    def pop(self):
        if self.empty():
            return -1
        self.tail += 1
        return self.list_[self.tail]

    def front(self):
        if self.empty():
            return -1
        return self.list_[self.tail+1]

    def back(self):
        if self.empty():
            return -1
        return self.list_[self.head]


# 큐
'''https://www.acmicpc.net/problem/10845'''
'''import sys
try:
    N = int(sys.stdin.readline())
    queue = Queue()
    for _ in range(N):
        tup_ = tuple(sys.stdin.readline().split(' '))
        if len(tup_) == 2:
            queue.push(int(tup_[1]))
        else:
            command = tup_[0].rstrip()
            if command == 'pop':
                print(queue.pop())
            elif command == 'empty':
                print(queue.empty())
            elif command == 'size':
                print(queue.size())
            elif command == 'back':
                print(queue.back())
            elif command == 'front':
                print(queue.front())
except ValueError or IndexError:
    print('Input Error')


a = {0 : []}
a[0].sort(reverse=True)
print(a)
'''

a = [1,2,3,4]
for i in range(4):
    a[i] *= 2
print(a)

# 억억단을 외우자
# 1 ~ e 범위에서 약수의 개수가 가장 많은 것을 return한다.
# 만약 같다면 작은 수를 return 한다.


def solution(e, starts):
    def get_count_div(x):
        if x == 1:
            return 1
        i = 1
        count = 0
        while i * i < x:
            if x % i == 0:
                count += 2
            i += 1
        if i * i == x:
            return count + 1
        return count

    starts.sort()

    len_s = len(starts)
    starts_div = [1] * len_s

    for x in range(starts[0], e + 1):
        count_ = get_count_div(x)
        # print(f'\nx = {x} // count_ = {count_}')
        for idx in range(len_s):
            if starts[idx] > x:
                break
            elif starts_div[idx] < count_:
                starts_div[idx] = count_
                starts[idx] = x
            # print((f'\nstarts = {starts}\nstartd = {starts_div}'))

    return starts

print(92681)