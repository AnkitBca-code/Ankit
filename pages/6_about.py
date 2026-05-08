"""#date:22/4/26
#use of markdown , write , code and subheader
import streamlit as st
st.title("About Us")
st.markdown("A CV analysis using AI project is an automated system that uses Natural Language Processing (NLP) and Machine Learning (ML) to parse, rank, and evaluate job applications against job descriptions. It automates screening by extracting skills, experience, and education from resumes, eliminating manual, time-consuming tasks and reducing human bias.")
st.subheader("Key Aspects of the Project")
st.write("Automatic Parsing: Extracts structured data (skills, experience, contact info) from unstructured formats like PDF or DOCX using tools like Pyresparser")
st.subheader("Ranking & Scoring: ")
st.markdown("Compares candidates to job descriptions, scoring them based on skill matching, experience level, and education, often producing a 0-100% match score.")
st.subheader("Keyword Extraction:")
st.markdown("Detects relevant technical skills and phrases to ensure candidates meet requirements.")
st.subheader("Coding")
st.code("from PyPDF2 import PdfReader")
st.code("def extract_text(pdf_path):")
st.code("reader = PdfReader(pdf_path)text = ")
st.code("for page in reader.pages:")
st.code("text += page.extract_text()return text")

"""


import streamlit as st
st.title("📌 About Us")

st.markdown("""
### 📰 Fake News Detection System

In today’s digital world, misinformation spreads rapidly across social media and online platforms. 
Our **Fake News Detection System** is designed to help users identify whether a news article is **real or fake** using Artificial Intelligence techniques.

---

### 🎯 Our Mission
Our mission is to:
- Reduce the spread of misinformation  
- Promote awareness and critical thinking  
- Provide a reliable tool for verifying news content  

---

### 🤖 How It Works
This system uses **Natural Language Processing (NLP)** and **Machine Learning models** to analyze the text of news articles.  
It evaluates patterns, keywords, and linguistic features to determine the authenticity of the news.

---

### 🚀 Features
- 🔍 Instant news verification  
- 🧠 AI-powered prediction  
- 📊 Easy-to-use interface  
- ⚡ Fast and accurate results  

---

### 👨‍💻 Our Team
This project is developed as part of an academic initiative to explore real-world applications of Artificial Intelligence.  
We aim to continuously improve the system for better accuracy and usability.

---

### 🌐 Why It Matters
Fake news can influence public opinion, create confusion, and harm society.  
Our system helps users make informed decisions by providing a quick and reliable way to verify information.

---

### 📬 Contact Us
For feedback or queries, feel free to reach out through the Contact page.

""")



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