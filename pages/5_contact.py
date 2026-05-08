import streamlit as st

st.title("📞 Contact Us")

st.markdown("""
### 📬 Get in Touch

Have questions, feedback, or suggestions? We'd love to hear from you!

---

### 📧 Email
fake-news-support@gmail.com  

---

### 📱 Phone
+91 9876543210  

---

### 📍 Address
Ranchi,Jharkhand,India  

---

### 🕒 Working Hours
- Monday – Friday: 9:00 AM – 6:00 PM  
- Saturday: 10:00 AM – 4:00 PM  
- Sunday: Closed  

---
""")




#BACKGROUND COLOR
def set_bg_color():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #d5e1e3;  /* dark blue */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_color()
