# 칸트 출석 계산기 PRD
# 코드 위에 적어 둔 범위입니다. 화면으로 보여 주지 않습니다.
#
# 누가 씁니까
# 칸트 수강생이 씁니다. 이름과 전화번호는 받지 않습니다.
#
# 무엇을 입력합니까
# 고용24 출결 현황을 입력합니다.
# 출석, 지각, 조퇴, 외출, 결석 횟수입니다.
# 내 출석률과 전체 출석률을 입력합니다.
# 공가는 두 칸으로 나눕니다.
# 결석으로 잡혀 있던 날에 쓴 공가는 결석 1일을 뺍니다.
# 지각, 조퇴, 외출로 잡혀 있던 날에 쓴 공가는 그 횟수 1번을 뺍니다.
#
# 무엇을 보여 줍니까
# 지금 추세대로 과정 끝까지 출결한다고 가정합니다.
# 그때의 수료 확률을 보여 줍니다.
# 제적당하지 않으려면 결석을 몇 번 더 할 수 있는지도 보여 줍니다.
# 공가는 한도에서 신청 횟수를 빼서, 남은 횟수를 보여 줍니다.
#
# 계산 규칙
# 전체 훈련일수의 20% 이상 결석이면 제적입니다. 190일이면 38일 이상입니다.
# 단위기간은 한 달입니다. 그 달 출석이 50% 이하면 제적입니다.
# 지각, 조퇴, 외출은 3번을 결석 1일로 셉니다. 횟수를 3으로 나눕니다.
# 결석일에 쓴 공가는 결석 일수에서 빼고, 조퇴·지각·외출에 쓴 공가는 3번 모음에서 뺍니다.
# 공가 한도는 전체 소정훈련일수의 10%입니다. 소수 첫째 자리에서 반올림합니다. 190일이면 19일입니다.
# 09:10 입실, 17:50 퇴실 같은 하루 시각 판정은 넣지 않습니다. 고용24에 이미 나온 숫자를 입력합니다.
#
# 로지스틱은 어디에 씁니까
# 남은 결석 횟수와 남은 공가는 규정으로 계산합니다.
# 이미 쓴 공가는 지금까지의 결석에서만 뺍니다. 앞으로의 속도에는 넣지 않습니다.
# 로지스틱은 그 예상 결석을 넣고, 수료 확률과 제적 확률을 보여 주는 데만 씁니다.

import streamlit as st
from sklearn.linear_model import LogisticRegression

st.set_page_config(page_title="QR출결", page_icon="🇰🇷")
st.markdown(
    """
    <style>
    .stApp {background: #f3f4f6;}
    .block-container {max-width: 860px; padding-top: 5rem !important;}
    [data-testid="stHeader"] {background: #f3f4f6;}
    [data-testid="stHeading"], [data-testid="stHeadingWithActionElements"] {overflow: visible;}
    h1, h2, h3 {line-height: 1.45; padding-top: 0.4rem;}
    div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) [data-testid="stColumn"] {min-width: 150px;}
    h1, h2, h3, p, label, .under {color: #222 !important;}
    div[data-testid="stButton"] button {
        background: #5d6d89 !important; border: none !important;
    }
    div[data-testid="stButton"] button p {color: #fff !important;}
    div[data-testid="stAlert"],
    div[data-testid="stAlertContainer"],
    div[data-testid="stAlertContentSuccess"],
    div[data-testid="stAlertContentWarning"],
    div[data-testid="stAlertContentError"],
    div[data-testid="stAlertContentInfo"] {
        background: #fff !important; color: #222 !important; border: 1px solid #d0d5dd !important;
    }
    div[data-testid="stAlert"] p,
    div[data-testid="stAlert"] * {color: #222 !important;}
    div[data-testid="stMetric"] {
        background: #fff; border: 1px solid #e3e3e3; border-radius: 12px; padding: 10px 12px;
    }
    div[data-testid="stMetricLabel"] p,
    div[data-testid="stMetricValue"],
    div[data-testid="stMarkdownContainer"] p,
    div[data-testid="stMarkdownContainer"] code,
    div[data-testid="stCaptionContainer"] p {color: #222 !important; background: transparent !important;}
    div[data-testid="stNumberInput"] input {
        background: #fff !important; color: #222 !important; border: 1px solid #e3e3e3 !important;
    }
    div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) [data-testid="stNumberInputContainer"] {
        position: relative; width: 84px; height: 84px; margin: 0 auto;
        background: #5d6d89; border-radius: 50%; overflow: hidden;
    }
    div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) div[data-testid="stNumberInput"] input {
        position: absolute; inset: 0; width: 84px !important; height: 84px !important;
        background: transparent !important; color: #fff !important; border: none !important;
        border-radius: 50% !important; font-size: 26px !important; font-weight: 700;
        text-align: center; padding: 0 0 16px 0 !important;
    }
    div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) [data-testid="stNumberInputStepDown"],
    div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) [data-testid="stNumberInputStepUp"] {
        position: absolute; bottom: 6px; z-index: 2; width: 28px; height: 22px;
        background: transparent !important; color: #fff !important; border: none; padding: 0;
    }
    div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) [data-testid="stNumberInputStepDown"] svg,
    div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) [data-testid="stNumberInputStepUp"] svg {
        fill: #fff !important; color: #fff !important;
    }
    div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) [data-testid="stNumberInputStepDown"] {left: 10px;}
    div[data-testid="stHorizontalBlock"]:has(> div:nth-child(5)) [data-testid="stNumberInputStepUp"] {right: 10px;}
    .under {text-align: center; margin-top: 6px; font-size: 14px;}
    .pill {
        display: inline-block; border: 1px solid #e3e3e3; border-radius: 999px;
        padding: 8px 14px; background: #fff; color: #555; font-size: 14px;
    }
    div[data-testid="stProgress"] > div {background: #e6e8ee; height: 14px; border-radius: 8px;}
    div[data-testid="stProgress"] > div > div {background: #d5deef; border-radius: 8px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.header("KANT 수료확률 계산기")
st.caption("고용24 앱을 켜고, QR출결에 나온 출석·지각·조퇴·외출·결석을 그대로 넣어 보세요.")

항목 = ["출석", "지각", "조퇴", "외출", "결석"]
칸 = st.columns(5)
숫자 = []
for 열, 이름 in zip(칸, 항목):
    with 열:
        st.markdown('<div class="circle">', unsafe_allow_html=True)
        숫자.append(st.number_input(이름, min_value=0, value=0, label_visibility="collapsed"))
        st.markdown(f'<div class="under">{이름}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
출석, 지각, 조퇴, 외출, 결석 = 숫자

전체칸, 진행칸 = st.columns(2)
전체일수 = 전체칸.number_input("전체 일수", min_value=1, value=190)
진행일수 = 진행칸.number_input("진행 일수", min_value=0, value=19)
내출석률 = 출석 / 전체일수 * 100
st.markdown(
    f'<span class="pill">나의출석률</span> &nbsp; <b>{내출석률:.1f}%</b> ({int(출석)}/{int(전체일수)}일)',
    unsafe_allow_html=True,
)
st.progress(min(내출석률 / 100, 1.0))

과정진행률 = 진행일수 / 전체일수 * 100
st.markdown(
    f'<span class="pill">과정진행률</span> &nbsp; <b>{과정진행률:.1f}%</b> ({int(진행일수)}/{int(전체일수)}일)',
    unsafe_allow_html=True,
)
st.progress(min(과정진행률 / 100, 1.0))

st.caption("공가는 쓰인 날의 출결이 무엇이었는지에 따라 나눕니다.")
결석공가칸, 조퇴공가칸 = st.columns(2)
결석공가 = 결석공가칸.number_input("결석일에 쓴 공가", min_value=0, value=0)
조퇴공가 = 조퇴공가칸.number_input("지각·조퇴·외출에 쓴 공가", min_value=0, value=0)
공가 = 결석공가 + 조퇴공가

# 결석 몇 일이 제적인지. 190일이면 38일 이상.
제적선 = int(전체일수 * 0.2)
# 공가 한도. 190일이면 19.
공가한도 = int(전체일수 * 0.1 + 0.5)
남은공가 = max(공가한도 - int(공가), 0)

# 앞으로의 속도는 공가를 빼기 전의 결석으로 센다.
원래모음 = int(지각) + int(조퇴) + int(외출)
원래환산 = int(결석) + 원래모음 // 3
# 이미 쓴 공가만 지금까지의 결석에서 뺀다.
반영결석 = max(int(결석) - int(결석공가), 0)
모을횟수 = max(원래모음 - int(조퇴공가), 0)
환산결석 = 반영결석 + 모을횟수 // 3
st.markdown(
    f'<span class="pill">총결석일</span> &nbsp; <b style="color:#222">{환산결석}일</b>',
    unsafe_allow_html=True,
)
다음까지 = 3 - (모을횟수 % 3)

# 제적선 이상이면 제적. 38이면 추가로 33번까지가 안전.
남은결석 = max(제적선 - 환산결석 - 1, 0)

# 지금 속도를 남은 날까지 잇는다. 공가 사용은 앞으로의 속도에 넣지 않는다.
if 진행일수 == 0:
    예상결석 = 환산결석
    앞으로결석 = 0
else:
    하루결석 = 원래환산 / 진행일수
    앞으로결석 = 하루결석 * (전체일수 - 진행일수)
    예상결석 = 환산결석 + 앞으로결석
# 남은 공가를 이후 결석일에만 쓸 때 내려가는 예상. 확률에는 넣지 않는다.
공가쓰면예상 = 환산결석 + max(앞으로결석 - 남은공가, 0)

# 과거 기록: 예상 결석 일수 -> 수료 / 제적
결석기록 = []
결과기록 = []
for 일수 in range(0, 제적선 + 21):
    결석기록.append([일수])
    if 일수 >= 제적선:
        결과기록.append("제적")
    else:
        결과기록.append("수료")

모델 = LogisticRegression()
모델.fit(결석기록, 결과기록)

if st.button("수료 확률 계산하기!"):
    if 진행일수 == 0:
        st.warning("과정 진행 일수를 입력해야 끝까지의 속도를 계산합니다.")
        st.stop()
    확률 = 모델.predict_proba([[예상결석]])
    수료칸 = list(모델.classes_).index("수료")
    제적칸 = list(모델.classes_).index("제적")
    수료확률 = float(확률[0][수료칸])
    제적확률 = float(확률[0][제적칸])

    왼쪽, 오른쪽 = st.columns(2)
    왼쪽.metric("수료 확률", f"{round(수료확률 * 100)}%")
    오른쪽.metric("제적 확률", f"{round(제적확률 * 100)}%")
    왼쪽, 오른쪽 = st.columns(2)
    왼쪽.metric("제적 전 더 가능한 결석", f"{남은결석}일")
    오른쪽.metric("남은 공가", f"{남은공가}회")
    st.markdown(
        f"지금 환산 결석 **{환산결석}일**. "
        f"공가 없이 이 속도면 예상 결석 **{round(예상결석, 1)}일**."
    )
    st.markdown(
        f"남은 공가 **{남은공가}회**를 이후 결석일에 쓰면 "
        f"예상 결석은 **{round(공가쓰면예상, 1)}일**까지 내려갑니다. "
        f"이 숫자는 확률에 넣지 않았습니다."
    )
    st.markdown(
        f"지각·조퇴·외출이 결석 1일이 되기까지 **{다음까지}회**. "
        f"나의출석률 **{round(내출석률, 1)}%**, 과정진행률 **{round(과정진행률, 1)}%**."
    )

    if 환산결석 >= 제적선:
        st.error("이미 전체 결석 20% 이상입니다.")
    elif 예상결석 <= 제적선 - 5 and 수료확률 >= 0.7:
        st.success("하던대로 합시다!!!  수료 가즈아!!")
    elif 수료확률 >= 0.3:
        st.warning("공가 없이 이 속도면 경계입니다. 결석을 줄여야 합니다.")
    else:
        st.error("공가 없이 이 속도면 제적 쪽입니다. 출석률 관리가 필요해요")
