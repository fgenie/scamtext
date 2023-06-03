
import re

def is_spam(message):
    keywords = ["수익", "차체험반", "고정수입", "성공", "엠바고", "식약처", "공개", "급등주", "종목", "광고", "무료거부", "체험반"]
    spam_url_patterns = ["me2\.kr", "buly\.kr", "bit\.ly", "han\.gl"]
    
    message = message.lower()

    # Check for spam keywords
    for keyword in keywords:
        if keyword in message:
            return True

    # Check for spam URLs
    for pattern in spam_url_patterns:
        if re.search(pattern, message):
            return True

    # If none of the conditions above are met, consider the message as normal
    return False
