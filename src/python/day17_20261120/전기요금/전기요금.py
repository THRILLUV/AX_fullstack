
import pandas as pd
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# [과제2 효과] 브라우저 탭 제목과 아이콘 바꾸기
st.set_page_config(page_title="AI 전기요금 예측기", page_icon="⚡")

st.title("⚡ AI 우리 집 전기요금 예측기")
st.write("가전제품을 선택하고 사용량을 입력하면 한 달 전기요금을 예측해 드립니다.")

# 1. 데이터 불러오기
data = pd.read_csv("Day16_20261119/전기 사용량.csv")

# 2. X, Y 구분
가전목록 = [
    "에어컨", "냉장고", "세탁기", "건조기", "tv",
    "컴퓨터", "전자레인지", "전기밥솥",
    "공기청정기", "전기히터"
]

X = data[가전목록]
Y = data["한달사용요금"]

# 3. 학습용 / 테스트용 데이터 분리
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# 4. 머신러닝 학습
model = LinearRegression()
model.fit(X_train, Y_train)

# 5. 테스트 데이터로 오차 계산
테스트예측 = model.predict(X_test)

mae = mean_absolute_error(Y_test, 테스트예측)
mse = mean_squared_error(Y_test, 테스트예측)

# 기준선(베이스라인)
# 전체 한달사용요금의 평균 하나를 테스트 개수만큼 복사해서 직선으로 만든다.
평균 = Y.mean()
기준선 = [평균] * len(Y_test)

# 실제요금을 리스트에 하나씩 담고, 가장 크게 틀린 값 찾기
실제요금들 = []
최대오차 = 0

for 실제, 예측값 in zip(Y_test, 테스트예측):
    실제요금들.append(실제)
    틀린크기 = abs(실제 - 예측값)
    if 틀린크기 > 최대오차:
        최대오차 = 틀린크기

# 6. 가전제품별 입력 단위
단위 = {
    "에어컨": "하루 평균 사용시간 (시간)",
    "냉장고": "보유 대수 (대)",
    "세탁기": "일주일 사용 횟수 (회)",
    "건조기": "일주일 사용 횟수 (회)",
    "tv": "하루 평균 사용시간 (시간)",
    "컴퓨터": "하루 평균 사용시간 (시간)",
    "전자레인지": "하루 평균 사용시간 (분)",
    "전기밥솥": "하루 평균 보온시간 (시간)",
    "공기청정기": "하루 평균 사용시간 (시간)",
    "전기히터": "하루 평균 사용시간 (시간)"
}

st.divider()

# 7. 가전제품 선택
st.subheader("🏠 우리 집 가전제품 선택")
st.write("보유한 가전제품의 버튼을 켜주세요.")

입력값 = {}

# 모든 가전제품을 0으로 먼저 저장 (토글을 안 켠 가전은 0)
for 가전 in 가전목록:
    입력값[가전] = 0

# 2열로 배치
칸1, 칸2 = st.columns(2)

for 번호, 가전 in enumerate(가전목록):

    # 짝수 번호는 왼쪽, 홀수 번호는 오른쪽
    if 번호 % 2 == 0:
        위치 = 칸1
    else:
        위치 = 칸2

    # [과제2 효과] 켜고 끄는 토글 버튼
    선택 = 위치.toggle(
        가전,
        key=f"선택_{가전}"
    )

    # 토글을 켠 가전제품만 입력창 표시
    if 선택:

        if 가전 in ["냉장고", "세탁기", "건조기"]:
            최대값 = 100.0
        elif 가전 == "전자레인지":
            최대값 = 1440.0
        else:
            최대값 = 24.0

        # [과제2 효과] key로 입력창마다 이름표 붙이기
        입력값[가전] = 위치.number_input(
            f"{가전} - {단위[가전]}",
            min_value=0.0,
            max_value=최대값,
            value=1.0,
            step=1.0,
            key=f"입력_{가전}"
        )

st.divider()

# 8. 예측 버튼
# [과제2 효과] type="primary" 강조 버튼
if st.button("⚡ 한 달 전기요금 예측하기", type="primary"):

    # 학습 때와 똑같은 열 이름으로 표를 만든다
    새데이터 = {}
    for 가전 in 가전목록:
        새데이터[가전] = [입력값[가전]]

    예상요금 = model.predict(pd.DataFrame(새데이터))[0]

    # 음수 요금 방지
    if 예상요금 < 0:
        예상요금 = 0

    # 평균 오차(MAE) 기준 참고 범위
    최소요금 = 예상요금 - mae
    if 최소요금 < 0:
        최소요금 = 0
    최대요금 = 예상요금 + mae

    st.success("AI 전기요금 예측 완료!")

    st.subheader("📊 예측 결과")

    st.metric("예상 한 달 전기요금", f"{예상요금:,.0f}원")

    st.write(f"📌 평균 오차(MAE) 기준 참고 범위: {최소요금:,.0f}원 ~ {최대요금:,.0f}원")

    st.info(
        "이 범위는 테스트 데이터의 평균 오차를 "
        "더하고 뺀 참고값이며, 실제 요금이 "
        "반드시 이 안에 들어온다는 뜻은 아닙니다."
    )

    # 9. 머신러닝 테스트 결과
    st.subheader("🧪 머신러닝 테스트 결과")

    결과1, 결과2, 결과3 = st.columns(3)

    결과1.metric("MAE", f"{mae:,.0f}원")
    결과2.metric("MSE", f"{mse:,.0f}")
    결과3.metric("최대 절대오차", f"{최대오차:,.0f}원")

    # 10. 실제값과 예측값 비교
    st.subheader("📈 실제 요금과 AI 예측 요금 비교")

    비교데이터 = pd.DataFrame({
        "실제요금": 실제요금들,
        "예측요금": 테스트예측,
        "기준선(평균)": 기준선
    })

    st.line_chart(비교데이터)

    st.write(f"기준선: {평균:,.0f} 원")

    상세보기 = st.expander("테스트 데이터 상세 보기")
    상세보기.dataframe(비교데이터)

# 11. 회귀계수 분석
분석창 = st.expander("🔍 가전제품별 회귀계수 확인")

가전이름들 = []
계수들 = []

for 이름, w in zip(X, model.coef_):
    가전이름들.append(이름)
    계수들.append(round(w, 2))

계수데이터 = pd.DataFrame({
    "가전제품": 가전이름들,
    "회귀계수": 계수들
})

분석창.dataframe(계수데이터)

분석창.write(
    "회귀계수는 다른 조건이 같을 때 "
    "입력값이 1 증가하면 예상 요금이 "
    "얼마나 변하는지 나타냅니다."
)

st.caption("※ 실습용 합성 데이터에 기반한 예측이며 실제 청구요금과 다를 수 있습니다.")
