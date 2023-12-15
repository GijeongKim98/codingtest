# 책 페이지
'''https://www.acmicpc.net/problem/1019'''

def init_counts(digit):
    counts_0, counts_1_9 = [0], [1]
    
    for idx in range(2,digit):
        counts_0.append(counts_0[-1] + counts_1_9[-1]*9)
        counts_1_9.append(idx * 10**(idx-1))
        
    return counts_0, counts_1_9 

if __name__ == "__main__":
    try:
        N = int(input())
        numbers = list(map(int, list(str(N))))
        
        
        digit = len(numbers)
        counts_0, counts_1_9 = init_counts(digit)
        power_10 = [int("1"+"0"*i) for i in range(1,digit)]
        
        # print(power_10)
        # print(counts_0)
        # print(counts_1_9)
        
        answer = [0 for _ in range(10)]
        
        for idx, number in enumerate(numbers[:-1], start=2):
            now = digit - idx
            # 0 일때의 처리
            if number == 0:
                answer[0] += N % power_10[now] + 1
                continue
            if idx == 2:
                count_0 = counts_0[now] + counts_1_9[now] * (number-1)
            
            else:
                count_0 = counts_1_9[now] * number + power_10[now]
            
            count_less_number = counts_1_9[now] * number + power_10[now]
            count_number = counts_1_9[now] * number + N % power_10[now] + 1
            count_bigger_number = counts_1_9[now] * number

            for k in range(10):
                if k == 0:
                    answer[k] += count_0
                
                elif k < number:
                    answer[k] += count_less_number
                
                elif k == number:
                    answer[k] += count_number
                
                else:
                    answer[k] += count_bigger_number
        
        
        s = 0 if digit > 1 else 1
        
        for k in range(s,numbers[-1]+1):
            answer[k] += 1
        
        print(*answer)
        
    except ValueError or IndexError as e:
        print(e)
    