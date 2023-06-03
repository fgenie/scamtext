
import re

def is_spam(message):
    # Check for suspicious words or patterns in the message
    spam_keywords = ['회사공시', '수익률', '오르기 전', '주식', '클릭 종목확인', '마지막반', '체험반', '익 절 가', '연혁']
    spam_patterns = [
        re.compile(r'https://.*kr/'), # Suspicious shortened URLs
        re.compile(r'\d{1,2}차목표가'), # Target price patterns
        re.compile(r'- \d{4}년') # Year patterns for profiling person
    ]

    # Check if message contains any suspicious words
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check if message matches any suspicious patterns
    for pattern in spam_patterns:
        if pattern.search(message):
            return True

    # If none of the above checks pass, consider the message as normal
    return False
