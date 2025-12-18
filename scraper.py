import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

ROLES = [
    "Associate Cloud Engineer 2-3 years",
    "Associate DevOps Engineer 2-3 years",
    "Associate Site Reliability Engineer 2-3 years"
]

def scrape_jobs():
    jobs = []

    for role in ROLES:
        url = f"https://www.google.com/search?q={role}+jobs&ibp=htl;jobs"
        res = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(res.text, "html.parser")

        for job_card in soup.select("div.BjJfJf")[:5]:
            try:
                title = job_card.select_one("h2").text
                company = job_card.select_one(".vNEEBe").text
                location = job_card.select_one(".Qk80Jf").text
                link = job_card.find("a")["href"]

                jobs.append({
                    "title": title,
                    "company": company,
                    "location": location,
                    "experience": "2–3 Years",
                    "jd": title + " role requiring 2–3 years experience.",
                    "apply_link": link
                })
            except Exception:
                continue

    return jobs

