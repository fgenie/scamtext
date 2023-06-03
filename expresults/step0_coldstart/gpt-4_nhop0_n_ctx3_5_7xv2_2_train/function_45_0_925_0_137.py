
import re

def is_spam(message):
    # Check for excessive capitalization
    excessive_caps = len(re.findall(r'[A-Z]', message)) / len(message) > 0.5

    # Check for presence of urls
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_urls = len(url_pattern.findall(message)) > 0

    # Check for special characters in the message
    special_chars = len(re.findall(r'[!?@#$%^&*]', message)) > 2

    # Check for excessive line breaks
    excessive_line_breaks = len(re.findall(r'\n', message)) > 2

    # Check for spam keyword patterns
    spam_keywords = ['광고', '추천', '현황', '종목', '목표가']
    has_spam_keywords = any([keyword in message for keyword in spam_keywords])

    return excessive_caps or has_urls or special_chars or excessive_line_breaks or has_spam_keywords
