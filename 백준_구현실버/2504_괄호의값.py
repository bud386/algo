import sys

brackets = list(sys.stdin.readline().strip())


# 올바른 괄호열인지 체크하는 함수
def check_true(brakets):
    stack = []
    for bracket in brackets:
        
        # 여는 괄호열이면 stack에 추가
        if bracket == '(' or bracket == '[':
            stack.append(bracket)
        
        # stack이 비어있지 않고(앞에 여는 괄호열이 있을때) 닫는 괄호열')' 일때 stack의 마지막값(LIFO) 확인
        # 짝이 맞으면 지우고 아니면 stack에 추가
        elif bracket ==')' and stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(bracket)
        
        # stack이 비어있지 않고 닫는 괄호열']' 일때 stack의 마지막값(LIFO) 확인
        # 짝이 맞으면 지우고 아니면 stack에 추가
        elif bracket ==']' and stack:
            if stack[-1] == '[':
                stack.pop()
            else:
                stack.append(bracket)
    
    # stack에 값이 존재한다면 안맞다는 의미
    if stack:
        return False
    # 짝이 다 맞아서 다 지워지면 올바른 괄호열
    else:
        return True

def calculation(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '(' or bracket == '[':
            stack.append(bracket)
        elif bracket == ')' and stack:
            if stack[-1] == '(':
                stack[-1] = 2

            # 괄호가 여러개 쌓여있는 경우
            else:
                temp = 0
                # 마지막에 들어온것부터 0번째 인덱스까지 (LIFO)
                # 괄호가 겹겹이 쌓여있으면 마지막 인덱스에는 괄호가 아닌  숫자가 들어가 있음
                # 그 숫자를 temp에 계속 더해주다가 마지막 괄호에서 곱해주는 과정
                for i in range(len(stack)-1, -1, -1):
                    # '()' 로 겹겹이 쌓여있을떄
                    # 마지막으로 감싸주는 부분에서 *2 해준다.
                    if stack[i] == '(':
                        stack[-1] = temp * 2
                        break
                    # 마지막 인덱스에 숫자가 들어있는 경우 계속 더해준다.
                    else:
                        temp += stack[i]
                        stack.pop()
        
        elif bracket ==']' and stack:
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                temp = 0
                for i in range(len(stack)-1, -1, -1):
                    # '()' 로 겹겹이 쌓여있을떄
                    if stack[i] == '[':
                        stack[-1] = temp * 3
                        break
                    # 마지막 인덱스에 숫자가 들어있는 경우 계속 더해준다
                    else:
                        temp += stack[i]
                        stack.pop()
    return sum(stack)
        


if check_true(brackets) == False:
    print(0)
else:
    print(calculation(brackets))