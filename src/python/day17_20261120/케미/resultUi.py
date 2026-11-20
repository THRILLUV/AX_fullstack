import streamlit as st
from html import escape


def 결과화면(이름, 상대이름, 점수):

    st.divider()
    st.subheader(f"💘 {이름}님과 {상대이름}님의 케미지수")

    이름표시 = escape(이름)
    상대표시 = escape(상대이름)

    # ----------------------------------------
    # 결과 화면 디자인
    # ----------------------------------------

    st.markdown("""
    <style>
    .winner-card {
        background: linear-gradient(145deg, #402077, #6D28D9);
        border: 2px solid #B69DFB;
        border-radius: 24px;
        padding: 32px 22px;
        min-height: 438px;
        box-sizing: border-box;
        text-align: center;
        color: white;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(76,29,149,0.25);
    }

    .winner-crown {
        font-size: 76px;
        line-height: 1.1;
        margin-bottom: 15px;
    }

    .winner-label {
        color: #EEE4FF;
        font-size: 17px;
        font-weight: 700;
        letter-spacing: 0.8px;
    }

    .winner-name {
        font-size: clamp(34px, 3.3vw, 50px);
        line-height: 1.25;
        font-weight: 800;
        margin: 18px 0 10px;
        color: white;
    }

    .winner-score {
        font-size: clamp(64px, 6vw, 94px);
        line-height: 1.15;
        font-weight: 900;
        color: #FFE49A;
    }

    .winner-desc {
        font-size: 19px;
        line-height: 1.6;
        color: #F3E8FF;
        margin-top: 18px;
        font-weight: 600;
    }

    .rank-card {
        background: #1B2030;
        border: 1px solid #545D74;
        border-radius: 18px;
        padding: 22px 24px;
        min-height: 134px;
        box-sizing: border-box;
        margin-bottom: 12px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .rank-label {
        color: #DDD0FF;
        font-size: 18px;
        font-weight: 750;
    }

    .rank-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 12px;
    }

    .rank-name {
        color: #FFFFFF;
        font-size: clamp(24px, 2.7vw, 34px);
        line-height: 1.3;
        font-weight: 800;
    }

    .rank-score {
        color: #FFE49A;
        font-size: clamp(28px, 3vw, 38px);
        line-height: 1.2;
        font-weight: 850;
        white-space: nowrap;
    }

    @media (max-width: 700px) {
        .winner-card {
            min-height: 360px;
            padding: 26px 16px;
        }

        .winner-crown {
            font-size: 64px;
        }

        .winner-desc {
            font-size: 17px;
        }

        .rank-card {
            min-height: 118px;
            padding: 18px 20px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # ----------------------------------------
    # 두 사람의 친밀도 점수 표시
    # ----------------------------------------

    왼쪽, 가운데, 오른쪽 = st.columns([1, 2, 1])

    with 가운데:

        st.markdown(f"""
        <div class="winner-card">
            <div class="winner-crown">💘</div>
            <div class="winner-label">CHEMISTRY SCORE</div>
            <div class="winner-name">
                {이름표시} × {상대표시}
            </div>
            <div class="winner-score">{점수:.1f}점</div>
            <div class="winner-desc">
                두 사람의 예상 친밀도입니다!
            </div>
        </div>
        """, unsafe_allow_html=True)