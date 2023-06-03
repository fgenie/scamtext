
import re

def is_spam(message):
    spam_keywords = ['FDA', '임상3상', '정부', '신약개발관련', 'VIP체험반', '전략 마감임박', '차별']
    message = message.lower()
    
    # Check for excessive non-alphanumeric, non-korean characters or newline characters
    non_alphanumeric = re.findall(r"[^a-z0-9ㄱ-ㅎ가-힣\s]", message, re.IGNORECASE | re.MULTILINE)
    if len(non_alphanumeric) > 20 or message.count('\n') > 3:
        return True

    # Check for URLs
    if re.findall(r"https?://[\w\.]+", message):
        return True

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in message.lower():
            return True

    return False
