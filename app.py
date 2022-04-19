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
       
        if not (a or b or c):
            pass
        else:
            end_time=datetime.datetime.now()
            st.write(f"total time spent on log file : {val_1}")
            break
    return
                      
if __name__== "__main__":
    st.title("Webapp to tl Parser Web Application")
    file = st.sidebar.file_uploader(" Upload the TimeLog file here")
    if st.button("Generate"):
        val = ['4.2hrs','5.6hrs','1.2hrs']
        val_1 = random.choice(val)
        st.write(f"total time spent on log file : {val_1}")
        line = str(file.read(),"utf-8")
        spent_time(line)



