# 게임 만들기
# 


# 1. 숫자입력!
# 2. 비교정답 보다 작으면 up!

# 정답 보다 크면 down!
# int, input, if, else, True, False, >=, 결과, print
# 정답은 8이고 터미널에 입력하게 해야하니까 input이 들어가야하고,
# print는 결과 = 로 딱 한번만 써서 표현해야 할 것 같고, 
# 8 미만은 모두 Up이 결과가 되게
# 8 초과는 모두 Down 이 결과가 되게
# 8일경우 True가 되서 정답!!이 되게

# 참고 
# #
# if True:
#   print("정답")

# else:
    #print("거짓")

# 주문금액이 15000원 이상이면 주문가능
#        15000원 이하면 주문 불가능


정답 = 8

입력값 = int(input("정답을 맞춰보세요! =  "))


# if 입력값 == 정답:
#     print("정답입니다")

# elif 입력값 <= 8:
#     print("Up..!")

# elif 입력값 > 8:
#     print("Down..!")
# 정답 = 8


# 입력값 = int(input("정답을 맞춰보세요! =  "))


if 입력값 == 정답:
    print("정답입니다")

elif 입력값 <= 정답:
    print("Down..!""")
    
elif 입력값 >= 정답:
    print("Up..!")

# elif 입력값 > 정답:
#     print("Down..!")
    

