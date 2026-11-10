# app.py


# Streamlit
# - 파이썬으로 웹사이트나 웹 애플리케이션을 쉽게
#   만들수있게 도와주는 도구!

# 설치
# pip install streamlit

#설치 확인
# streamlit --version
# as 줄임말

import streamlit as st

st.title("AI 리터러시 수업!")
st.write("AI 란?")
st.write("컴퓨터가 사람의 지능적인 작업을 수행하도록 만드는 기술이당")

# 2. 위에 내용을 실행!
# 

# streamlit run 파일명.py
# 터미널켜고 -> cmd -> python -m streamlist run app.py


st.header("규칙 기반 AI란?")
st.write("Rule-Based AI")
st.write("사람이 정한 규칙을 따르는 인공지능")


st.header("머신러닝")
st.write("데이터에서 규칙이나 패턴을 학습하는 기술")
st.write("사람이 모든 규칙을 직접 작성하지 않고 컴퓨터 데이터를 보고 패턴을 찾는다.")




st.image("1_ai.png")

st.image("1-1_rule.png")

st.image("2_ml.png")

st.header("딥러닝 {deep Learning)")

st.write("얼굴인식, 음성인식, 제품불량 이미지 판ㅁㄹ, 의료 영상 분석지원")
st.write("여러 층의 인공신경망을 이용하는 머신러닝 기술")

st.image("3_dl.png")


# 생성형 AI 란?

st.write("생성형 AI란 프롬프트를 통해 이미지, 오디오, 텍스트, 코드 등을 생성하는 AI이다")
st.write("전통적인 LLM(Large Languge Model)은 텍스트를 생성하지만, 이미지와 텍스트, 비디오, 오디오 등을 모두 처리 할 수 있는 멀티모달도 있다.")
st.image("4_genai.png")


# LLM이란

st.image("5_llm.png")

