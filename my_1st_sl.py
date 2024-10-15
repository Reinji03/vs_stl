import streamlit as st
st.title('첫번째 웹 어플 만들기 👋')

# 텍스트 출력
st.write('# 1. Markdown 텍스트 작성하기')

# Markdown 문법으로 작성된 문장 출력
st.markdown(
  '''
  # 마크다운 헤더1
  - 마크다운 목록1. **굵게** 표시
  - 마크다운 목록2. *기울임* 표시
   - 마크다운 목록2-1
   - 마크다운 목록2-2
 
  ## 마크다운 헤더2
  - [네이버](https: naver.com)
  - [구글](https: google.com)
 
  ### 마크다운 헤더3
  일반 텍스트
  '''
  )

# DataFrame 출력
import pandas as pd # pandas 라이브러리 임포트
st.write('# 2. DataFrame 표시하기') # 텍스트 출력
df = pd.DataFrame({ # DataFrame 생성
'이름': ['홍길동', '이순신', '강감찬'],
 '나이': [20, 45, 35]
 })

# 그래프 출력
import numpy as np # numpy 라이브러리 임포트
st.write('# 3. 그래프 표시하기') # 텍스트 출력
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"]) # DataFrame 생성
st.bar_chart(chart_data) # 바 차트 출력

from PIL import Image

st.write('# 4. 이미지 표시하기') #텍스트 출력
img = Image.open('python.jpg') # 이미지 파일 열기
st.image(img,width=300) # 이미지 출력

import streamlit as st



# 텍스트
st.header('🚗 텍스트 출력')
st.write('') # 빈 줄 삽입

st.write('# 마크다운 H1 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('')

st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.write('')

st.markdown('마크다운 : st.markdown()')
st.markdown('''
            1. ordered item
                - unordered item
                - unordered item
            2. ordered item
            3. ordered item
            ''')
st.divider() # � 구분선

# 마크다운
'''# � Magic에 마크다운을 조합
1. ordered item
    - 강조: **unordered item**
    - 기울임: *unordered item*
2. ordered item
3. ordered item
'''

# 데이터프레임
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df # � 데이터프레임 출력

# 차트
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
fig # � 차트 출력

# 사이드바 # 중간에 sidebar 넣으면 됨
st.header('⬅⬅⬅⬅ 사이드바')
st.sidebar.write('사이드바 텍스트')
st.sidebar.checkbox('체크박스 1')
st.sidebar.checkbox('체크박스 2')
st.sidebar.radio('라디오 버튼', ['radio 1', 'radio 2', 'radio 3'])
st.sidebar.selectbox('셀렉트박스', ['select 1', 'select 2', 'select 3'])

# 레이아웃: 컬럼
st.header('컬럼 레이아웃')
col_1, col_2, col_3 = st.columns([1,2,1]) # 컬럼 인스턴스 생성. 1:2:1 비율로 컬럼을 나눔

with col_1:
  st.write(' 1번 컬럼')
  st.checkbox('이것은 1번 컬럼에 속한 체크박스 1')
  st.checkbox('이것은 1번 컬럼에 속한 체크박스 2')

with col_2:
  st.write(' 2번 컬럼')
  st.radio('2번 컬럼의 라디오 버튼', ['radio 1', 'radio 2', 'radio 3']) 

col_3.write(' 3번 컬럼')
col_3.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])

# 레이아웃: 탭
st.header('탭 레이아웃')

# 탭 인스턴스 생성. 3개의 탭을 생성
tab_1, tab_2, tab_3 = st.tabs(['탭AAAAA', '탭BBBBB', '탭CCCCC']) 
with tab_1:
  st.write('탭AAAAA')
  st.write('이것은 탭A의 내용입니다.')
  fig
with tab_2:
  st.write('탭BBBBB')
  st.write('이것은 탭B의 내용입니다.')
  df
  ### 코드 블럭 넣기
  '''
  ```python
  import pandas as pd
  a=3
  b=4
  ```
  '''

tab_3.write('탭CCCCC')
tab_3.write('이것은 탭C의 내용입니다.')
tab_3.write(fig) # 코드주의!!

