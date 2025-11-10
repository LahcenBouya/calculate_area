import math
def calcul_area(height,width,cover):
    area=height * width
    number_of_cans=math.ceil(area / cover)
    print(f"the number of cans is {number_of_cans}")
test_height=int(input("please enter the height: "))
test_width=int(input("please enter the width: "))
coverage=5
calcul_area(height=test_height,width=test_width,cover=coverage)