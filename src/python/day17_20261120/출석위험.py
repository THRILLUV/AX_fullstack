# 칸트 출석 제적 위험
# 규정으로 남은 일수를 계산하고,
# 지금 결석 속도가 끝까지 이어질 때의 제적 확률은 로지스틱으로 본다.

import streamlit as st
from sklearn.linear_model import LogisticRegression

전체기본 = 190
제적비율 = 0.2
공가비율 = 0.1

def 반올림(값):
    return int(값 + 0.5)

제적일수 = 반올림(전체기본 * 제적비율)
학습결석 = list(range(0, 제적일수 + 20))
학습결과 = ["제적" if 일수 >= 제적일수 else "수료" for 일수 in 학습결석]

모델 = LogisticRegression()
모델.fit([[일수] for 일수 in 학습결석], 학습결과)
제적칸 = list(모델.classes_).index("제적")

st.set_page_config(page_title="칸트 출석 제적 위험", page_icon="📋")
st.title("칸트 출석 제적 위험")
st.write("고용24에 나온 출결을 넣으면, 이 속도가 끝까지 이어질 때 제적 쪽인지 보여 줍니다.")

전체 = st.number_input("전체 훈련일수", min_value=1, value=전체기본, step=1)
진행 = st.number_input("과정 진행 일수", min_value=1, value=19, step=1)
출석 = st.number_input("출석 일수", min_value=0, value=15, step=1)
결석 = st.number_input("결석 일수", min_value=0, value=4, step=1)
지각 = st.number_input("지각 횟수", min_value=0, value=0, step=1)
조퇴 = st.number_input("조퇴 횟수", min_value=0, value=0, step=1)
외출 = st.number_input("외출 횟수", min_value=0, value=0, step=1)
공가 = st.number_input("사용한 공가 일수", min_value=0, value=0, step=1)
이번달수업 = st.number_input("이번 달 수업 일수 (모르면 0)", min_value=0, value=0, step=1)
이번달출석 = st.number_input("이번 달 출석 일수", min_value=0, value=0, step=1)

if st.button("계산하기"):
    조각 = int(지각 + 조퇴 + 외출)
    환산결석 = int(결석) + 조각 // 3
    남은조각 = 조각 % 3
    제적선 = 반올림(int(전체) * 제적비율)
    공가한도 = 반올림(int(전체) * 공가비율)
    남은결석 = 제적선 - 환산결석
    남은공가 = 공가한도 - int(공가)

    남은일 = int(전체) - int(진행)
    if int(진행) > 0:
        예상추가 = 환산결석 / int(진행) * 남은일
    else:
        예상추가 = 0
    예상결석 = 환산결석 + 예상추가

    결과 = 모델.predict([[예상결석]])
    확률 = 모델.predict_proba([[예상결석]])
    제적확률 = float(확률[0][제적칸])

    안빠지면 = int(출석) + 남은일
    최종출석률 = 안빠지면 / int(전체) * 100

    st.subheader("이 속도가 계속되면")
    st.metric("제적 확률", f"{round(제적확률 * 100)}%")
    st.metric("수료 확률", f"{round((1 - 제적확률) * 100)}%")
    st.write(f"예상 최종 결석: {예상결석:.1f}일 (제적 기준 {제적선}일 이상)")

    if 결과[0] == "제적":
        st.error("이 속도라면 과정 끝까지 갔을 때 제적 쪽입니다.")
    else:
        st.success("이 속도라면 결석 20% 제적선 안에 있습니다.")

    st.subheader("지금 규정으로 남은 여유")
    st.write(f"환산 결석: {환산결석}일 (결석 {int(결석)}일 + 지각·조퇴·외출 {조각}회 중 {조각 // 3}일)")
    st.write(f"제적까지 남은 결석: {남은결석}일. {제적선}일이 되는 순간 제적입니다.")
    st.write(f"지각·조퇴·외출은 앞으로 {3 - 남은조각}번이면 결석 1일이 됩니다.")
    st.write(f"공가 한도 {공가한도}일 중 {int(공가)}일 사용, 남은 공가 {남은공가}일")
    st.write(f"앞으로 한 번도 안 빠지면 출석률 {최종출석률:.1f}% ({안빠지면}/{int(전체)}일)")

    if int(이번달수업) > 0:
        이번달률 = int(이번달출석) / int(이번달수업) * 100
        st.write(f"이번 달 출석률 {이번달률:.1f}%")
        if int(이번달출석) / int(이번달수업) <= 0.5:
            st.error("이번 달 출석이 50% 이하입니다. 단위기간 제적 기준입니다.")
        else:
            필요출석 = 반올림(int(이번달수업) * 0.5) + 1
            st.write(f"이번 달 50%를 넘기려면 출석이 {필요출석}일보다 많아야 합니다.")

    st.caption("제적 확률은 예상 결석 일수를 로지스틱에 넣은 값입니다. 남은 일수와 3번에 1일은 규정 계산입니다.")
