# -*- coding: utf-8 -*-
"""word_cloud_en.ipynb

### 워드클라우드 (영문)

#### 필요한 패키지 불러오기:
"""
# 영어 분석 라이브러리 설치.
#!pip install nltk

# Commented out IPython magic to ensure Python compatibility.
from wordcloud import WordCloud
import numpy as np
import pandas as pd
import nltk                                   # Natural Language Tool Kit (영어).
import re
import matplotlib.pyplot as plt
from PIL import Image                         # Pillow 패키지의 이미지 핸들링 모듈.
from nltk.corpus import stopwords             # 불용어.
# %matplotlib inline

# 다음을 한번 실행한다!
nltk.download('punkt')
nltk.download('stopwords')

"""#### 데이터 읽어오기:"""

f= open("data/book_crime_and_punishment.txt",'r',encoding='UTF-8')
#f = open("../data/book_three_little_pigs.txt",'r',encoding='UTF-8')
my_book = f.readlines()
f.close()

"""#### 전처리:"""

n_min = 4                                                           # 최소 단어 길이.
corpus = []
for a_line in my_book:
    pre = re.sub('\W', ' ', a_line)                                # 특수문자 제외.
    pre = re.sub('_', ' ', pre)                                    # 특수문자 제외.
    pre = re.sub('\d+','', pre)                                    # 수자 제외.
    pre = nltk.word_tokenize(pre)                                   # 단어 단위로 분절.
    pre = [x for x in pre if len(x) > n_min]                        # 최소 길이 충족.
    pre = [x.lower() for x in pre]                                  # 소문자화.  정규화 (Normalization).
    pre = [x for x in pre if x not in stopwords.words('english')+['could']]   # 불용어 처리.
    corpus += pre                                                   # 단어를 말뭉치에 추가.

"""#### 키워드 추출 (Option):"""

# Series 로 변환.
my_series = pd.Series(corpus)

# Top 10 확인.
my_word_counts = my_series.value_counts().sort_values(ascending=False)
my_word_counts[:10]

# 딕셔너리로 변환해 둔다.
my_dict = dict(my_word_counts)

"""#### 워드 클라우드 기본형 생성:"""

# 다음은 워드클라우드의 요구사항.
a_long_sentence = ' '.join(corpus)

wc = WordCloud(background_color='white', max_words=30)              # 바탕색, 단어 개수 등 설정.
wc.generate(a_long_sentence)
#wc.generate_from_frequencies(my_dict)                              # 딕셔너리에서 생성.
#wc.words_                                                          # 단어 사전 출력.

plt.figure(figsize=(10,10))
plt.imshow(wc)
plt.axis("off")                                    # 축을 꺼줌.
plt.show()


"""#### 워드 클라우드 마스크 사용형 생성:"""

# 백그라운드 마스크
img = Image.open('images/background_1.png')                    # 타원형.
# img = Image.open('../data/background_2.png')                   # 말풍선.
# img = Image.open('../data/background_3.png')                    # 하트.
# img = Image.open('../data/male-face-silhouette-15.png')
# plt.imshow(img)
# plt.show()
back_mask = np.array(img)

wc = WordCloud(background_color='white', max_words=30, mask=back_mask,  contour_width=1, contour_color='orange')            # 바탕색, 단어 개수 등 설정.
wc.generate(a_long_sentence);                                                      # 긴 문자열에서 생성.
#wc.generate_from_frequencies(my_dict);                                            # 딕셔너리에서 생성.

plt.figure(figsize=(10,10))
plt.imshow(wc)
plt.axis("off")                                    # 축을 꺼줌.
plt.show()
