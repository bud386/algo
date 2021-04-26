import sys
input = sys.stdin.readline

N = int(input())

# 회문검사
def palindrome(n):
    start = 0
    end = len(n) - 1
    while start < end:
        if n[start] != n[end]:
            return False
        start += 1
        end -= 1
    return True

# 에라토스테네스의 체
maxi = 1003001  # 1,000,000이상일때 가장 작은 소수이면서 회문인 수
num_list = [True for _ in range(maxi+1)] # True일때 소수

for i in range(2, maxi//2 + 1): # 최대약수는 자기 자신 나누기 2
    if num_list[i] == True: # 소수이면 
        for j in range(2*i, maxi+1, i): # 자기자신 제외 자신의 모든 배수 제거(False처리)
            num_list[j] = False
prime_palindrome = [i for i in range(2, maxi+1) if num_list[i] and palindrome(str(i)) ] # 소수이면서 회문인 숫자저장

for num in prime_palindrome:
    if num >= N:
        print(num)
        break