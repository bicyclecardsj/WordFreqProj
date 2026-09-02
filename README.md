# 📊 단어 빈도수 시각화 대시보드

Streamlit과 KoNLPy를 활용하여 CSV 파일 형태의 한국어 텍스트 데이터에서 키워드를 추출하고, 이를 막대그래프 및 워드클라우드로 시각화해 주는 웹 대시보드 서비스입니다.

---
## 🛠 기술 스택

### Environment
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

### Framework & Libraries
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![KoNLPy](https://img.shields.io/badge/KoNLPy-009688?style=for-the-badge)
![WordCloud](https://img.shields.io/badge/WordCloud-4B0082?style=for-the-badge)

---

## 🛠 기술 스택

## 📌 주요 기능

* **CSV 파일 데이터 불러오기 & 미리보기**: 사용자가 원하는 CSV 파일을 업로드하고, 분석할 컬럼을 지정하여 파일 데이터를 미리 확인할 수 있습니다.
* **한국어 자연어 처리 (NLP)**: KoNLPy의 `Okt` 형태소 분석기를 활용해 명사, 동사, 형용사 등 의미 있는 품사만 추출하고 불용어(Stopwords)를 제거합니다.
* **사용자 정의 시각화 옵션**:
  * **수평 막대그래프 (Bar Chart)**: 상위 N개 키워드의 빈도수를 직관적으로 확인
  * **워드클라우드 (Word Cloud)**: 키워드 빈도에 따른 시각적 텍스트 클라우드 생성
* **대시보드 사이드바 설정**: 보여줄 단어 수(10~500개) 조정 및 시각화 항목 선택 가능

---

## 📸 실행 화면 (Screenshots)

| 1. CSV 파일 업로드 및 데이터 확인 | 2. 빈도수 막대그래프 시각화 | 3. 워드클라우드 시각화 |
| :---: | :---: | :---: |
| ![파일 업로드](https://github.com/user-attachments/assets/81ad07f0-7e81-4c7d-bbdd-185bc4abd717") | ![막대그래프](https://github.com/user-attachments/assets/49807628-a3a3-441d-b9f2-f455e811dd90) | ![워드클라우드](https://github.com/user-attachments/assets/3bfdc6fe-ffa0-42c7-868b-5f2a10cf2777") |

---

## 🚀 시작 가이드
1. 사전 요구사항
Python 3.8+

Java (JDK 8 이상): KoNLPy 작동을 위해 필요하며 JAVA_HOME 환경변수 설정이 완료되어야 합니다.

2. 패키지 설치
pip install streamlit pandas matplotlib konlpy wordcloud

3. 애플리케이션 실행
streamlit run WordFreqDashboard.py

---

## 📁 프로젝트 구조

```text
├── mylib/
│   ├── myTextAnalyzer.py        # 텍스트 로드, 한국어 토큰화 및 빈도수 추출 모듈
│   └── myStreamlitVisualizer.py # Matplotlib & WordCloud 시각화 모듈
├── WordFreqDashboard.py         # Streamlit 대시보드 메인 실행 파일
└── README.md                    # 프로젝트 설명 문서
