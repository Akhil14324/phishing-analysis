import re

phishing_keywords = [
    "urgent", "verify", "suspended", "click here",
    "limited time", "account blocked", "reset password"
]

def analyze_email(email):
    score = 0
    email_lower = email.lower()

    for word in phishing_keywords:
        if word in email_lower:
            score += 1

    urls = re.findall(r"http[s]?://\S+", email)
    if urls:
        score += 1

    if score >= 3:
        return "Phishing"
    else:
        return "Legitimate"

with open("emails.txt", "r") as file:
    content = file.read()

emails = content.split("\n\n")

for i, email in enumerate(emails, start=1):
    result = analyze_email(email)
    print(f"Email {i}: {result}")
    print("-" * 30)
