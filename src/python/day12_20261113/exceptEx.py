# 파일명 : exceptEx.py

# 예외처리
#   ㄴ 프로그램이 에러가 나도 죽지 않게 막고, 에러가 무엇인지 알아내는 방법
#   ㄴ 비정상적인 종료 막기1

#   ㄴ 실생활:
#       ㄴ 에어백, 멀티탭 (과전류 차단), 


# try
# ㄴ 문제가 발생할 수 있는 코드를
# except
#   에러나 예외가 발생하면 처리할 수 있는 코드들.

# 나이를 입력받아서 청소년인지 성인인지 구별?

# 1. 저장할 데이터는?
# 사용자의 나이,
# 성인이 몇살인지 기준나이

# 2. 실행 순서?
#   ㄴ 1. 사용자 나이 입력을 받는다.
#   ㄴ 2. 성인기준 나이와 비교한다.
#   ㄴ 3. 출력한다.

# 3. 생길수 있는 에러는?
#    ㄴ 숫자와 한글 병기 OR 한글로만 (십육세) 할경우.
#   ㄴ 공백이 있는경우.
#   ㄴ 불가능한 나이

# 프로그램의 정상 실행
#   ㄴ 내가 가지고 있는 모든 코드가 실행이 된다.


# try:
#     나이 = int(input("나이를 입력하세요: "))

#     if 나이 > 19:
#         print("성인")
#     else:
#         print("청소년")
        
# except : 
#     print("에러다!")
    
# print("정상종료")


# 웹사이트 만든다.
# 1. 도구 먼저 가져오기(포함하기)

import streamlit as st

st.title("예외처리")
st.header("try ~ excpet")


st.subheader("나이를 입력받아서 내년 나이를 출력하세요!")

# text_input() 모든 데이터가 문자로 온다.
# list1 = [1,2,3]
# print(list1[3])

# try:
#     나이 = int(input("나이: "))

#     if 나이 > 19:
#         print("성인")

#     else:
#         print("청소년")
# except :
#     print("에러다!")

# print("정상종료!")

# 웹 사이트 만든다
# 1. 도구 먼저 가져오기(포함하기)

# 터미널
# streamlit run exceptEx.py
#
import streamlit as st

# st.title("예외처리")
# st.header("try ~ excpet")

# st.subheader("나이를 입력받아서 내년 나이 출력하세요!")

# text_input() 모든 데이터가 문자로 온다.
# value_error
#  시작하자마자 에러난 이유는
#  스트림릿은 위에서 부터 아래로 쓰윽! 코드를 한번씩 실행
#  비어있는 채로 "" 숫자로 변환할려고 하다 보니
#  빈 문자를 숫자로 못 바꿔서 에러가 발생!

# try:
#     나이 = st.text_input("나이 입력:")

#     나이 = int(나이)
#     st.write("내년엔", 나이 +1 ,"살")

# except ValueError as e:  # 발생한 에러에 대한 내용을 e 변수에 저장한다
#     print("개발자 확인용: " ,e)  # 개발자만 확인용
#     #st웹사이트 화면에 띄우기 위해서! st도구를 사용한다
#     st.write("문자가 아니라 숫자를 입력해주세요!") #고객한테는 쉽게 바꿔서 보여줘야된다.

#-------------------------------------------------------
# 주문 평균 금액
# 오늘 하루의 주문 평균을 계산해서 화면에 보여주는 간단한 코드
# value 설정은 기본값 설정
# st.subheader("주문 평균 금액")

# try:
#     총합 = st.number_input("총 매출:",value=1000000)
#     주문건수 = st.number_input("주문 건수: ", value=10)
#     st.write("평균:", 총합 / 주문건수 , "원")
# except ZeroDivisionError as e:
#     print("개발자 확인용: ",e)
#     st.write("오늘은 주문이 없어요.")



#===========================

# 친구 이름 찾기
st.header("친구 이름 찾기")

# 친구목록 = ["민수", "지영", "철수"]


# # 1. 친구 목록 전체 출력
# st.write(친구목록)

st.header("친구 이름 찾기")

친구목록 = ["민수", "지영", "철수"]

st.write(친구목록)

# # 2. 몇번째 친구 입력할지? number_input()



# # 3. 선택한 친구의 이름을 출력하시오!
# #    없는 친구 " 그 번호의 친구는 없어요!"
# if 번호 <= -1:
#     st.warning("그 친구 번호는 없음!")
# else:


# 번호 = int(st.number_input("몇 번째 친구? 0부터", value=0, step=1))

# try:
#     번호 = int(st.number_input("몇 번째 친구? 0부터", value=0, step=1))
#     st.write(친구목록[번호])
# except IndexError:
#     st.write("그 번호의 친구는 없어요!")

# try:
   
#    친구 =  st.write(친구목록[번호])
# except:
#     st.warning("그 번호의 친구는 없어요!")




try:
    번호 = int(st.number_input("몇번째 친구를 선택할?? 0부터 시작임", value=0, step=1, min_value=0, max_value=2))
    st.write(친구목록[번호])
except:
    print("에러다!")
    st.warning("그 친구의 번호는 없어요")

# 번호글자 = st.text_input("몇번째 친구를 선택할?? 0부터")

# if 번호글자:
#     try:
#         번호 = int(번호글자)
#         st.write(친구목록[번호])
#     except IndexError:
#         st.write("그 번호의 친구는 없음!")
#     except ValueError:
#         st.write("숫자로 입력해라!")


# 강사님께 Q&A

# 박태희(AX_4기)  [오후 1:28]
# try:
#     번호 = int(st.number_input(“몇번째 친구를 선택할?? 0부터 시작임“, value=0, step=1, min_value=0, max_value=2))
#     st.write(친구목록[번호])
# except:
#     print(“에러다!”)
#     st.warning(“그 친구의 번호는 없어요“)[오후 1:28]아예 최소값 최대값 제한해놓으면 에러 메세지 띄울일도 없겠죠?
# 이서희(튜터/AX/4기)  [오후 1:32]
# 당연합니다~
# [오후 1:32]하지만 친구라는건 계속 추가가 되기 때무에~ 유동적으로 변할 수있습니다~


# 내생각 : 그럼 최솟값만 0으로 제한하고 추가되는 친구목록에만 warning으로 메시지 뜨게하면 되겠다.