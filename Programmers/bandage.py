# 붕대 감기

def solution(bandage, health, attacks):
    A, B, C = bandage # a : 시전시간, b: 초당 회복량, c: 추가 회복량
    now = 1
    now_h = health
    for time, att in attacks:
        delta = time - now
        now_h = min(now_h+delta*B+(delta//A)*C, health)
        
        now = time+1
        
        now_h -= att
        
        if now_h <= 0:
            return -1
              
    return now_h
    

if __name__ == "__main__":
    
    b,h,a = [5, 1, 5],30,[[2, 10], [9, 15], [10, 5], [11, 5]]
    # b,h,a = [3, 2, 7],20,[[1, 15], [5, 16], [8, 6]]
    b,h,a = [4, 2, 7],20,[[1, 15], [5, 16], [8, 6]]
    b,h,a = [1, 1, 1],5,[[1, 2], [3, 2]]
    ans = solution(b, h, a)
    print(ans)
    
    
    # 5, -1, -1, 3