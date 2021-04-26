import sys
input = sys.stdin.readline

tc = 0
while True:
    brackets = input().strip()
    if '-' in brackets:
        break

    cnt = 0
    stack = []
    for bracket in brackets:
        # 여는 괄호 stack 추가
        if bracket == '{':
            stack.append(bracket)
        elif bracket == '}':
            if stack:
                # 마지막이 여는 괄호라면 괄호 한쌍 삭제
                if stack[-1] == '{':
                    stack.pop()
                # 마지막이 닫는 괄호라면 여는 괄호로 바꾸고 삭제
                elif stack[-1] == '}':
                    cnt += 1
                    stack.pop()
            else:
                stack.append(bracket)

    tc += 1
    if '}' in stack: # } {{{
        cnt += len(stack)//2 + 1
    else:
        cnt += len(stack)//2
    print(f'{tc}. {cnt}')
