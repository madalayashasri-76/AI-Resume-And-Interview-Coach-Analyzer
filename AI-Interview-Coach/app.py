import streamlit as st
from resume_analyzer import analyze_resume
from interview_generator import generate_questions
from mistral_ai import generate_ai_response
import datetime

# ---------------- Page Configuration ----------------

st.set_page_config(
    page_title="AI Interview Coach",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Custom Styling ----------------

st.markdown("""
<style>

.main {
    background-color: #f8f9fa;
}

h1 {
    color: #2c3e50;
}

h2 {
    color: #34495e;
}

.stButton>button {
    width: 200px;
    border-radius: 10px;
    height: 40px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Sidebar ----------------
menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📄 Resume Analyzer",
        "🎯 Interview Practice",
        "ℹ️ About"
    ]
)

# ---------------- Dashboard ----------------

if menu == "🏠 Dashboard":

    st.title("🤖 AI Interview Coach Dashboard")

    st.write(
        """
        Welcome to AI Interview Coach.

        Improve your interview preparation using AI-powered
        resume analysis and personalized interview questions.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Resume Analysis",
            "Available"
        )

    with col2:
        st.metric(
            "AI Questions",
            "Generated"
        )

    with col3:
        st.metric(
            "Interview Mode",
            "Active"
        )

    st.subheader("🚀 Application Features")

    features = [
        "📄 Resume PDF Analysis",
        "📊 Resume Score Calculation",
        "🛠 Skill Detection",
        "🤖 Mistral AI Interview Questions",
        "💡 Interview Suggestions",
        "📥 Report Generation"
    ]

    for feature in features:
        st.success(feature)

# ---------------- Resume Analyzer ----------------

elif menu == "📄 Resume Analyzer":

    import PyPDF2

    st.title("📄 Resume Analyzer")

    st.write(
        "Upload your resume PDF to analyze your profile."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file:

        st.success(
            "Resume uploaded successfully!"
        )

        st.write(
            "File Name:",
            uploaded_file.name
        )

        # Extract text from PDF

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        resume_text = ""

        for page in pdf_reader.pages:

            text = page.extract_text()

            if text:
                resume_text += text

        st.subheader(
            "📄 Extracted Resume Content"
        )

        st.text_area(
            "Resume Text",
            resume_text,
            height=300
        )

        if st.button("🔍 Analyze Resume"):

            result = analyze_resume(resume_text)

            st.subheader(
                "📊 Resume Score"
            )

            st.progress(
                result["score"] / 100
            )

            st.success(
                f"Your Resume Score: {result['score']}/100"
            )

            st.subheader(
                "🛠 Skills Found"
            )

            if result["skills"]:

                for skill in result["skills"]:
                    st.write("✅", skill)

            else:
                st.warning("No skills detected")

            st.subheader("📌 Resume Sections")

            for section, status in result["sections"].items():

                if status:
                    st.write("✅", section)
                else:
                    st.write("❌", section)

            st.subheader("💡 Suggestions")

            for suggestion in result["suggestions"]:
                st.warning(suggestion)
# ---------------- Interview Practice ----------------

elif menu == "🎯 Interview Practice":

    st.title("🎯 AI Interview Practice")

    st.write(
        "Generate personalized interview questions using Mistral AI."
    )

    role = st.selectbox(
        "Select your Target Role",
        [
            "Data Analyst",
            "Python Developer",
            "Full Stack Developer",
            "Machine Learning Engineer",
            "Software Engineer"
        ]
    )

    resume_summary = st.text_area(
        "Paste your Resume Summary",
        placeholder="Example: Python developer with skills in SQL, Power BI, Machine Learning...",
        height=200
    )

    if st.button("🤖 Generate AI Interview Questions"):

        if resume_summary:

            prompt = f"""
You are an expert technical interviewer.

Candidate Profile:
{resume_summary}

Target Job Role:
{role}

Generate interview preparation material.

Include:

1. Five technical interview questions.
2. Ideal answers for each question.
3. One interview tip for each question.

Format the response clearly with headings and bullet points.
"""

            with st.spinner(
                "Mistral AI is preparing your interview..."
            ):

                response = generate_ai_response(prompt)

            st.subheader(
                "🤖 AI Generated Interview Preparation"
            )

            st.write(response)

            report = f"""
AI Interview Coach Report

Generated On:
{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

Target Role:
{role}

Candidate Summary:
{resume_summary}

Interview Preparation:

{response}
"""

            st.download_button(
                label="📥 Download Interview Report",
                data=report,
                file_name="AI_Interview_Report.txt",
                mime="text/plain"
            )

        else:

            st.warning(
                "Please enter your resume summary first."
            )
# ---------------- About ----------------
# ---------------- About ----------------

elif menu == "ℹ️ About":

    st.title("ℹ️ About AI Interview Coach")

    st.markdown(
        """
# 🤖 AI Interview Coach

**AI Interview Coach** is an AI-powered interview preparation platform
designed to help students and job seekers improve their career readiness.

This application uses **Artificial Intelligence, Natural Language
Processing, and Generative AI** to analyze resumes, identify skills,
evaluate resume quality, and generate personalized interview guidance.

The platform provides an interactive environment where users can
understand their strengths, improve their resumes, and practice
role-based interview questions.

---

## 🎯 Project Vision

The main goal of AI Interview Coach is to make interview preparation
smarter, easier, and more personalized by providing:

- 📄 Intelligent Resume Analysis
- 🛠 Technical Skill Identification
- 📊 Resume Quality Evaluation
- 🤖 AI-generated Interview Questions
- 💡 Personalized Preparation Suggestions
- 📥 Downloadable Interview Reports

---

## 🚀 Key Features

### 📄 Resume Analyzer

✔ Upload Resume in PDF Format  
✔ Extract Resume Information  
✔ Analyze Technical Skills  
✔ Evaluate Resume Quality  
✔ Provide Improvement Suggestions

### 🤖 AI Interview Practice

✔ Generate Job Role-based Interview Questions  
✔ Create AI-generated Sample Answers  
✔ Provide Interview Preparation Tips  
✔ Support Personalized Practice Sessions

### 📊 Smart Career Assistance

✔ Understand Resume Strengths and Weaknesses  
✔ Improve Interview Confidence  
✔ Prepare for Technical Discussions

---

## 🛠 Technology Stack

### Programming Language

🐍 Python

### Application Framework

🎨 Streamlit

### Artificial Intelligence

🤖 Mistral AI API

🧠 Generative AI

### Python Libraries

📌 PyPDF2 - Resume PDF Text Extraction

📌 Pandas - Data Processing

📌 Plotly - Data Visualization

📌 OpenAI Python Library (for Mistral API)

---

# 👩‍💻 About The Developer

## Yashasri Madala

**Data Science Student**

Yashasri Madala is a passionate Data Science student interested in
building intelligent applications using Artificial Intelligence,
Machine Learning, and Data Analytics.

She enjoys transforming ideas into practical technology solutions
by combining programming skills, data-driven approaches, and modern
AI technologies.

Through academic learning and hands-on projects, she has developed
experience in Python programming, data analysis, machine learning,
AI application development, and visualization tools.

She is passionate about exploring emerging technologies like
Generative AI and creating applications that solve real-world
problems and improve user experiences.

---

## 🎯 Areas of Interest

🤖 Artificial Intelligence

📊 Data Science & Data Analytics

🧠 Machine Learning

🗣 Generative AI & Large Language Models

🐍 Python Development

📈 Data Visualization

---

## 💻 Technical Skills

🐍 Python

🗄 SQL

📊 Data Analysis

🤖 Machine Learning

🎨 Streamlit

📈 Power BI

🔧 Git & GitHub

---

## 🔗 Connect With Me

GitHub:
https://github.com/madalayashasri-76

LinkedIn:
https://www.linkedin.com/in/yashasri-madala-036b25389/

---

## 🌱 Future Enhancements

🔹 Voice-based Mock Interviews

🔹 Real-time Interview Performance Feedback

🔹 Job Description and Resume Matching

🔹 ATS Resume Score Improvement

🔹 Cloud Deployment

---

### 🚀 Built with Python, Streamlit, and Mistral AI
"""
    )

# ---------------- Footer ----------------

st.divider()

st.caption(
    "Developed by Yashasri Madala | AI Interview Coach Project"
)