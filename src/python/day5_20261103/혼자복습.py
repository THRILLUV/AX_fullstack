# 혼자복습.py



# 프로필 = {
#     "이름": "민수",
#     "나이": 20,
#     "생년월일": (2000, 3, 1)
# }
# print(f"이름: {프로필["이름"]} 나이: {프로필["나이"]}")    # 민수


# # 문자열 메서드 활용
# sentence = "python programming is fun"
# print(sentence.upper())         # 대문자로 변환하여 출력

# sentence = "PYTHON PROGRAMMING IS FUN"
# print(sentence.lower())        

# sentence = "PYTHON PROGRAMMING IS FUN"
# print(sentence.count("P"))    

# num1 = 10
# num2 = 3.14

# # 숫자열 연산
# sum_result = num1 + num2
# diff_result = num1 - num2
# product_result = num1 * num2
# division_result = num1 / num2
# integer_division_result = num1 // num2
# remainder_result = num1 % num2

# print("합:", sum_result)
# print("차:", diff_result)
# print("곱:", product_result)
# print("나누기:", division_result)
# print("정수 나누기:", integer_division_result)
# print("나머지:", remainder_result)

# num3 = -7.89
# abs_result = abs(num3)   # 절댓값 계산
# round_result = round(num3)  # 반올림 계산

# print("절댓값:", abs_result)
# print("반올림:", round_result)

# # 정수형 변수 선언
# num1 = 10
# num2 = -5

# # 정수형 변수끼리의 연산
# sum_result = num1 + num2
# print("합:", sum_result)  # 출력: 합: 5

# # 정수형 연산 결과
# print("합의 자료형:", type(sum_result))  
# # 출력: 합의 자료형: <class 'int'>

# # 실수형 변수 선언
# num3 = 3.14
# num4 = -0.8

# # 실수형 변수끼리의 연산
# product_result = num3 * num4
# print("곱:", product_result)  
# # 출력: 곱: -1.57

# # 실수형 연산 결과
# print("곱의 자료형:", type(product_result))  
# # 출력: 곱의 자료형: <class 'float'>


# # Boolean 변수 선언
# is_raining = True
# is_sunny = False


# # 비교 연산자를 사용하여 Boolean 값 비교
# x = 10
# y = 5

# greater_than = x > y
# print(greater_than)  # True 출력


# import pandas as pd

# # NaN을 포함한 데이터프레임 생성
# data = {'A': [1, 2, None],
#         'B': [3, None, 5]}
# df = pd.DataFrame(data)

# print(df)
# # 출력:
# #      A    B
# # 0  1.0  3.0
# # # 1  2.0  NaN
# # # 2  NaN  5.0

# name = input("이름을 입력하세요: ")
# print("안녕하세요,", name, "님!")


# num1 = int(input("첫 번째 숫자를 입력하세요: "))
# num2 = int(input("두 번째 숫자를 입력하세요: "))
# sum = num1 + num2
# print("두 숫자의 합은", sum, "입니다.")


# # 학생들의 성적 데이터를 변수에 할당
# grade1 = 85
# grade2 = 92
# grade3 = 78
# grade4 = 90
# grade5 = 88

# # 각 변수에 담긴 데이터 출력
# print("첫 번째 학생의 성적:", grade1)
# print("두 번째 학생의 성적:", grade2)
# print("세 번째 학생의 성적:", grade3)
# print("네 번째 학생의 성적:", grade4)
# print("다섯 번째 학생의 성적:", grade5)


# # 데이터를 변수에 할당
# data1 = 85
# data2 = 92
# data3 = 78
# data4 = 90
# data5 = 88

# # 데이터의 평균 계산
# total = data1 + data2 + data3 + data4 + data5  # 모든 데이터의 합을 계산
# count = 5  # 데이터의 개수를 직접 지정
# average = total / count  # 데이터의 평균을 계산

# # 결과 출력
# print("데이터 평균:", average)


# from sklearn.linear_model import LinearRegression

# # 선형 회귀 모델 객체 생성
# model = LinearRegression()

# # 리스트 생성
# numbers = [1, 2, 3, 4, 5]

# # 첫 번째 요소에 접근하기
# first_number = numbers[0]
# print("First number:", first_number)

# # 두 번째 요소에 접근하기
# second_number = numbers[1]
# print("Second number:", second_number)

# # 마지막 요소에 접근하기
# last_number = numbers[-1]
# print("Last number:", last_number)

# # 음수 인덱스를 사용하여 역순으로 요소에 접근하기
# second_last_number = numbers[-2]
# print("Second last number:", second_last_number)


# 리스트 생성
# my_list = [1, 2, 3, 4, 5]

# #리스트의 다양한 메서드(Methods)
# my_list.append(6) # 리스트에 새로운 항목 추가
# print(my_list)  # 출력: [1, 2, 3, 4, 5, 6]

# my_list.extend([7, 8, 9]) # 다른 리스트의 모든 항목을 추가
# print(my_list)  # 출력: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# my_list.insert(2, 10) # 두 번째 위치에 값 삽입
# print(my_list)  # 출력: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# my_list.remove(3) # 값 3 삭제
# print(my_list)  # 출력: [1, 2, 10, 4, 5, 6, 7, 8, 9]

# popped_value = my_list.pop(5) # 다섯 번째 위치의 값 제거하고 반환
# print(popped_value)  # 출력: 6
# print(my_list)  # 출력: [1, 2, 10, 4, 5, 7, 8, 9]

# print(my_list.index(4)) # 출력: 3 (값 4의 인덱스)

# print(my_list.count(7)) # 출력: 1 (값 7의 개수)

# my_list.sort() # 리스트 정렬
# print(my_list)  # 출력: [1, 2, 4, 5, 7, 8, 9, 10]

# my_list.sort() # 리스트 정렬
# print(my_list)

# my_list.reverse() # 리스트 역순으로 뒤집기
# print(my_list)  # 출력: [10, 9, 8, 7, 5, 4, 2, 1]

# my_list.sort(reverse=True) # 리스트 정렬
# print(my_list)


# # 중첩된 리스트에서 인덱싱하기
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list[2][2])  # 출력: 4 (두 번째 리스트의 첫 번째 항목)

# 리스트를 사용한 간단한 데이터 계산 예시
# grades = [85, 92, 88, 78, 90]
# average_grade = sum(grades) / len(grades)
# print("평균 성적:", average_grade)

# # 리스트에서 홀수 번째 인덱스의 값들 출력하기
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# odd_index_values = my_list[1::2]
# print("홀수 번째 인덱스의 값들:", odd_index_values)
# 역순 = my_list.sort(reverse=True)
# print(my_list)
 # 출력: [20, 40, 60, 80]

# # 숫자로 이루어진 리스트 정렬 예시
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.sort()
# print("정렬된 리스트:", numbers)  # 출력: [1, 1, 2, 3, 4, 5, 5, 6, 9]

# # 문자열로 이루어진 리스트 정렬 예시
# words = ['apple', 'banana', 'orange', 'grape', 'cherry']
# words.sort()
# print("정렬된 리스트:", words)  # 출력: ['apple', 'banana', 'cherry', 'grape', 'orange']

# # 내림차순으로 리스트 정렬 예시
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.sort(reverse=True)
# print("내림차순으로 정렬된 리스트:", numbers)  # 출력: [9, 6, 5, 5, 4, 3, 2, 1, 1]

# # 리스트의 문자열 길이로 정렬 예시
# words = ['apple', 'banana', 'orange', 'grape', 'cherry']
# words.sort(key=len)
# print("문자열 길이로 정렬된 리스트:", words)  # 출력: ['apple', 'grape', 'banana', 'cherry', 'orange']


# a, b = map(int, input().split())
# print(a + b)


# a, b = map(int, input())
# print(a + b)


# print(17 // 5)
# print(17 % 5)

# print(2 * 10)
# print(2 ** 3)

# print(10 / 3)
# print(10 // 3)

# a = 5
# print(a == 5)


# print(7 > 5)


# print(5 > 1 and 11 <= 10)



# my_name = "박태희"
# my_age = 34

# print("내 이름은" + my_name + "이고 ", my_age, "입니다.")

# print(f"내 이름은" , my_name + "이고", my_age, "입니다.")

# print(type(my_name))
# print(type(my_age))

# korean_scores = [78, 92, 85, 60, 88]

# print(korean_scores[0])
# print(korean_scores[-1])

# korean_scores.append(33)

# print(korean_scores)

# korean_scores.pop(3)
# print(korean_scores)
# korean_scores.insert(3, 70)
# print(korean_scores)


# korean_scores.append(95)
# print(korean_scores)

# korean_scores.sort()

# print(korean_scores)
# korean_scores.sort(reverse=True)
# print(korean_scores)

# 평균 = sum(korean_scores) / len(korean_scores)
# print(평균)


# korean_scores = [78, 92, 85, 60, 88]

# group_a = korean_scores[0:3]
# group_b = korean_scores[3:]

# print(group_a, group_b)

# reversed_scores = korean_scores[::-1]
# print(korean_scores)
# print(reversed_scores)


student_info = ("2026001", "김민준", 2010)


print(student_info)

print(student_info[0])