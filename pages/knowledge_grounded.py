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
# st.markdown('Streamlit is **_really_ cool**.')
# st.markdown('This text is :red[colored red], and this is **:blue[colored]** and bold.')
# st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
st.markdown('''
:green[**_A KNOWLEDGE-ENHANCED TEXT REPRESENTATION TOOLKIT FOR NATURAL LANGUAGE UNDERSTANDING_**]
''')

st.header("Knowledge Grounded Dialogue")

st.warning('''
**This module is a dialogue based on unstructured knowledge, which can conduct multiple rounds of dialogue. Write Exit to stop.**
''')



l = 10  
choice = list(range(l))     
i = 0
k = 0 
#让selectbox的key值唯一
while(1):
    # if i == 0:
    
    choice = st.selectbox('Question',['Select an example or input text','What is the definition of Open relationship?','Exit'],key = k)
    if choice == 'Select an example or input text':
        question = st.text_input('Input text here','',key = k+10)
        k = k+1
        break
    else:
        question = st.text_input('Input text here',choice, key = k+10)
        k = k+1
        col1, col2 = st.columns(2)
        with col1:
            # if(i==0):
            st.subheader("User")
            if(question!=''):
                st.info(question)

        with col2:
            # if(i==0): 
            st.subheader("CogAgent")       
            if question != 'Exit':
                ## return
                result = {
                        "pred_text": 'it is a marriage in which the partners agree that each may engage in relationships relationships , without this being regarded as infidelity .', 
                    }
                if question == 'What is the definition of Open relationship?':
                    # st.json(result)
                    # st.write('Answer')
                    st.success(result['pred_text']) 
                    i = i + 1
            else:
                st.success('Thanks')
                break
    if(i > l-1):
        st.error('The maximum number of rounds of conversation is 10!')
        break
    
    



