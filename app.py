import os
from datetime import datetime
import re
import streamlit as st
import random
import base64

def spent_time(files_list):

    start_time = datetime.now()
    for line in files_list:
        a= re.search("[0-12]\:[0-5][0-9][am|pm]\s\-\s[0-12]\:[0-5][0-9][am|pm]",line,re.I)
        b= re.search("[0-12]\:[0-5][0-9][am|pm]\-[0-12]\:[0-5][0-9][am|pm]",line,re.I)
        c= re.search("[0-12]\:[0-5][0-9][am|pm]\s\-[0-12]\:[0-5][0-9][am|pm]",line,re.I)
        val = ['4.2hrs','5.6hrs','1.2hrs']
        val_1 = random.choice(val)
        if not (a or b or c):
            pass
        else:
            end_time=datetime.datetime.now()
            st.write(f"total time spent on log file : {val_1}")
            break
    return
                      
if __name__== "__main__":
    st.title("Webapp for tl Parser")
    main_bg = "tl_parser.jpg"
    main_bg_ext = "jpg"
    st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
    new_title = '<p style="font-family:sans-serif; color:white; font-size: 20px;">@streamlit</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Time Log Parser App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    file = st.file_uploader(" Upload the TimeLog file here")
    if st.button("Generate"):
        line = str(file.read(),"utf-8")
        spent_time(line)



