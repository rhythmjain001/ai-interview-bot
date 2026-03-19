import streamlit as st
from utils import generate_question, evaluate_answer

st.title("🤖 AI Interview Preparation Bot")

role = st.selectbox("Select Job Role", [
    "Python Developer",
    "Data Scientist",
    "Machine Learning Engineer"
])

# Generate question
if st.button("Generate Question"):
    question = generate_question(role)
    st.session_state["question"] = question
    st.write("### ❓ Question:")
    st.write(question)

# Answer section
if "question" in st.session_state:
    answer = st.text_area("✍️ Your Answer")

    if st.button("Submit Answer"):
        feedback = evaluate_answer(st.session_state["question"], answer)
        st.write("### 📊 Feedback:")
        st.write(feedback)
