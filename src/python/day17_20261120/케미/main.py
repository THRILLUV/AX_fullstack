import streamlit as st
from streamlitUi import 입력창
from friendshipPredict import 친밀도예측
from resultUi import 결과화면

# 화면 설정
st.set_page_config(
    page_title="너랑 나랑 케미지수",
    layout="wide"
)

# 사용자 입력
이름, 상대이름, 대화시간, 관심사, 흡연값, 만남횟수 = 입력창()

# 친밀도 계산
if st.button("💘 친밀도 계산하기"):

    if 이름.strip() == "" or 상대이름.strip() == "":
        st.warning("두 사람의 이름을 모두 입력해 주세요.")

    else:
        점수 = 친밀도예측(
            대화시간,
            관심사,
            흡연값,
            만남횟수
        )

        결과화면(이름, 상대이름, 점수)