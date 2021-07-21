def solution(lottos, win_nums):
    answer = []
    ranking = [6, 6, 5, 4, 3, 2, 1]
    cnt = 0
    zero_cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
        if num == 0:
            zero_cnt += 1
            
    lowest = ranking[cnt]
    highest = ranking[cnt + zero_cnt]
        
    answer.append(highest)
    answer.append(lowest)
    
    return answer