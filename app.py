import streamlit as st
from matplotlib import image
import os

tab1, tab2, tab3 = st.tabs(["INTRODUCTION","EDUCATION", "INTERNSHIP"])

with tab1:
    st.title("JONNALAGADDA SAIKUMAR")
    st.header("CONNECT:")
    st.write("LINKDIN: [link](https://www.linkedin.com/in/saikumar-jonnalagadda-305003215)")
    st.write("GITHUB: [link](https://github.com/SaikumarJonnalagadda)")
    
    


with tab2:
    st.title("EDUCATION")
    st.header("10T CLASS")
    st.text("      CBSE")
    st.text("      HARVEST PUBLIC SCHOOL")
    st.header("12 CLASS")
    st.text("      NARAYANA JUNIOR COLLEGE")
    st.text("      Telangana State Board of Intermediate Education")
    st.header("B.TECH")
    st.text("      Amrita Vishwa Vidyapeetham")
    
    



with tab3:
    st.title("INTERNSHIP")
    st.header(" Innomatics Research Labs")
    st.text("IN DATA SCIENCE")
    FILE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    dir_of_interest = os.path.join(FILE_DIR, "resources")
    IMAGE_PATH = os.path.join(dir_of_interest, "images", "Congratulations.jpg")
    img = image.imread(IMAGE_PATH)
    st.image(img)

btn_click1 = st.button("Click Me!")

if btn_click1 == True:
    st.subheader("You clicked me :cry:")
    st.balloons()