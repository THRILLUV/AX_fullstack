from pathlib import Path

import pandas as pd
import streamlit as st

import elevator_ml as em


DATA_PATH = Path(__file__).with_name("엘리베이터.csv")
HOLD_TIME_COLUMN = "층 표시 유지 시간(초)"


@st.cache_data(max_entries=1)
def load_training_data(data_modified_at):
    return pd.read_csv(DATA_PATH)


@st.cache_resource(max_entries=2)
def load_trained_model(model_modified_at, data_modified_at, use_approach=True):
    return em.fun(load_training_data(data_modified_at), use_approach=use_approach)


st.set_page_config(
    page_title="엘리베이터 도착 대기시간 예측",
    page_icon="🛗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    [data-testid="stMainBlockContainer"] {
        width: 100%;
        max-width: none;
        padding: 0;
    }
    [data-testid="stMainBlockContainer"] > [data-testid="stVerticalBlock"] { gap: 0; }
    [data-testid="stHeader"] { background: transparent; }
    .st-key-elevator_scene {
        --door-center: 46%;
        --door-width: clamp(118px, min(54%, 65svh), 590px);
        --door-top: clamp(158px, 26svh, 234px);
        --panel-gap: clamp(8px, 2.8%, 28px);
        --panel-width: clamp(54px, 14%, 84px);
        --floor-depth: clamp(106px, 16%, 142px);
        position: relative;
        width: 100%;
    }
    .lift-wall {
        position: relative;
        min-height: 100vh;
        min-height: max(490px, 100svh);
        overflow: hidden;
        isolation: isolate;
        background:
            radial-gradient(ellipse at 45% -12%, #fff2d3d9, transparent 69%),
            repeating-linear-gradient(90deg, transparent 0 146px, #372d232e 147px 148px),
            linear-gradient(125deg, #c3b197 0%, #877768 60%, #554a3e 100%);
    }
    .lift-intro {
        position: absolute;
        top: clamp(46px, 7.5svh, 76px);
        left: clamp(18px, 6vw, 84px);
        color: #2c241d;
    }
    .lift-intro h1 {
        margin: 0;
        padding: 0;
        color: inherit;
        font-size: clamp(22px, 4.3vw, 46px);
        line-height: 1.2;
        letter-spacing: -.045em;
    }
    .lift-intro p {
        margin: 7px 0 0;
        color: #352b21;
        font-size: clamp(12px, 1.4vw, 15px);
    }
    .lift-floor {
        position: absolute;
        inset: auto 0 0;
        height: var(--floor-depth);
        border-top: 2px solid #4b443b;
        background: repeating-linear-gradient(90deg, transparent 0 94px, #29272566 95px 96px),
                    repeating-linear-gradient(0deg, transparent 0 41px, #29272538 42px 43px),
                    linear-gradient(#433c34, #716354);
    }
    .lift-indicator {
        position: absolute;
        bottom: calc(100% - var(--door-top) + 13px);
        left: var(--door-center);
        transform: translateX(-50%);
        display: flex;
        align-items: center;
        gap: .65rem;
        padding: .34rem .72rem;
        border: 2px solid #6b6355;
        border-radius: 6px;
        background: #181b18;
        color: #ffd27f;
        font: 700 clamp(17px, 3.5vw, 25px) ui-monospace, monospace;
        text-shadow: 0 0 12px #ffa9318c;
        box-shadow: inset 0 1px 4px #000, 0 3px 9px #30281f65;
    }
    .lift-indicator-arrow { font-size: .72em; }
    .lift-frame {
        position: absolute;
        top: var(--door-top);
        bottom: var(--floor-depth);
        left: calc(var(--door-center) - var(--door-width) / 2);
        width: var(--door-width);
        padding: clamp(6px, 1.5vw, 12px) clamp(6px, 1.5vw, 12px) 4px;
        border: 1px solid #797a75;
        border-radius: 4px 4px 0 0;
        background: linear-gradient(95deg, #727674, #e0ded5 5%, #b7b9b4 40%, #cfd1cc 94%, #777b7b);
        box-shadow: 0 8px 22px #2d2722a6, inset 0 1px 1px #fffcf0c9;
    }
    .lift-doors {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 2px;
        height: 100%;
        border: 1px solid #474948;
        box-shadow: 0 0 0 1px #474948;
        background: #3a3d3d;
    }
    .lift-door {
        background:
            repeating-linear-gradient(0deg, #fff2 0 1px, transparent 1px 3px),
            linear-gradient(100deg, #838a8c, #ccd1d0 30%, #b6bebf 58%, #8a9294);
        box-shadow: inset 0 6px 12px #1b1d1c4d;
    }
    .lift-door + .lift-door {
        background:
            repeating-linear-gradient(0deg, #fff2 0 1px, transparent 1px 3px),
            linear-gradient(80deg, #8a9294, #bcc3c3 24%, #d1d3ce 67%, #909694);
    }
    .st-key-elevator_call_panel {
        position: absolute;
        z-index: 2;
        top: 49%;
        left: calc(var(--door-center) + var(--door-width) / 2 + var(--panel-gap));
        width: var(--panel-width) !important;
        transform: translateY(-50%);
        align-items: center;
        gap: 6px;
        padding: 8px 4px;
        border: 1px solid #8a8981;
        border-radius: 6px;
        background: linear-gradient(105deg, #a7aaa6, #e1e0d7 46%, #b7bab5);
        box-shadow: 2px 5px 12px #30282075, inset 0 1px 0 #fffc;
    }
    .lift-panel-floor, .lift-call-status {
        width: 100%;
        color: #30352e;
        text-align: center;
        font: 700 11px ui-monospace, monospace;
    }
    .lift-call-status { font: 700 10px sans-serif; }
    .st-key-elevator_call_panel > [data-testid="stElementContainer"]:has(.lift-panel-floor, .lift-call-status) {
        min-height: 14px;
    }
    .st-key-elevator_call_panel [data-testid="stButton"] { display: grid; place-items: center; }
    .st-key-elevator_call_panel [data-testid="stButton"] button {
        width: clamp(44px, 8vw, 54px);
        min-width: 44px;
        height: clamp(44px, 8vw, 54px);
        padding: 0;
        border: 2px solid #6c736d;
        border-radius: 50%;
        color: #eff6ee;
        background: radial-gradient(circle at 42% 22%, #616d65, #252e29 75%);
        box-shadow: 0 2px 3px #30332f73, inset 0 1px 2px #a7b0a7;
        transition: box-shadow .15s ease, transform .1s ease;
    }
    .st-key-elevator_call_panel [data-testid="stButton"] button p { font-size: 19px; line-height: 1; }
    .st-key-elevator_call_panel [data-testid="stButton"] button:hover,
    .st-key-elevator_call_panel:has(.lift-called) [data-testid="stButton"] button {
        border-color: #8a5408;
        color: #ffe6ab;
        background: radial-gradient(circle at 44% 22%, #504023, #252312 77%);
        box-shadow: 0 0 0 2px #ffbe4e, 0 0 13px #f57f1e9c, inset 0 1px 2px #ffd98a69;
    }
    .st-key-elevator_call_panel [data-testid="stButton"] button:focus-visible {
        outline: 2px solid #322516;
        outline-offset: 4px;
    }
    .st-key-elevator_call_panel [data-testid="stButton"] button:active { transform: translateY(2px); }
    .st-key-elevator_result {
        position: absolute;
        z-index: 2;
        bottom: max(46px, calc(env(safe-area-inset-bottom) + 41px));
        left: 50%;
        width: min(340px, calc(100% - 32px)) !important;
        transform: translateX(-50%);
    }
    .lift-wait-result {
        display: flex;
        flex-wrap: wrap;
        gap: .15rem .8rem;
        align-items: baseline;
        justify-content: center;
        padding: .58rem 1rem;
        color: #fff0d2;
        background: #211d17;
        border: 1px solid #9d7d53;
        border-radius: 8px;
        box-shadow: 0 4px 16px #18151073;
        font-size: 13px;
        text-align: center;
    }
    .lift-wait-result strong { color: #ffd18a; font-size: 24px; line-height: 1.15; }
    .lift-wait-result small { flex-basis: 100%; color: #e0cdae; font-size: 11px; }
    .lift-details-link {
        position: absolute;
        z-index: 2;
        bottom: max(12px, calc(env(safe-area-inset-bottom) + 7px));
        left: 50%;
        transform: translateX(-50%);
        color: #fff0d2 !important;
        font-size: 13px;
        text-decoration: none !important;
    }
    .lift-details-link:hover, .lift-details-link:focus-visible { text-decoration: underline !important; }
    .st-key-elevator_model_details {
        width: min(860px, calc(100% - 32px)) !important;
        margin: 24px auto 32px;
    }
    @media (max-width: 500px) {
        .st-key-elevator_scene { --door-center: 43%; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if not DATA_PATH.is_file():
    st.error("앱과 같은 폴더에 `엘리베이터.csv`를 넣어주세요.")
    st.stop()

data_modified_at = DATA_PATH.stat().st_mtime_ns
model_modified_at = Path(em.__file__).stat().st_mtime_ns
data = load_training_data(data_modified_at)
floors = sorted(int(floor) for floor in data["현재층"].dropna().unique() if floor != 0)

with st.sidebar:
    st.header("예측 조건")
    st.caption("16층 호출을 기준으로 엘리베이터의 현재 상태를 입력하세요.")
    current_floor = st.selectbox(
        "엘리베이터 현재 층",
        floors,
        index=floors.index(16) if 16 in floors else 0,
        format_func=lambda floor: f"지하 {abs(floor)}층" if floor < 0 else f"{floor}층",
    )
    direction_label = st.selectbox("엘리베이터 이동 방향", ["상행", "하행"])
    passenger_count = st.slider("기존 탑승 인원", 1, 15, 7)
    hold_time = st.slider(
        HOLD_TIME_COLUMN,
        min_value=int(data[HOLD_TIME_COLUMN].min()),
        max_value=int(data[HOLD_TIME_COLUMN].max()),
        value=int(data[HOLD_TIME_COLUMN].median()),
        help="데모에서는 기존 호출 수를 이 항목의 값으로 사용합니다.",
    )
    hour = st.slider("시간대", 6, 22, 14, format="%d시")
    is_weekend = st.checkbox("주말")
    male_ratio = st.slider("탑승객 중 남성 비율", 0.0, 1.0, 0.5, 0.05)
    total_weight = st.number_input(
        "총 탑승 무게 (kg)", min_value=50, max_value=1281, value=544, step=10
    )
    temperature = st.slider("기온 (°C)", -9.3, 34.0, 13.1, 0.1)

input_signature = (
    current_floor,
    direction_label,
    passenger_count,
    hold_time,
    hour,
    is_weekend,
    male_ratio,
    total_weight,
    temperature,
    data_modified_at,
    model_modified_at,
)

floor_display = f"B{abs(current_floor)}" if current_floor < 0 else f"{current_floor}F"
direction_arrow = "▲" if direction_label == "상행" else "▼"

with st.container(key="elevator_scene", gap=None):
    st.markdown(
        f"""
        <div class="lift-wall">
          <div class="lift-intro">
            <h1>16층 엘리베이터</h1>
            <p>사이드바에서 조건을 고르고 문 옆 ▲를 눌러주세요.</p>
          </div>
          <div class="lift-indicator" aria-label="엘리베이터 현재 층 {floor_display}, {direction_label}">
            <span>{floor_display}</span>
            <span class="lift-indicator-arrow">{direction_arrow}</span>
          </div>
          <div class="lift-frame" aria-hidden="true">
            <div class="lift-doors">
              <div class="lift-door"></div>
              <div class="lift-door"></div>
            </div>
          </div>
          <div class="lift-floor" aria-hidden="true"></div>
          <a class="lift-details-link" href="#model-details">모델 검증 결과 ↓</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container(key="elevator_call_panel", gap=None):
        st.markdown('<div class="lift-panel-floor">16F</div>', unsafe_allow_html=True)
        predict_clicked = st.button("▲", key="elevator_call", help="16층에서 상행 호출")
        call_active = predict_clicked or st.session_state.get("elevator_prediction_signature") == input_signature
        status_class = "lift-call-status lift-called" if call_active else "lift-call-status"
        status_text = "호출됨" if call_active else "상행 호출"
        st.markdown(f'<div class="{status_class}">{status_text}</div>', unsafe_allow_html=True)

    with st.container(key="elevator_result", gap=None):
        call_feedback = st.empty()

if predict_clicked:
    input_row = pd.DataFrame(
        [{
            "현재층": current_floor,
            "이동방향": 1 if direction_label == "상행" else 0,
            "기존탑승인원(명)": passenger_count,
            HOLD_TIME_COLUMN: hold_time,
            "시간대(시)": hour,
            "주말여부": int(is_weekend),
            "남성비율": male_ratio,
            "총몸무게(kg)": total_weight,
            "기온(°C)": temperature,
        }]
    )
    call_feedback.markdown(
        '<div class="lift-wait-result" role="status">대기시간을 계산하고 있습니다...</div>',
        unsafe_allow_html=True,
    )
    input_row = em.add_approach_features(input_row)
    trained_result = load_trained_model(model_modified_at, data_modified_at)
    model = trained_result["model"]
    best_columns = trained_result["columns"]
    predicted_seconds = max(0, float(model.predict(input_row[best_columns])[0]))
    st.session_state["elevator_prediction_result"] = round(predicted_seconds)
    st.session_state["elevator_prediction_mae"] = trained_result["MAE"]
    st.session_state["elevator_prediction_signature"] = input_signature

if st.session_state.get("elevator_prediction_signature") == input_signature:
    wait_seconds = st.session_state["elevator_prediction_result"]
    validation_mae = st.session_state["elevator_prediction_mae"]
    call_feedback.markdown(
        f"""
        <div class="lift-wait-result" role="status">
          <span>예상 도착 시간</span><strong>약 {wait_seconds}초</strong>
          <small>검증 MAE {validation_mae:.1f}초</small>
        </div>
        """,
        unsafe_allow_html=True,
    )
elif "elevator_prediction_result" in st.session_state:
    call_feedback.markdown(
        '<div class="lift-wait-result" role="status">조건이 바뀌었어요. ▲를 다시 눌러주세요.</div>',
        unsafe_allow_html=True,
    )

with st.container(key="elevator_model_details", gap=None):
    st.markdown('<div id="model-details"></div>', unsafe_allow_html=True)
    comparison = st.expander(
        "모델 검증 결과 · 베이스라인",
        expanded=False,
        key="elevator_model_validation",
        on_change="rerun",
    )
    if comparison.open:
        with comparison:
            chart_view = st.selectbox(
                "볼 차트",
                ("최종 실험 모델", "개선 전 기존 모델", "학습 중간 단계"),
            )
            with st.spinner("검증 결과를 준비하고 있습니다..."):
                if chart_view == "개선 전 기존 모델":
                    result = load_trained_model(model_modified_at, data_modified_at, use_approach=False)
                else:
                    result = load_trained_model(model_modified_at, data_modified_at)

            chart_model = result
            if chart_view == "학습 중간 단계":
                stages = result["improvements"]
                step = st.selectbox(
                    "학습 단계",
                    range(len(stages)),
                    format_func=lambda i: f"{i + 1}단계 · MAE {stages[i]['MAE']:.2f}초",
                    help="컬럼 조합을 비교하다가 가장 낮은 MAE가 갱신된 단계만 표시합니다.",
                )
                chart_model = stages[step]

            st.caption(f"선택된 입력 변수 · {', '.join(chart_model['columns'])}")
            st.caption(f"예측 MAE {chart_model['MAE']:.2f}초 · 베이스라인 MAE {result['baseline_MAE']:.2f}초")
            st.line_chart(
                pd.DataFrame({
                    "실제 대기시간": result["actual"],
                    "모델 예측": chart_model["predictions"],
                    "베이스라인 MAE": result["baseline_MAE"],
                    "예측 MAE": chart_model["MAE"],
                }),
                x_label="검증 샘플 순서",
                y_label="대기시간(초)",
                height=260,
            )
