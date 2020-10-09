"""
나의 도시를 소개하는 프로그램을 만들어 봅시다!
필수 정보 : 도시 이름, 랜드마크
"""
city_name = "부산"
landmark = "광안대교"
food = "국밥"
distance = 366

print(f"{city_name}에 대해서 소개합니다!")
print("%s에는 %s가 있습니다." % (city_name, landmark))
print("{0}이 맛있습니다.".format(food))
print("용인에서 %s까지 %dkm정도 떨어져있습니다." % (city_name, distance))