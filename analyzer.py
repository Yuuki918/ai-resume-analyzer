import openai
from config import openai_api_key

openai.api_key = openai_api_key

def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an AI resume analyzer. A user submitted this resume:

---RESUME---
{resume_text}

---JOB DESCRIPTION---
{job_description}

1. List candidate’s name, skills, and years of experience.
2. Match skills against the job requirements.
3. Score the resume from 0–100 based on relevance.
4. Suggest improvements (grammar, skills, structure).
5. Return your response in clear and concise format.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    return response.choices[0].message['content']
