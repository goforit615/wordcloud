# -*- coding: utf-8 -*-
"""konlpy_a.ipynb


### 한글 사용:
"""

# 한글 분석 라이브러리 설치.
#!pip install konlpy

import konlpy

"""KoNLPy 패키지는 꼬꼬마, 한나눔, 트위터 (Okt), Mecab (MacOs) 분석기를 제공한다. 서로 약간의 차이점이 있으니 다음과 같이 비교해 본다.

#### 꼬꼬마 분석기:
"""

# 꼬꼬마 분석기 객체를 가져와서 분석 준비를 한다. 대문자 주의!!!
kkma = konlpy.tag.Kkma()

my_text = "한국어를 사용해 봅시다 너무 재미있어요 함께 분석해 볼까요?"

# 문장 단위로 분절.
kkma.sentences(my_text)

# 명사 추출.
kkma.nouns(my_text)

# 형태소 (분절).
print(kkma.morphs(my_text))

# 품사 태깅 (Part of Speech Tagging).
print(kkma.pos(my_text))

"""#### 한나눔 분석기:"""

# 한나눔 분석기 객체를 가져와서 분석 준비를 한다. 대문자 주의!
hannanum = konlpy.tag.Hannanum()

# 명사 추출.
hannanum.nouns(my_text)

# 형태소 (분절).
print(hannanum.morphs(my_text))

# 품사 태깅.
print(hannanum.pos(my_text))

"""#### 트위터 분석기:"""

# 트위터 분석기 객체를 가져와서 분석 준비를 한다. 대문자 주의!
okt = konlpy.tag.Okt()

# 명사 추출.
okt.nouns(my_text)

# 형태소 (분절).
print(okt.morphs(my_text))

# 품사 태깅.
print(okt.pos(my_text))



