
import re

def is_spam(text):
    # Check for message length
    if len(text) < 20:
        return False

    url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    spam_keywords = ['적중', '주식', '고정수입', '추천주', '실현', '단타', '체험반', '달성기념', '상승']
    large_percentage_pattern = '[0-9]*[.]?[0-9]+%'

    # Check for urls
    if re.search(url_pattern, text):
        return True

    # Check for spam keywords
    if any(keyword in text for keyword in spam_keywords):
        return True

    # Check for large percentage values
    if re.search(large_percentage_pattern, text):
        return True

    return False
