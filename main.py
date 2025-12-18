import pandas as pd
from scraper import scrape_jobs
from email_template import generate_email

RESUME_SUMMARY = """
Associate-level Cloud/DevOps engineer with 2–3 years of experience
working on AWS, CI/CD pipelines, Docker, Kubernetes, Terraform,
monitoring, and production support.
"""

jobs = scrape_jobs()
rows = []

for job in jobs:
    email = generate_email(job, RESUME_SUMMARY)

    rows.append({
        "Job Title": job["title"],
        "Company": job["company"],
        "Location": job["location"],
        "Experience Level": job["experience"],
        "Job Description": job["jd"],
        "Apply Link": job["apply_link"],
        "Generated Email": email
    })

df = pd.DataFrame(rows)
df.to_excel("jobs_output.xlsx", index=False)

print("✅ Excel file created: jobs_output.xlsx")
