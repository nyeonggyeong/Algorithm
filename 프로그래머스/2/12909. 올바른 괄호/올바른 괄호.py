def solution(s):
    stack = []  # 스택을 사용하여 열린 괄호를 추적
    
    for char in s:
        if char == '(':  # 열린 괄호가 나오면 스택에 추가
            stack.append(char)
        elif char == ')':  # 닫힌 괄호가 나오면
            if not stack:  # 스택이 비어있다면 짝이 맞지 않음
                return False
            stack.pop()  # 스택에서 열린 괄호 하나를 제거
    
    # 스택에 남아있는 열린 괄호가 있으면 짝이 맞지 않음
    return len(stack) == 0