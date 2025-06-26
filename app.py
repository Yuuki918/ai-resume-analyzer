import streamlit as st
from parser import extract_text_from_pdf
from analyzer import analyze_resume

st.title("📄 AI Resume Analyzer (Grok-powered by GPT-4)")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
job_desc = st.text_area("Paste Job Description Here")

if uploaded_file and job_desc:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_pdf("temp_resume.pdf")
    st.subheader("🔍 Analyzing Resume...")

    result = analyze_resume(resume_text, job_desc)
    st.markdown("### 🧠 AI Evaluation:")
    st.text(result)
