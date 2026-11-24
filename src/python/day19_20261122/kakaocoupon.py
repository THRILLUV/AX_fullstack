# kakaocoupon.py

# 내가만든 모듈 가져오기

import my


# my 라고 하는 모듈 안에 스트림릿 타이틀을 사용

my.st.title("쿠폰 보내기")

# 테이블 제약조건 넣어서 생성하기!
# 테이블명 : coupons


# 선물하기에서 선물을 보내면 선물번호가 자동으로 생긴다.
# 보내는사람 아이디, 받는 사람아이디, 전화번호 상품이름은 꼭 있어야한다.
# 받는사람은 쿠폰 번호로 상품을 받는다.
# 쿠폰번호는 절대 겹치면 안되고 값이 꼭 있어야한다.
# 카드 메세지는 안 써도 된다.

# 데이터 타입, 제약조건, 생성하는 코드


# user_id - text
# 전화번호 - text = ("ex) 010-0000-0000").strip()
#   ㄴ 전화번호는 user_id 에 포함
# 보내는 사람 - user_id
# 받는 사람 - user_id

# 선물번호 - integer - 중복 절대 X - 
#   ㄴ integer primary key autoincremet unique, 
#   ㄴ 선물번호는 user_id 아래에 종속

# 쿠폰번호 - integer - 중복 절대 X 순서대로 생겨야함 
#   ㄴ integer primary key autoincremet unique, 

# 카드메세지 - msg - text


# 필수 : 보내는아이디, 받는아이디
#     : 받는사람의전화번호(중복X)
#     : 상품이름, 쿠폰번호(중복X)
# 선택 : 카드메시지

# 쿠폰보내기를 하려면 로그인이 필요하다.
# 내가 로그인이 되어있는지 - TF로
# 친구목록을 조회해야하기 때문에.
# 받는사람의 아이디,전화번호가 존재 하는지?

# 1. db 모듈에서 불러오기
db저장소 = my.db.connect("kakao.db")
# 2. 조작도구
마우스 = db저장소.cursor()

my.st.subheader("로그인 실습")
로그인탭,가입탭 = my.st.tabs(["로그인","회원가입"])


# 로그인 탭을 누르면 로그인 할 수 있는 화면
with 로그인탭:
    아이디 = my.st.text_input("아이디", key="로그인_아이디").strip()
    비밀번호 = my.st.text_input("비밀번호", type="password", key="로그인_비번").strip()

    # 디비 조회 해야함
    마우스.execute(f"""
        select          -- 3. 조회
            아이디
        from            -- 1. 시작은 프롬
            members
        where           -- 2. 특정조건 확인
            아이디 = '{아이디}'
    
""")
    회원 = 마우스.fetchone()
    my.st.write("찾은 아이디: ", 회원)


# # 가입탭을 누르면 가입창이 뜬다.
# with 가입탭:
#     pass








# 선물db = db.connect("gift.db")







# 받는사람 = my.st.text_input("선물을 받을 분의 ID를 입력하세요.")


