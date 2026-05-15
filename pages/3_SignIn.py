import streamlit as st
import pymongo
import time

st.set_page_config(page_title="Sign In", layout="centered")

# ---------------- CSS ----------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #d5e1e3;
    }

    /* FORM BOX */
    .signin-box {
        background-color: white;
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0px 5px 18px rgba(0,0,0,0.15);
    }

    /* TITLE */
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #1f2937;
    }

    /* BUTTON */
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        height: 48px;
        font-size: 18px;
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

# ---------------- FORM BOX ----------------


st.markdown(
    "<div class='title'>🔐 Sign In</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<center>Fake News Detection System</center><br>",
    unsafe_allow_html=True
)

# ---------------- INPUTS ----------------

t1 = st.text_input("🆔 Username")

t2 = st.text_input("🔒 Password", type="password")

remember = st.checkbox("Remember Me")

# ---------------- BUTTON ----------------

if st.button("🚀 Sign In"):

    with st.spinner("Checking Login..."):
        time.sleep(2)

    # DATABASE CONNECTION
    conn = pymongo.MongoClient(
        "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.8.2"
    )

    mydb = conn["news"]

    my = mydb["user_info"]

    res = my.find({"username": t1, "password": t2})

    v = 0

    for data in res:

        v = v + 1

        st.session_state['username'] = t1

        st.success("Login Successful ✅")

        st.balloons()

        time.sleep(1)

        st.switch_page("pages/pro.py")

    if v == 0:
        st.error("Invalid Username or Password ❌")

st.markdown("</div>", unsafe_allow_html=True)
