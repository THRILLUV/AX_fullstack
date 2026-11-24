# kakaojoin.py

import sqlite3 as db
import streamlit as st

#1. 저장소 만들기

db저장소 = db.connect("kakao.db")
#2. 조작도구 만들기
마우스 = db저장소.cursor()

# 3. 카카오톡 회원가입 페이지만든다.
#  아이디,비밀번호,이름,전화번호는 꼭 입력한다.

# 칸마다 3질문
# 이 칸으로 정확히 한 사람을 가리키나?
# 이 칸이 비어있으면 안되나?
# 이 칸이 다른사람이랑 겹치면 안되나?

# 데이터베이스에서 테이블을 관리하기 위해서
# 카톡 비유 친구,쇼핑,선물하기 등등
# 회원 테이블을 같이 쓴다.
# 오픈채팅탭 개발자가 비어있는값을 확인하는 if문
# 까먹음?



마우스.execute("""
    create table if not sxists members(
        회원번호    integer  primary key  autoincrement,
        아이디      text     not null   unique,
        비밀번호    text     not null,
        이름        text     not null,
        전화번호    text     not null   unique 
    )



""")

# not null 만 컬럼에 지정하면 값을 필수!
# 단 중복되는 값들이 들어올 수 있다.
# 컬럼마다 어떤건 중복되도 되고 어떤건 안된다. 정해줘야함. (데이터 무결성)
# 중복되면 안되는 곳에는 unique를 써서 추가 설정한다.

# 모든 데이터를 저장하는 테이블에 대표 번호
# DB관리자(성능,백업,튜닝,권한,계정관리) - DBA
# OCP 자격증
# 제약조건을 꼭 확인한다.

st.title("카카오 회원가입")
아이디 = st.text_input("아이디").strip()
비밀번호 = st.text_input("비밀번호", type="password").strip()
이름 = st.text_input("이름").strip()
전화번호 = st.text_input("전화번호 (예: 010-1234-5678)").strip()

# 입력값들은 공백이 들어가면 문제가 발생할 수있다!
# varchar 타입은 글자수를 제한할 수있다.
# not null은 값을 무조건 가져와라! 값이 비면 안된다!
# 글자수 제한과는 무관하다!
if st.button("가입하기"):
    마우스.execute(f"""
        insert into
            members(아이디,비밀번호,이름,전화번호)
        values
            ('{아이디}','{비밀번호}','{이름}','{전화번호}')
    """)

    db저장소.commit()


# AI챗봇 회원별 대화 기록 primary key
# 머신러닝 학습 데이터
#   같은 회원이 들어가면 쏠림 현상
#   unique 처음부터 막기
# 업무 자동화