"""
0부터 n까지, n부터 0까지
- 숫자 하나를 입력
- 0부터 n까지 출력, n부터 0까지 출력
"""
n = int(input("숫자 하나를 입력하세요 : "))
i = 0

while i<=n:
    print(i)
    i += 1
i=n
print("----------")
while i>=0:
    print(i)
    i-=1