import streamlit as st
import time
import pymongo

import pickle

# LOAD MODEL
model = pickle.load(open("../model.pkl", "rb"))
vector = pickle.load(open("../vector.pkl", "rb"))


# DATABASE CONNECTION
conn = pymongo.MongoClient(
   "mongodb+srv://lalanprasadgupta726097_db_user:Cmy8ddC5RHQ3Ymmc@cluster0.ussmgak.mongodb.net/?appName=Cluster0"
)

mydb = conn["news"]

my = mydb["user_info"]


# LOADING
with st.spinner("Loading..."):
    time.sleep(1)

# BACKGROUND COLOR
st.markdown(
    """
    <style>

    .stApp {
        background-color: #d5e1e3;
    }

    /* PROFILE BOX */
    .block-container {
        padding-top: 8rem;
    }

    /* BUTTON */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        height: 42px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

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

    # CHANGE PASSWORD
    with c1:

        with st.expander("🔒 Change Password"):

            old_pass = st.text_input(
                "Enter Old Password",
                type="password"
            )

            new_pass = st.text_input(
                "Enter New Password",
                type="password"
            )

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

                    st.success("Password Changed Successfully ✅")

                else:
                    st.error("Old Password Incorrect ❌")

    # PROFILE DETAILS
    with c2:

        with st.expander("📄 See Your Profile"):

            str1 = st.session_state['username']

            res = my.find({"username": str1})

            for data in res:

                st.write(f"🆔 Username : {data['username']}")

                st.write(f"📧 Password : {data['password']}")

                st.write(f"🎭 Role : {data['role']}")

                st.write(f"🏠 Address : {data['address']}")

                st.write(f"📅 DOB : {data['dob']}")

                st.write(f"📧 Email : {data['email']}")

    # FAKE NEWS DETECTION SYSTEM
    # FAKE NEWS DETECTION SYSTEM
        # FAKE NEWS DETECTION SYSTEM
    with c3:

        st.subheader("📰 Fake News Detection")

        news = st.text_area(
            "Enter News Content"
        )

        if st.button("Detect News"):

            if news == "":

                st.warning("Please Enter News ❗")

            else:

                transform_text = vector.transform([news])

                prediction = model.predict(transform_text)

                if prediction[0] == "FAKE":

                    st.error("❌ Fake News Detected")

                else:

                    st.success("✅ Real News")

                st.info("AI Analysis Completed")
else:

    st.error("Please Login First ❌")
