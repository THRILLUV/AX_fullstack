
# streamlitUi.py

import streamlit as st


def 입력창():

    # 화면 디자인 (ChatGPT 활용)
    st.markdown("""
    <style>
    .title-wrapper {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    .title-box {
        background: linear-gradient(120deg, #312E81, #7C3AED);
        width: 100%;
        max-width: 1480px;
        box-sizing: border-box;
        padding: 36px 26px;
        border-radius: 32px;
        color: white;
        text-align: center;
    }

    .title-box h1 {
        color: white;
        font-size: clamp(30px, 3.5vw, 48px);
        line-height: 1.3;
        margin: 0 0 12px;
        font-weight: 800;
    }

    .title-box p {
        color: #F3E8FF;
        font-size: clamp(17px, 1.7vw, 21px);
        line-height: 1.6;
        margin: 0;
    }

    /* 입력창 라벨과 숫자 */
    div[data-testid="stWidgetLabel"] p {
        font-size: 17px;
        line-height: 1.5;
        font-weight: 600;
    }

    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        font-size: 19px;
        min-height: 45px;
    }

    div[data-testid="stRadio"] label p {
        font-size: 18px;
    }

    div.stButton > button {
        min-height: 54px;
        font-size: 19px;
        font-weight: 700;
        background: #7C3AED;
        color: white;
        border-radius: 14px;
        border: none;
    }

    div.stButton > button:hover {
        background: #8B5CF6;
        color: white;
    }

    @media (max-width: 700px) {
        .title-box {
            padding: 26px 18px;
            border-radius: 24px;
        }

        div[data-testid="stWidgetLabel"] p {
            font-size: 16px;
        }
    }
    </style>

    <div class="title-wrapper">
        <div class="title-box">
            <h1>💘너랑 나랑 케미지수💘</h1>
            <p>너와 나 사이, 숫자로 말해줘</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ----------------------------------------
    # 01. 두 사람의 정보 입력
    # ----------------------------------------

    with st.container(border=True):

        st.subheader("01. 두 사람의 정보 입력")

        # 작성자와 상대방 이름
        이름열, 상대열 = st.columns(2)

        with 이름열:
            이름 = st.text_input("작성자 이름")

        with 상대열:
            상대이름 = st.text_input("궁금한 사람 이름")

        # 입력창을 좌우 2열로 나누기
        왼쪽, 오른쪽 = st.columns(2)

        with 왼쪽:

            # 대화 시간
            대화시간 = st.number_input(
                "두 사람이 대화한 시간(분)",
                min_value=0
            )

            if 대화시간 >= 300:
                st.info("🤭 이미 맥스일지도..?")

            # 흡연 취향
            흡연 = st.radio(
                "두 사람의 흡연 취향이 일치하나요?",
                ["Yes", "No"],
                horizontal=True
            )

            흡연값 = 1 if 흡연 == "Yes" else 0

        with 오른쪽:

            # 공통 관심사
            관심사 = st.number_input(
                "두 사람의 공통 관심사는 몇 개인가요?",
                min_value=0,
                step=1
            )

            # 개인 만남 횟수
            만남횟수 = st.number_input(
                "두 사람이 개인적으로 만난 횟수",
                min_value=0
            )

    return 이름, 상대이름, 대화시간, 관심사, 흡연값, 만남횟수
