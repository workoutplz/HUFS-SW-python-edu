"""
나에 대한 정보를 입력하여 나를 소개해주는 프로그램을 만들어 봅시다!
필수 정보 : 이름, 나이, 재학 중인 학교의 이름
"""
name = input("너의 이름은? ")
age = input("너의 나이는? ")
school_location = input("너의 학교의 위치는? ")
school_name = input("너의 학교의 이름은? ")
birthday = input("너의 생일은? ")
home = input("너의 집은? ")

print(f"안녕, 나의 이름은 {name}이야!")
print(f"나의 나이는 {age}살이야.")
print("그리고 나는 지금 %s에 있는 %s를 다니고 있어." % (school_location, school_name))
print("내 생일은 {0}이니깐 참고해줘! ㅎㅎ\n그리고 나는 {1}에 살고 있어!".format(birthday, home))