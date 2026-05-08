import streamlit as st
import time
import pymongo
conn=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2")
mydb=conn["news"]
my=mydb["user_info"]

with st.spinner("Loading..."):
    time.sleep(1)

# BACKGROUND-COLOR
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



# TOP BAR
col1, col2 = st.columns([9,1])

with col1:
    st.title("User Profile")

with col2:
    if st.button("⏻"):
        
        # SESSION REMOVE
        del st.session_state['username']
        
        st.switch_page("1_main.py")

# SESSION CHECK
if 'username' in st.session_state:

    st.success(f"Welcome: {st.session_state['username']}")

    c1, c2, c3 = st.columns(3)
    
    with c1:
        with st.expander("Change Password"):
            old_pass = st.text_input("Enter Old Password", type="password")
            new_pass = st.text_input("Enter New Password", type="password")

            if st.button("Update Password"):
                str1 = st.session_state['username']

                res = my.find_one({
                    "username": str1,
                    "password": old_pass
                })

                if res:

                   my.update_one(
                      {"username": str1},
                      {"$set": {"password": new_pass}}
                   )

                   st.success("Password Changed Successfully")

                else:
                    st.error("Old Password Incorrect")
                
    
              
    with c2:
        with st.expander("See Your Profile"):
            st.success("USER PROFILE DETAILS")

            str1 = st.session_state['username']

            res = my.find({"username": str1})

            for data in res:
                st.write(f"👤Username : {data['username']}")
                st.write(f"🔒 Password : {data['password']}")
                st.write(f"⚧ Gender : {data['gender']}")
                st.write(f"🏠 Address : {data['address']}")
                st.write(f"🎂 DOB : {data['dob']}")


     
    if c3.button("Fake News Detection System"):
        pass

else:
    st.error("Please Login First")
       
