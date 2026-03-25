import streamlit as st
import face_recognition
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="人脸识别系统", layout="centered")

st.title("《人工智能通识》人脸识别系统")
st.write("上传一张照片，系统将自动检测人脸位置。")

# 上传文件组件
uploaded_file = st.file_uploader("选择一张图片...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 将上传的文件转换为 PIL 图像，再转为 numpy 数组
    image = Image.open(uploaded_file)
    image_np = np.array(image.convert('RGB'))

    with st.spinner('正在处理中...'):
        # 1. 查找图像中所有的人脸位置
        face_locations = face_recognition.face_locations(image_np)
        
        # 2. 绘制识别框 (使用 OpenCV)
        # 注意：face_recognition 返回的是 (top, right, bottom, left)
        annotated_image = image_np.copy()
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(annotated_image, (left, top), (right, bottom), (0, 255, 0), 2)

    # 显示结果
    st.subheader(f"检测到 {len(face_locations)} 张人脸")
    st.image(annotated_image, caption='处理后的图像', use_column_width=True)
    
    if len(face_locations) > 0:
        st.success("人脸检测完成！")
    else:
        st.info("未检测到人脸，请换一张图片试试。")
