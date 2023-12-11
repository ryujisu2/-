def sub(n):
    if n <= 1:
        return n
    return sub(n-1) + sub(n-2)

#소스코드가 실행되지 않아 아래 코드를 추가하여 실행하였습니다.
print(sub(3))
print(sub(2))
print(sub(1))