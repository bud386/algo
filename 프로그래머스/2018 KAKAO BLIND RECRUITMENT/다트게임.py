def solution(dartResult):
    i = 0
    n = len(dartResult)
    scores = []

    while i < n:
        score = 0
        # 숫자 확인
        if '0' <= dartResult[i] <= '9' and dartResult[i+1] == '0':
            dart = int(dartResult[i:i+2])
            i += 2
        if '0' <= dartResult[i] <= '9' and dartResult[i+1] != '0':
            dart = int(dartResult[i])
            i += 1        

        # 보너스 확인
        if dartResult[i] == 'S':
            score += dart
            i += 1
        elif dartResult[i] == 'D':
            score += dart ** 2
            i += 1
        elif dartResult[i] == 'T':
            score += dart ** 3
            i += 1
        scores.append(score)

        if i >= n:
            break
        
        # 옵션 확인
        if dartResult[i] == '*':
            if len(scores) < 2:
                scores[-1] *= 2
            else:
                scores[-1] *= 2
                scores[-2] *= 2
            i += 1
        elif dartResult[i] == '#':
            scores[-1] *= -1
            i += 1

    answer = sum(scores)
    return answer

dartResult = '1T2D3D#'
solution(dartResult)