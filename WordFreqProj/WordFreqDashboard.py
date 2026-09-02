import streamlit as st
import mylib.myTextAnalyzer as ta
import mylib.myStreamlitVisulalizer as sv
from konlpy.tag import Okt
import pandas as pd

st.title("단어 빈도수 시각화")

# 파일 업로드
uploaded_file = st.sidebar.file_uploader("파일 선택", type=["csv"])

# 컬럼명 설정
col_name = st.sidebar.text_input("데이터가 있는 컬럼명", value=" ")

# 데이터 미리 확인해보기
if st.sidebar.button("데이터 파일 확인") and uploaded_file is not None:
    df_preview = pd.read_csv(uploaded_file)
    st.write("### 데이터 미리보기")
    st.dataframe(df_preview.head())
    uploaded_file.seek(0)

st.sidebar.header("설정")

with st.sidebar.container(border=True):
    # 빈도수 그래프 설정
    show_bar = st.checkbox("빈도수 그래프", value=True)
    num_bar_words = st.slider("단어 수 (그래프)", min_value=10, max_value=50, value=20, key="bar_slider")

    # 워드 클라우드 설정
    show_wc = st.checkbox("워드클라우드", value=False)
    num_wc_words = st.slider("단어 수 (워드클라우드)", min_value=10, max_value=500, value=50, key="wc_slider")

    # 분석 시작 버튼
    start_analysis = st.button("분석 시작", use_container_width=True)


if start_analysis:
    if uploaded_file is not None:
        try:
            file_columns = pd.read_csv(uploaded_file, nrows=0).columns
            uploaded_file.seek(0)
            
            if col_name in file_columns:
                corpus = ta.load_corpus(uploaded_file, col_name)
                
                status_box = st.empty()
                
                my_tags = ['Noun', 'Verb', 'Adjective']
                my_stopwords = ['영화', '하는', '정말', '진짜', '보고', '있는',  
                                '보는', '입니다', '그냥', '정도', '봤는데', '봤습니다',
                                '같은', '합니다', '봤어요','한번', '없는', '해서', '이런',
                                '보면']
                
                # 로딩 스피너와 함께 분석 함수 호출
                with st.spinner("데이터 분석 중... 잠시만 기다려주세요."):
                    counter = ta.count_word_freq(corpus, Okt().pos, my_tags, my_stopwords)
                
                # 결과 상단 바 출력 및 시각화
                total_reviews = len(corpus)
                total_words = sum(counter.values())

                status_box.info(f"분석이 완료되었습니다 ({total_reviews:,}개의 {col_name}, {total_words:,}개의 단어)")

                if show_bar:
                    st.write("### 빈도수 그래프")
                    sv.visualize_barh_graph(counter, num_bar_words)
                    
                if show_wc:
                    st.write("### 워드클라우드")
                    sv.visualize_wordcloud(counter, num_wc_words)
            else:
                st.error(f"입력하신 컬럼명 '{col_name}'이 파일에 존재하지 않습니다.")
        except Exception as e:
            st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
    else:
        st.warning("분석할 CSV 파일을 업로드해 주세요.")