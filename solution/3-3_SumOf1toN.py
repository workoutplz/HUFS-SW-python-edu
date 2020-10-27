"""
N까지의 합
- 숫자 하나를 입력
- 1부터 N까지 숫자의 합을 출력
"""
number = int(input("숫자 하나를 입력해주세요 : "))
i = 0
result = 0

while i<=number:
    result += i
    i+=1

print(f'1부터 {number}까지의 합은 {result}입니다.')