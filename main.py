import streamlit as st
#st.title("Wellcome")
#st.header("rte")
#import pandas as pd
#dataset = pd.read_csv("TrafficViolationOCT2024.csv")
#st.dataframe(dataset)
name = st.text_input("Enter your Name : ")
fname = st.text_input("Enter your Father Name : ")
adr = st.text_area("Enter your text :")
classdata = st.selectbox("Enter your class : ",(1,2,3,4,5))
button = st.button("Done")
if button :
    st.markdown(f"""
Name : {name}
Father Name :{fname}
Address : {adr}
class : {classdata}""")