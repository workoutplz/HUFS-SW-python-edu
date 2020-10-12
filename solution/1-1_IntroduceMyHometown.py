"""
나의 도시를 소개하는 프로그램을 만들어봅시다!
- 포맷팅 방법 3가지를 각각 최소 한 번씩은 사용해야함.
- 도시 이름, 랜드마크에 대한 정보는 반드시 넣을 것.
"""
city_name = "부산"
landmark = "광안대교"
food = "국밥"
distance = 366

print(f"{city_name}에 대해서 소개합니다!")
print("%s에는 %s가 있습니다." % (city_name, landmark))
print("{0}이 맛있습니다.".format(food))
print("용인에서 %s까지 %dkm정도 떨어져있습니다." % (city_name, distance))