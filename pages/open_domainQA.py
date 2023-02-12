import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np
# import cv2 # 计算机视觉

# 加载图像的函数
# def load_an_image(image):
#     img = Image.open(image)
#     return img

######################################################
st.title('CogAgent')

st.markdown('''
**A KNOWLEDGE-ENHANCED TEXT REPRESENTATION TOOLKIT FOR NATURAL LANGUAGE UNDERSTANDING**
''')

st.header("Open Domain Question Answering")

st.warning('''
**Write Exit to stop**
''')

# 图片文件上传器
# image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
# if image_file is not None:
#     st.image(load_an_image(image_file), width=250)

choice = st.selectbox('Select an example or input text',['','Which part of earth is covered with water?',
'Who proved that genes are located on chromosomes?',
'Where will the summer olympics be held in 2020?',
'Who has the largest contract in the NBA?',
'Who has the most points in nba finals history?' ,
'Who died in Harry Potter and the Half-Blood Prince?'])
if choice == '':
    question = st.text_input('Question', 'Input text here or select an example')
else:
    question = st.text_input('Question', choice)
n_doc = st.slider('Please select the number of relevant articles retrieved from Wikipedia',0,100) 
       
submit = st.button('SUBMIT')

if submit:
    if question != 'Exit':
        ## return
        psgs = []
        for i in range(n_doc):
            k = 'passages_content_' + str(i)
            psgs.append(k)
        result = {
        "pred_answer": '71 percent', 
        "wiki_psgs": psgs
        }

        if question == 'Which part of earth is covered with water?':
            st.json(result)
            
        #title1 = st.text_input('Question', 'Input more')
    else:
        st.info('Thanks')
        



