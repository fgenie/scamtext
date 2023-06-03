
import re

def is_spam(message):
    # Check for typical spam phrases
    spam_phrases = [
        r"성투",
        r"상담",
        r"광고",
        r"매수",
        r"상한가",
        r"무료",
        r"종목",
    ]

    for phrase in spam_phrases:
        if re.search(phrase, message):
            return True

    # Check for the presence of URLs
    url_patterns = [
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        r"www.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[-!*[+(,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
    ]

    for url_pattern in url_patterns:
        if re.search(url_pattern, message):
            return True

    return False
