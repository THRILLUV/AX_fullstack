# train.py


# 학습용/시험용 데이터 나누기
# 데이터를 두가지로 묶는다.
# 학습용 데이터 (train Data)
# -모델이 공부하는 데이터! (연습문제)
# 시험용 데이터 (test data)
# - 모델이 처음 보는 데이터 (시험문제)

# 모델을 공정하게 비교하려고

# 실행순서
# 1. 전체 데이터를 준비한다.
# 2. 학습용/ 시험용으로 나눈다.
# 3. 학습용 데이터로만 모델을 공부시킨다.
# 4. 시험용 데이터로 예측하고 MSE를 계산한다.
# 5. 점수를 보고 모델을 평가, 선택한다.


# 데이터를 나누려면 도구가 필요하다!
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. 전체데이터
공부시간 = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]   # X: 문제 (대괄호 안에 대괄호 형태)
점수 = [12, 22, 29, 43, 48, 62, 68, 83, 88, 97]                  # y: 정답

# 2. 나누기
#   나누는 기준이 학습 80% 시험용 20%
X_train,X_test, y_train,y_test = train_test_split(공부시간
                                                  ,점수
                                                  ,test_size=0.2
                                                  ,random_state=1)

# 3. 잘 나눠어졌는지 확인
print("총 데이터: ", len(공부시간))
print("공부용 개수: ",len(X_train), "시험용 개수: ",len(X_test))
print("공부용 개수: ",len(y_train), "시험용 개수: ",len(y_test))

# 4. 모델가져오기
#  학습을 해서 숫자로 결과를 보여주는 모델!
model = LinearRegression()

# 5. 학습
model.fit(X_train,y_train)

# 6. 예측
# 공부용 , 시험용 결과를 낸다.
공부용학습예측 = model.predict(X_train)
시험용학습예측 = model.predict(X_test)

# 채점
print("공부용 MSE: ",mean_squared_error(y_train,공부용학습예측))
print("시험용 MSE: ",mean_squared_error(y_test,시험용학습예측))