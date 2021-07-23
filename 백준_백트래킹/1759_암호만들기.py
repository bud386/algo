import sys
input = sys.stdin.readline

L, C = map(int, input().split())
words = sorted(list(input().split()))

pick = []
vowel = ['a', 'e', 'i', 'o', 'u']

def combi(start, vowel_cnt, consonant_cnt):
    global L, C
    if len(pick) == L and vowel_cnt >= 1 and consonant_cnt >= 2:
        print(''.join(pick))        
        return
    for i in range(start, C):
        if words[i] in vowel:
            vowel_cnt += 1
        else:
            consonant_cnt += 1
        pick.append(words[i])
        combi(i+1, vowel_cnt, consonant_cnt)
        pick.pop()
        if words[i] in vowel:
            vowel_cnt -= 1
        else:
            consonant_cnt -= 1

combi(0, 0, 0)
