def solution(lines):
    log_time = []
    
    # 시간을 초단위로 변환
    for line in lines:
        log = line.split()
        h,m,s = log[1].split(':')
        end = int(h) * 3600 + int(m) * 60 + float(s)        
        end = round(end, 3)
        start = end - float(log[2][:-1]) + 0.001        
        start = round(start, 3)
        log_time.append([start,end])
    
    print(log_time)
    answer = 1
    for t in log_time:
        answer = max(answer, max_cnt(t[0], log_time), max_cnt(t[1], log_time))
    print(answer)
    return answer
    
def max_cnt(t, log_time):
    cnt = 0
    start = t
    end = start + 1 - 0.001
    end = round(end, 3)
    for time in log_time:        
        if time[0] > end or time[1] < start:            
            continue
        cnt += 1    
    return cnt


# lines = 	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]# 4
solution(lines)