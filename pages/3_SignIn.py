import streamlit as st
import pymongo


#BACKGROUND-COLOR
def set_bg_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #d5e1e3; 
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_color()



st.title("SignIn")
t1=st.text_input("Username")
t2=st.text_input("Password")
if st.button("SIGNIN"):
       conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
       mydb=conn["news"]
       my=mydb["user_info"]
       res=my.find({"username":t1,"password":t2})
       v=0
       for data in res:
              v=v+1
              st.session_state['username'] = t1
              st.switch_page("pages/4_profile.py")
              
       if v==0:
              st.success("Invalid Login !!!")




              
             
              
      
