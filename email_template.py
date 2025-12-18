from openai import OpenAI

client = OpenAI()

def generate_email(job, resume_summary):
    prompt = f"""
Candidate Summary:
{resume_summary}

Job Title: {job['title']}
Company: {job['company']}
Experience Level: {job['experience']}

Job Description:
{job['jd']}

Write a professional outreach email for an associate-level role.
Tone: polite, concise, human.
Do not exaggerate experience.
120 words max.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You write professional recruiter emails."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
