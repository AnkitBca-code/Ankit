import streamlit as st
import pymongo
import time

st.set_page_config(page_title="Sign Up", layout="centered")

# ---------------- SIMPLE CSS ----------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #d5e1e3;
    }

    /* FORM BOX */
    .signup-box {
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
    "<div class='title'>📝 Sign Up</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<center>Fake News Detection System</center><br>",
    unsafe_allow_html=True
)

# ---------------- FORM ----------------

c1, c2 = st.columns(2)

username = c1.text_input("🆔 Username")

email = c1.text_input("📧 Email Address")

password = c1.text_input("🔒 Create Password", type="password")

confirm_password = c1.text_input("🔑 Confirm Password", type="password")

role = c2.selectbox(
    "🎭 Select Role",
    ["News Reader", "Journalist", "Researcher", "Admin"]
)

address = c2.text_area("🏠 Address")

dob = c2.date_input("📅 DOB")

agree = st.checkbox("I agree to the Terms & Conditions")

# ---------------- BUTTON ----------------

b1 = st.button("🚀 Create Account")

def get_data():

    if password != confirm_password:
        st.error("Passwords do not match ❌")

    elif not agree:
        st.warning("Please accept Terms & Conditions")

    else:

        with st.spinner("Creating Account..."):
            time.sleep(2)

        # DATABASE CONNECTION
        conn = pymongo.MongoClient(
            mongodb+srv://lalanprasadgupta726097_db_user:Cmy8ddC5RHQ3Ymmc@cluster0.ussmgak.mongodb.net/?appName=Cluster0

        )

        mydb = conn["news"]

        my = mydb["user_info"]

        my.insert_one({
            "username": username,
            "email": email,
            "password": password,
            "role": role,
            "address": address,
            "dob": str(dob)
        })

        st.success("Account Created Successfully ✅")

    

if b1:
    get_data()

st.markdown("</div>", unsafe_allow_html=True)



                         










