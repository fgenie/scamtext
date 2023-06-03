
import re

def is_spam(message):
    # Define a list of spam keywords
    spam_keywords = [
        "추천", "광고", "성과", "배터리", "지급중", "자동화", "육박"
    ]

    # Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_url = bool(url_pattern.search(message))

    # Count the number of spam keywords present in the message
    keyword_count = sum([1 for keyword in spam_keywords if keyword in message])

    # If the message has URL or contains more than one spam keyword, classify it as spam
    if has_url or keyword_count > 1:
        return True

    return False
