import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time # used for prodress bar

st.title('streamlit 勉強中')

st.write("テキスト入力テスト")

# progress bar
st.write('show prgressbar')

'start!'

latest_iteration = st.empty()
bar = st.progress(0) # indicate the type of prgoress value 0:int, 0.0 ;: float

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


'Done!!!!'

# column display
left_column, right_column = st.beta_columns(2)

button=left_column.button('Display Char in right column')
if button:
    right_column.write('Here is right column')


# expander
st.write('Case-Answer with Expander')
expander1=st.beta_expander('Case1')
expander1.write('You should do xxxxx')
expander2=st.beta_expander('Case2')
expander2.write('You should do xxxxx')
expander3=st.beta_expander('Case3')
expander3.write('You should do xxxxx')
expander4=st.beta_expander('Case4')
expander4.write('You should do xxxxx')
expander5=st.beta_expander('Case5')
expander5.write('You should do xxxxx')



#Publication app on Web


