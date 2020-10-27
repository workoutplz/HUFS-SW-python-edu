"""
소문자와 대문자
- Hi,I,am,wonjun 을 입력
- , 기준으로 나누어 그 중 0번째는 소문자, 2번째는 대문자로 바꿔주기
"""

myString = input("문자열을 입력하세요.")
tmp = myString.split(",")
tmp[0] = tmp[0].lower()
tmp[2] = tmp[2].upper()