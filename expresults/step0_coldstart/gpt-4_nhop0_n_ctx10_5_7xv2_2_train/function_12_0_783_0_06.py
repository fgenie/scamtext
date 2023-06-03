
import re

def is_spam(message):
    # Check for common spam words and phrases
    spam_keywords = [
        r'\d{1,}\s?[퍼|.%]\s?[센]?.\w{1,}',
        r'[가-힣]*\d+[가-힣]*[광고]',
        r'[적중|수익].{1,}\%',
        r'http[s]?://.{6,}',
        r'칩.계열사',
        r'랩.가드',
    ]

    # Check for message length
    if len(message.split()) > 40:
        return True

    # Check for spam keywords in the message
    for keyword in spam_keywords:
        if re.search(keyword, message):
            return True

    # If no spam characteristics found, return False
    return False
