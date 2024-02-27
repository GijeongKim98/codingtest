# 주사위 고르기
# 다시 풀기 : 해결 못한 알고리즘 이분 탐색

# 풀이 방법
# 1. 절반의 주사위를 선택
#   # - 방법1 : 백트래킹을 이용해 구한다.
    # - 방법2 : combination
    
# 2. 주사위 별 합계 구하기
    # 나올 수 있는 숫자를 확인 6 ** 5 = 7776개의 숫자 계산 필요
    # 주사위 1개 => 6개
    # 주사위 2개 => 36개
    # for 문으로 주사위 한개씩 더한다.

# 3. 승률 계산 = 승리 횟수 계산
    # 합계1, 합계2 => 둘 다 정렬 후 투 포인터 알고리즘을 사용한다. => 지고 이긴 것을 알 수 있다.
    # 합계1만 정렬 => 합계2의 원소들을 가지고 binary search를 사용해 이길 수 있는 것들을 탐색

# 4. 최신화
    # 승률이 높아지는 조합을 최신화
    
# 틀린 방법은 아닌데 시간초과 발생 바이너리 서치로 해보자

def solution1(dice):
    def sumation(sums, d2):
        result = []
        for num1 in d2:
            for num2 in sums:
                result.append(num1 + num2)
        return result
    
    
    # get_sum_of_dice 함수 구현
    def get_sum_of_dice(dice_list):
        result = [0]
        for idx in dice_list:
            result = sumation(result, dice[idx])
        return result
            
    
    # get_count_of_victory 함수 구현
    def get_count_of_victory(choose_list):
        # 2번 과정 각각의 합을 구해야함
        dice_a, dice_b = [0], []
        
        for idx in range(1,n):
            if is_a_dice[idx]:
                dice_a.append(idx)
            else:
                dice_b.append(idx)
                
        sums_a, sums_b = get_sum_of_dice(dice_a), get_sum_of_dice(dice_b)
        
        length_of_sums = len(sums_a)
        
        # 정렬
        sums_a.sort()
        sums_b.sort()
        
        # 승리 횟수 조사
        a_idx, b_idx = 0, 0
        a_count, b_count = 0, 0
        
        while a_idx < length_of_sums and b_idx < length_of_sums:
            if sums_a[a_idx] < sums_b[b_idx]:
                a_count += b_idx
                a_idx += 1
            elif sums_a[a_idx] > sums_b[b_idx]:
                b_count += a_idx
                b_idx += 1
            
            else:
                a_c, b_c = 0, 0
                while a_idx < length_of_sums-1 and sums_a[a_idx] == sums_a[a_idx+1]:
                    a_c += 1
                    a_idx += 1
                    a_count += b_idx - b_c
                    
                while b_idx < length_of_sums-1 and sums_b[b_idx] == sums_b[b_idx+1]:
                    b_c += 1
                    b_idx += 1
                    b_count += a_idx - a_c
                    
                a_count += b_idx - b_c
                b_count += a_idx - a_c
                
                a_idx += 1
                b_idx += 1                
        
        while a_idx < length_of_sums:
            a_count += b_idx
            a_idx += 1
            
        while b_idx < length_of_sums:
            b_count += a_idx
            b_idx += 1
        
        num = 0        
        if a_count >= b_count:
            count = a_count
            for idx in dice_a:
                num += (1 << idx)
        
        else:
            count = b_count
            for idx in dice_b:
                num += (1 << idx)
        
        return num, count 
    
    
    # dfs 함수 구현
    def dfs(step):
        
        if step == n//2: # 절반을 선택 했을때
            #2-3번 과정: 주사위합계 및 승리 횟수 조사 
            number, count = get_count_of_victory(is_a_dice)
            
            # 4번 과정
            if count > result[1]:
                result[0], result[1] = number, count
             
        for idx in range(1,n):
            if not is_a_dice[idx]:
                is_a_dice[idx] = 1
                dfs(step+1)
                is_a_dice[idx] = 0
        
    
    # 1번 과정 : 주사위 나누기 => dfs를 활용
    
    n = len(dice) # 주사위의 개수
    is_a_dice = [0 for _ in range(n)] # a가 선택했는지 조사
    is_a_dice[0] = 1
    result = [0,0] # 최대의 이긴 횟수일 때의 조합을 이진수로 표현, 최대의 이긴 횟수
    dfs(1)
    
    
    answer = []
    
    for idx in range(n):
        if result[0] & (1 << idx):
            answer.append(idx+1)

    return answer


def solution(dice):
    def sumation(sums, d2):
        result = []
        for num1 in d2:
            for num2 in sums:
                result.append(num1 + num2)
        return result
    
    
    # get_sum_of_dice 함수 구현
    def get_sum_of_dice(dice_list):
        result = [0]
        for idx in dice_list:
            result = sumation(result, dice[idx])
        return result
            
    
    # get_count_of_victory 함수 구현
    def get_count_of_victory():
        def binary_search(s):
            low, high = 0, len(sums_b)
            k = 0
            while low < high:
                mid = (low + high) // 2
                
                if sums_b[mid] < s:
                    low = mid+1
                elif sums_b[mid] > s:
                    high = mid
                else:
                    return mid
            
            return low
                
       # 2번 과정 각각의 합을 구해야함
        dice_a, dice_b = [0], []
        
        for idx in range(1, n):
            if is_a_dice[idx]:
                dice_a.append(idx)
            else:
                dice_b.append(idx)
                
        sums_a, sums_b = get_sum_of_dice(dice_a), get_sum_of_dice(dice_b)
        
        count_ = len(sums_a) * len(sums_b)
        
        # 정렬
        # sums_a.sort()
        
        dict_ = dict()
        
        for sum_b in sums_b:
            if sum_b in dict_:
                dict_[sum_b] += 1
            else:
                dict_[sum_b] = 1
                
        sums_b = list(dict_.keys())
        sums_b.sort()
        
        sum_ = 0
        for sum_b in sums_b:
            sum_ += dict_[sum_b]
            dict_[sum_b] = sum_
        
        a_count = 0
        d_count = 0
        # binary search 사용
        for sum_a in sums_a:
            b_idx = binary_search(sum_a)
            if b_idx == len(sums_b):
                a_count += dict_[sums_b[-1]]
            
            elif b_idx == 0:
                d_count += (dict_[sums_b[b_idx]] if sums_b[b_idx] == sum_a else 0)
            
            else:
                a_count += dict_[sums_b[b_idx-1]]
                d_count += (dict_[sums_b[b_idx]] - dict_[sums_b[b_idx-1]] if sums_b[b_idx] == sum_a else 0)
            
        b_count = count_ - a_count - d_count 
        
        num = 0        
        if a_count >= b_count:
            count = a_count
            for idx in dice_a:
                num += (1 << idx)
        
        else:
            count = b_count
            for idx in dice_b:
                num += (1 << idx)
        
        return num, count     
    
    # dfs 함수 구현
    def dfs(step):
        
        if step == n//2: # 절반을 선택 했을때
            #2-3번 과정: 주사위합계 및 승리 횟수 조사 
            number, count = get_count_of_victory()
            
            # 4번 과정
            if count > result[1]:
                result[0], result[1] = number, count
            
            return
             
        for idx in range(1,n):
            if not is_a_dice[idx]:
                is_a_dice[idx] = 1
                dfs(step+1)
                is_a_dice[idx] = 0
        
    
    # 1번 과정 : 주사위 나누기 => dfs를 활용
    
    n = len(dice) # 주사위의 개수
    is_a_dice = [0 for _ in range(n)] # a가 선택했는지 조사
    is_a_dice[0] = 1
    result = [0,0] # 최대의 이긴 횟수일 때의 조합을 이진수로 표현, 최대의 이긴 횟수
    dfs(1)
    
    
    answer = []
    
    for idx in range(n):
        if result[0] & (1 << idx):
            answer.append(idx+1)

    return answer


if __name__ == "__main__":
    # dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]
    # dice = [[1, 2, 3, 4, 5, 6], [2, 2, 4, 4, 6, 6]]
    dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
    ans = solution(dice)
    print(ans)