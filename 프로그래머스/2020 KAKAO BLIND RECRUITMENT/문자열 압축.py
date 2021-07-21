def solution(s):
    ans = len(s)
    length = len(s)
    
    for i in range(1, length//2 + 1): # i 길이로 단어 자르기
        tmp = s[:i]
        cnt = 1
        new_s = ''
        for j in range(i, length+i, i): # j번째부터 i 길이만큼 자르기
            if tmp == s[j: j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    new_s += tmp
                else:
                    new_s = new_s + str(cnt) + tmp
                tmp = s[j:j + i]
                cnt = 1
        ans = min(ans, len(new_s))
    return ans

solution("ababcdcdababcdcd")