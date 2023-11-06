# wordcloud

## 설치

pip를 사용하는 경우:

     pip install wordcloud

Conda를 사용하는 경우 `conda-forge` 채널에서 설치할 수 있습니다.

     conda install -c conda-forge wordcloud

#### 설치 참고 사항

wordcloud는 `numpy`, `pillow` 및 `matplotlib`에 의존합니다.

#### 윈도우
1. Java 1.7+이 설치되어 있나요?
2. [JAVA_HOME](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/index.html) 설정하기
3. [JPype1 (>=0.5.7)을 다운로드](http://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype) 받고 설치. 다운 받은 .whl 파일을 설치하기 위해서는 pip 을 업그레이드 해야할 수 있습니다.
```
> pip install --upgrade pip
> pip install JPype1-0.5.7-cp27-none-win_amd64.whl
```
4. 명령 프롬프트로 KoNLPy 설치하기
```
> pip install konlpy
```
## 터미널 명령줄 사용법
```
python word_cloud_en.py
```

