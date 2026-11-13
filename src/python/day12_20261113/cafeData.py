# cafeDate.PAYMENT_PRICE
# 1. 도구
#   카페 매출을 분석하고 예측(머신러닝)하는 프로그램

import pandas as pd
import streamlit as st

# 상황
#   ㄴ 어떤 상품군에서 매출이 마낳이 나왔는지 보여주세요!
# 기록된 매출과 반품은 얼마인가?


# 2. 파일 읽어오기
try:
    원본데이터 = pd.read_csv("CAFE_DATA.csv")

# 구조확인
# 행과 열 수 확인
# 위에서 3개만확인 하는거

    print("전체 행과 열 : ", 원본데이터.shape)
# print(원본데이터.info())
    print(원본데이터.isna().sum())
    print(원본데이터.head(3))


# 구조확인

# 전체 행과 열 :  (49, 20)
# ADDR_DC            0
# TRDAR_NM           0
# RCIPT_NO           0
# SALES_CD           0
# ORDER_TY           0
# ORDER_CN           0
# SALES_DE           0
# SALES_TIME         0
# SALES_WKDAY_CD     0
# RESVE_DT          29
# LCLAS_CD           0
# MLSFC_CD           0
# SCLAS_CD           0
# SLE_CO             0
# SETLE_PRICE        0
# DSCNT_PRICE        0
# PAYMENT_PRICE      0
# DSCNT_NM           0
# DSCNT_RT          24
# SETLE_MTH_CN       0
# dtype: int64


except FileNotFoundError:
    print("파일이 없으요")