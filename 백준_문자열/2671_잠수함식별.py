import re
import sys
input = sys.stdin.readline

string = input().strip()
pattern = re.compile('(100+1+|01)+') # 정규식 패턴을 정규식 객체로 컴파일합니다
m = pattern.fullmatch(string) # 전체 string이 정규식 pattern과 일치하면 True를 반환. 문자열이 패턴과 일치하지 않으면 None을 반환.
if m: 
    print("SUBMARINE")
else: 
    print("NOISE")
