# -*- coding: utf-8 -*-
"""word_cloud_kr.ipynb

### 워드클라우드 (국문)

#### 필요한 패키지 불러오기:
"""

# 한글 분석 라이브러리 설치.
#!pip install konlpy

# 한글 (나눔) 글꼴 설치 (시각화를 위해서).
#!sudo apt-get install -y fonts-nanum
#!sudo fc-cache -fv
#!rm ~/.cache/matplitlib -rf

# Commented out IPython magic to ensure Python compatibility.
from wordcloud import WordCloud
import konlpy
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from PIL import Image                         # Pillow 패키지의 영상 핸들링 클래스.
# %matplotlib inline
plt.rc('font', family='NanumBarunGothic')

"""#### 데이터 읽어오기:"""


#f = open("data/example_seoul_government.txt",'r',encoding="cp949")  # Encoding 주의!!!
f = open("data/대한민국헌법.txt",'r',encoding="utf-8")  # Encoding 주의!!!

my_text = f.readlines()
f.close()

# 몇개만 출력해 본다.
my_text[:10]

"""#### 전처리:"""

no_meaning = "관련|요청|개선|건의|시장|민원|이용"
no_meaning += "|관리|문제|불편|설치|불법|제안|필요"
no_meaning += "|정책|언제|대책|서울시|서울|박원순|요망|부탁|주세요|의|대한"

my_text_clean = []
for a_line in my_text:
    a_line = re.sub('\W+',' ', a_line)           # 특수 문자 스페이스로 대체.
    a_line = re.sub('\d+',' ', a_line)           # 수치 스페이스로 대체.
    a_line = re.sub('[a-zA-Z]',' ',a_line)       # 영문 스페이스로 대체.
    a_line = re.sub('ㅠ|ㅋ|ㅎ', ' ', a_line)     # 단모음, 단자음 스페이스로 대체.
    a_line = re.sub(no_meaning, ' ', a_line)     # 특별한 의미 없는 단어 스페이스로 대체.
    a_line = re.sub('\s+', ' ', a_line)          # 잉여 스페이즈 줄임.
#    my_text_clean += [a_line]
    my_text_clean.append(a_line)

# 몇개만 출력해 본다.
my_text_clean[:10]

"""#### 한글 단어(명사) 추출:"""

my_tagger = konlpy.tag.Okt() 

# 명사 추출.
my_words = []
for a_line in my_text_clean:
    my_words.extend( my_tagger.nouns(a_line) )
#    my_words.extend( my_tagger.morphs(a_line, stem=True) )  # 모든 형태소 사용하는 경우.

# 단음절 제거.
my_words_2 = []
for a_word in my_words:
    if len(a_word) > 1:
        my_words_2 += [a_word]

# 단음절 제거.
# List comprehension 방법 사용.
# my_words_2 = [a_word  for a_word in my_words if len(a_word) > 1]

"""#### 키워드 추출 (Option):"""

# Series 로 변환.
my_series = pd.Series(my_words_2)

# 도수 분포표. Top 20
my_word_counts = my_series.value_counts().sort_values(ascending=False)
my_word_counts[:20]

# 딕셔너리로 변환해 둔다.
my_dict = dict(my_word_counts)

"""#### 워드 클라우드 기본형 생성:"""

# 다음은 워드클라우드의 요구사항.
a_long_sentence = ' '.join(my_words_2)

wc = WordCloud(font_path='fonts/NanumGothic.ttf', #'/usr/share/fonts/truetype/nanum/NanumBarunGothic',
               background_color='white',
               max_words=30)              # 바탕색, 단어 개수 등 설정.
wc.generate(a_long_sentence)
#wc.generate_from_frequencies(my_dict)
# wc.words_

plt.figure(figsize=(10,10))
plt.imshow(wc)
plt.axis("off")                                    # 축을 꺼줌.
plt.show()

"""#### 워드 클라우드 마스크 사용형 생성:"""

# 백그라운드 마스크
# img = Image.open('../data/background_1.png')                    # 타원형.
#img = Image.open('../data/background_2.png')                   # 말풍선.
img = Image.open('data/background_3.png')                    # 하트.
back_mask = np.array(img)

wc = WordCloud(font_path='fonts/NanumGothic.ttf', #'/usr/share/fonts/truetype/nanum/NanumBarunGothic',
               background_color='white',
               max_words=100,
               mask=back_mask,
               contour_width=1,
               contour_color='orange')            # 바탕색, 단어 개수 등 설정.
wc.generate(a_long_sentence)

plt.figure(figsize=(10,10))
plt.imshow(wc)
plt.axis("off")                                    # 축을 꺼줌.
plt.show()

