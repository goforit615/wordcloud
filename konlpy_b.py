# -*- coding: utf-8 -*-
"""konlpy_b.ipynb


### 한글 분석기 비교.

#### 1. 형태소 분석기 (복습).

트위터 형태소 분석기 사용.
"""

# 한글 분석 라이브러리 설치.
# !pip install konlpy
import os

from konlpy.tag import Okt
okt=Okt()
print(okt.morphs("광주소마고와 함께 코딩을 배워 보아요", stem=True))   # 어간추출 적용한 토큰화.

print(okt.nouns("광주소마고와 함께 코딩을 배워 보아요"))

print(okt.pos("광주소마고와 함께 코딩을 배워 보아요", stem=True))  # 어간추출 적용한 형태소 분석.

