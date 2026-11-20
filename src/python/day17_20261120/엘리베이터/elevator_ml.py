from itertools import combinations

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


APPROACH_COLUMNS = ["16층 이하 상행", "16층 이하 상행 시 층 차이"]


def add_approach_features(data):
    floor = data["현재층"]
    approaching = floor.le(16) & data["이동방향"].eq(1)
    floor_position = floor + floor.lt(0).astype(int)  # 지하와 지상 사이에는 0층이 없습니다.
    return data.assign(**{
        APPROACH_COLUMNS[0]: approaching.astype(int),
        APPROACH_COLUMNS[1]: (16 - floor_position).where(approaching, 0),
    })


def fun(Data, use_approach=True):
    X_Data = Data[[
        "현재층", "이동방향", "기존탑승인원(명)", "시간대(시)", "주말여부",
        "남성비율", "총몸무게(kg)", "층 표시 유지 시간(초)", "기온(°C)",
    ]]
    original_columns = X_Data.columns.tolist()
    required_columns = APPROACH_COLUMNS if use_approach else []
    if use_approach:
        X_Data = add_approach_features(X_Data)
    y = Data["대기시간(초)"]
    X_train, X_test, y_train, y_test = train_test_split(
        X_Data, y, test_size=0.2, random_state=1
    )
    베이스라인예측 = [y_train.mean()] * len(y_test)
    least = {}
    improvements = []

    for i in range(0 if required_columns else 1, len(original_columns) + 1):
        for cols in combinations(original_columns, i):
            columns = list(cols) + required_columns
            model = LinearRegression()
            model.fit(X_train[columns], y_train)
            예측시간 = model.predict(X_test[columns])
            MAE = mean_absolute_error(y_test, 예측시간)

            if not least or MAE < least["MAE"]:
                stage = {
                    "columns": columns,
                    "MAE": MAE,
                    "predictions": 예측시간,
                }
                improvements.append(stage)
                least = {"model": model, **stage}

    least["actual"] = y_test.to_numpy()
    least["baseline_predictions"] = 베이스라인예측
    least["baseline_MAE"] = mean_absolute_error(y_test, 베이스라인예측)
    least["improvements"] = improvements
    return least
