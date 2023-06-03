
import re

def is_spam(text):
    spam_indicators = [
        r'\d{2,}',  # 2 or more consecutive digits
        r'[.*]',  # special characters
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',  # URLs
        r'[A-Za-z0-9\._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}',  # email addresses
        r'\b(광고)\b',  # spam indicator words
    ]

    spam_count = 0
    total_count = len(text.split())

    for indicator in spam_indicators:
        matches = re.findall(indicator, text)
        if matches:
            spam_count += len(matches)

    if total_count == 0:
        return False

    spam_ratio = spam_count / total_count

    if spam_ratio > 0.3:
        return True
    else:
        return False
