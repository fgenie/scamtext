
import re

def is_spam(message):
    # Check for common spam words and phrases
    spam_phrases = [
        "상한가확정",
        "실력입증",
        "추천주",
        "수익 보장",
        "목표달성기념",
        "AI사업본격화"
    ]
    
    for phrase in spam_phrases:
        if phrase in message:
            return True
    
    # Check for suspicious URLs
    url_pattern = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)')
    match = url_pattern.search(message)
    if match:
        url = match.group()
        if 'me2.kr' in url:
            return True

    # Check for suspicious amount of money
    money_pattern = re.compile(r'((\d{1,3}(,\d{3})*)원)')
    match = money_pattern.search(message)
    if match:
        return True

    # Check for suspicious date patterns
    date_pattern = re.compile(r'\d{1,2}[日月]?')
    match = date_pattern.search(message)
    if match:
        return True

    return False
