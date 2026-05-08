import streamlit as st
import time

# Loading animation
with st.spinner("Analyzing news authenticity..."):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

#st.success("System Ready ✅")

# Title
st.title("Fake News Detection System 📰 ")

# Subtitle animation
st.markdown("### Detect whether news is **Real or Fake** using AI 🤖")


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


st.markdown("## 📰 Sample News")

st.markdown(
    """
    <style>
    .news-card {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 20px;
        text-align: center;
    }
    .real {
        border-top: 5px solid green;
    }
    .fake {
        border-top: 5px solid red;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

# ✅ REAL NEWS CARD
with col1:
    st.image("https://images.unsplash.com/photo-1504711434969-e33886168f5c")
    st.markdown("### ✅ Real News")
    st.write("Government launches new digital education program across India.")
    st.markdown('</div>', unsafe_allow_html=True)

# ❌ FAKE NEWS CARD
with col2:
    st.image("https://images.unsplash.com/photo-1495020689067-958852a7765e")
    st.markdown("### ❌ Fake News")
    st.write("Scientists confirm humans can live without sleep for 30 days.")
    st.markdown('</div>', unsafe_allow_html=True)