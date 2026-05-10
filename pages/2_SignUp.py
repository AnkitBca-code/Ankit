import streamlit as st
import random
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


st.title("SignUp")
c1,c2=st.columns(2)
name=c1.text_input("User Name")
Password=c1.text_input("Password")
c=c1.selectbox("Course",['BCA','IT','CS','AI & ML'])
g=c1.radio("Gender",['M','F'])
address=c2.text_area("Address")
dob=c2.date_input("DOB")
co=c2.color_picker("Select Color",value="#00f900")
#web_cam=c2.camera_input("Take a picture")
#count=random.randint(1,100)
#str1="img"+str(count)+".png"
#st.write(str1)
#with open(str1,"wb") as f:
#       f.write(web_cam.getvalue())
b1=st.button("SAVE")
def get_data():
       st.success("Following Deatils are save successfully")
       st.write(name)
       st.write(Password)
       st.write(c)
       st.write(g)
       st.write(address)
       st.write(dob)
       st.write(co)
       #st.write(str1)
       conn=pymongo.MongoClient("mongodb+srv://lalanprasadgupta726097_db_user:Cmy8ddC5RHQ3Ymmc@cluster0.ussmgak.mongodb.net/?appName=Cluster0")
       mydb=conn["news"]
       my=mydb["user_info"]
       my.insert_one({"username":name,"password":Password,"course":c,"gender":g,"address":address,"dob":str(dob),"color":co})
       st.success("You are registered !!!")
       
       
if b1:
       get_data()





                         










