import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image#画像表示
import time
st.title('Streamlit 超入門')

#st.write('DataFrame')

#df = pd.DataFrame({
#    '1列目' : [1, 2, 3, 4],
#    '2列目' : [10, 20, 30 ,40]
#    })

#st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
# ↑動的な表（writeは表の幅等が指定できない）
#st.table(df.style.highlight_max(axis=0))
#静的な表↑（ソートとかはできない

#マークダウン↓（
#"""
# 章 ←大文字で表示
## 節　←中文字で表示
### 項　←小文字で表示
#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#""

#df = pd.DataFrame(
#    np.random.rand(20, 3),
#    columns=['a', 'b', 'c']
#)
#↓折れ線グラフ
#st.line_chart(df)
#st.area_chart(df)

#マップ
#df = pd.DataFrame(
#    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],#35.69と139.70は新宿付近
#    columns=['lat', 'lon']#緯度と経度
#)
#st.map(df)

#画像↓
st.write('プログレスバーの表示')
'Start!!'

larest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    larest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
'Done!!!!!'

# if st.checkbox('Show Image'):#trueかfalseで返す
#     img = Image.open('onepiece01_luffy.png')
#     st.image(img, caption='onepi', use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を教えて',
#     list(range(1, 11))
# )
# 'あなたの好きな数字は、', option, 'です。'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ1')
expander.write('問い合わせの1回答')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ2の回答')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味を教えてください。')
# #スライダー↓
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)#最小値、最大値、標準値
# 'あなたの趣味:', text
# 'コンディション：', condition