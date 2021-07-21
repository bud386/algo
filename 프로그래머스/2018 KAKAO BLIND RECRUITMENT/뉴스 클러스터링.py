def solution(str1, str2):
    answer = 0
    new_str1 = {}
    new_str2 = {}
    str1 = str1.lower()
    str2 = str2.lower()

    # 단어 나누고, 개수 확인
    for i in range(len(str1)-1):
        if 'a' <= str1[i] <= 'z' and 'a' <= str1[i+1] <= 'z':
            if str1[i:i+2] in new_str1:
                new_str1[str1[i:i+2]] += 1
            else:
                new_str1[str1[i:i+2]] = 1

    for i in range(len(str2)-1):
        if 'a' <= str2[i] <= 'z' and 'a' <= str2[i+1] <= 'z':
            if str2[i:i+2] in new_str2:
                new_str2[str2[i:i+2]] += 1
            else:
                new_str2[str2[i:i+2]] = 1


    union = [] # 합집합
    intersection = [] # 교집합
    for word1 in new_str1:
        if word1 in new_str2:
            min_cnt = min(new_str1[word1], new_str2[word1])
            max_cnt = max(new_str1[word1], new_str2[word1])
            for i in range(min_cnt):
                intersection.append(word1)
            for i in range(max_cnt):
                union.append(word1)
        else:
            for i in range(new_str1[word1]):
                union.append(word1)

    for word2 in new_str2:
        if word2 in new_str1:
            continue
        for i in range(new_str2[word2]):
            union.append(word2)

    # print(intersection, union)
    if union:
        answer = len(intersection) / len(union) * 65536
    else:
        answer = 65536

    print(int(answer))
    return int(answer)


str1 = 'E=M*C^2'
str1 = 'FRANCE'
str2 = 'e=m*c^2'
str2 = 'french'
solution(str1, str2)