def solution(s):
    num = ''
    result = []
    for i in s:                
        if 48 <= ord(i) <= 57:
            num += i
        else:
            if num:                
                result.append(int(num))
            num = ''
    
    answer = {} 
    key = set(result)
    for i in key:
        answer[i] = result.count(i)
    answer = sorted(answer, key= lambda x : answer[x], reverse=True)
    
    return answer