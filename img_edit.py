import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center;'>Image Editor</h1>",unsafe_allow_html=True)
st.markdown("---")
image=st.file_uploader("Upload your Image: RK", type=['jpeg','png','jpg'])
info=st.empty()
size=st.empty()
mode=st.empty()
format_=st.empty()
if image:
    img=Image.open(image)
    info.markdown("<h2 style='text-align:center;'>Information</h2>",unsafe_allow_html=True)
    size.markdown(f"<h6>Size: {img.size}</h6>",unsafe_allow_html=True)
    mode.markdown(f"<h6>Mode: {img.mode}</h6>",unsafe_allow_html=True)
    format_.markdown(f"<h6>Format: {img.format}</h6>",unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Resizing</h2>",unsafe_allow_html=True)
    width=st.number_input("width",value=img.width)
    height=st.number_input("height",value=img.height)
    st.markdown("<h2 style='text-align:center;'>Rotation</h2>",unsafe_allow_html=True)
    degree=st.number_input("degree")
    st.markdown("<h2 style='text-align:center;'>Filters</h2>",unsafe_allow_html=True)
    filters=st.selectbox("Filters",options=("None","Blur", "Detail", "Emboss", "Smooth"))
    s_btn=st.button("Submit")
    col1,col2=st.columns(2)
    if s_btn:
        edited=img.resize((width,height)).rotate(degree)
        filtered=edited
        if filters != "None":
            if filters == "Blur":
                filtered=edited.filter(BLUR)
            elif filters == "Detail":
                filtered=edited.filter(DETAIL)
            elif filters == "Emboss":
                filtered=edited.filter(EMBOSS)
            elif filters == "Smooth":
                filtered=edited.filter(SMOOTH)
        
        col1.text("Original Img: ")
        col1.image(img)
        col2.text("Edited Img: ")
        col2.image(filtered)
        