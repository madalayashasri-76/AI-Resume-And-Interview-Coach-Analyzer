def analyze_resume(text):

    text = text.lower()

    # Skills Database
    skills = [
        "python",
        "java",
        "sql",
        "html",
        "css",
        "javascript",
        "machine learning",
        "data analysis",
        "power bi",
        "excel",
        "streamlit",
        "git",
        "github"
    ]

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    # Resume Sections

    sections = {
        "Education": "education" in text,
        "Skills": "skills" in text,
        "Projects": "project" in text or "projects" in text,
        "Experience": "experience" in text,
        "Certifications": "certification" in text or "certifications" in text
    }

    # Resume Score

    score = 0

    # 5 marks for each detected skill
    score += len(found_skills) * 5

    # 10 marks for each section
    for section in sections.values():
        if section:
            score += 10

    # Maximum score = 100
    score = min(score, 100)

    # Suggestions

    suggestions = []

    if not sections["Education"]:
        suggestions.append("Add your educational qualifications.")

    if not sections["Skills"]:
        suggestions.append("Include a dedicated Skills section.")

    if not sections["Projects"]:
        suggestions.append("Add projects to showcase your practical experience.")

    if not sections["Experience"]:
        suggestions.append("Include internships or work experience if available.")

    if not sections["Certifications"]:
        suggestions.append("Mention relevant certifications to strengthen your profile.")

    if len(found_skills) < 5:
        suggestions.append("Add more technical skills relevant to your target job role.")

    # If no suggestions
    if not suggestions:
        suggestions.append("Excellent resume! Your resume contains most important sections.")

    return {
        "score": score,
        "skills": found_skills,
        "sections": sections,
        "suggestions": suggestions
    }