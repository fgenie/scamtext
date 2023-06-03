
import re

def is_spam(message):
    # Identify common spam keywords and patterns
    spam_keywords = ["지니틱스", "나노 수익", "종목", "체험반", "단타", "하루 일 확"]
    spam_url_pattern = re.compile(r"(https?://)?(www.)?([a-zA-Z0-9\-_]+\.[a-zA-Z]+)/?[a-zA-Z0-9\-_]*")

    # Check for presence of spam keyword in message (case-insensitive)
    if any(keyword.lower() in message.lower() for keyword in spam_keywords):
        return True

    # Check for presence of spam url pattern
    if spam_url_pattern.search(message):
        return True

    return False
