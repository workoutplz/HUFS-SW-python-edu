# 포맷 코드를 이용한 포매팅
number = 20
name = "이원준"
height = 185.1
print("저는 %d살입니다." % number)
print("제 이름은 %s입니다." % name)
print("저는 %s이고, 제 나이는 %d살입니다." % (name, number))
print("제 키는 %f입니다." % height)
# print("제 키는 %.1f입니다." % height)

# format 함수를 이용한 포매팅
print("저는 {0}살이고, 제 이름은 {1}입니다.".format(number, name))

# f 를 활용한 포매팅
print(f"제 키는 {height}이고요, 제 이름은 {name}입니다.")

# f를 활용하면 다양한 옵션을 줄 수도 있습니다.
print(f'{"왼쪽 정렬":<20}')
print(f'{"오른쪽 정렬":>20}')
print(f'{"가운데 정렬":^20}')