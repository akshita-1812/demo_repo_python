# pip install streamlit

import streamlit as st

st.title("Welcome to streamlit")
# st.header("this is header file")
# st.subheader("hello everyone")

# st.write("welcome to my first page")
# st.text("just text...")
# value=st.slider("pick a number",0,100)
# st.write("you selected",value)

# col1,col2=st.columns(2)
# col1.write("Left column")
# col1.write("hello python students")
# col2.write("right column")

with st.expander("click on Expand"):
    st.write("hello....")

# with st.container():
#     st.write("container block")
#     st.line_chart([1,2,4])

# st.sidebar.title("side bar")
# st.sidebar.selectbox("choose one:",['opt 1','opt 2'])

# tab1,tab2,tab3=st.tabs(["tab1","tab2","tab3"])
# tab1.write("tab 1")
# tab2.write("tab 2")
# tab3.write("tab 3")

# st.write("Above line")

# st.write("below line")