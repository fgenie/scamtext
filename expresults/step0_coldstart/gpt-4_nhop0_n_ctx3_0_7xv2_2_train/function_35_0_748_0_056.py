
import re

def is_spam(message):
    # Regular expression to check for presence of URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    
    # List of spam related keywords or phrases
    spam_keywords = ['VIP', '투자', '차별화', '추천', '시황', '카카오톡', '악성광고', '텔레그램']

    # Check for URLs in the message
    if url_pattern.search(message):
        return True

    # Check for spam keywords in the message
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # If none of the above conditions are met, it's not spam
    return False
