import sys

word = list(map(str, sys.stdin.readline().strip()))
word = sorted(word)

word_cnt = {}
for i in range(len(word)):
    word_cnt[word[i]] = word.count(word[i])

possible = True
odd_cnt = 0

# 글자수가 홀수인게 1개일때만 가능
if len(word) % 2:
    for cnt in word_cnt.values():
        if cnt % 2:
            odd_cnt += 1
            if odd_cnt == 2:
                possible = False
                break

# 글자수가 홀수인게 있으면 불가능
else:
    for cnt in word_cnt.values():
        if cnt % 2:
            possible = False
            break

ans = ''
if possible:
    if len(word) % 2:
        for idx, val in word_cnt.items():
            ans += idx*(val//2)
            if val % 2:
                middle_word = idx
        ans += middle_word + ans[::-1]
        
    else:
        for idx, val in word_cnt.items():
            ans += idx*(val//2)
        ans += ans[::-1]

else:
    ans = "I'm Sorry Hansoo"

print(ans)




# ans = ''
# if possible:
#     if len(word) % 2:
#         for idx, val in word_cnt.items():
#             ans += idx*(val//2)
#             if val % 2:
#                 middle_word = idx
#                 word.remove(idx)
#         ans += middle_word
#         for i in range(len(word)-1, 0, -2):
#             ans += word[i]

#     else:
#         for i in range(0, len(word), 2):
#             ans += word[i]
#         for i in range(len(word)-1, 0, -2):
#             ans += word[i]
# else:
#     ans = "I'm Sorry Hansoo"

# print(ans)







