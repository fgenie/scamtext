
import re

def is_spam(message):
    # List of spam patterns
    spam_patterns = [
        r'\b(?:[0-9](?:[%]|,[0-9]{3})?[%]{0,1}\^?[+/-]|[0-9]*\s*(?:\^|[+/-])\s*[0-9]+\s*(?:\^|[+/-]))',
        r'\bhttp(?:s)?://\w+',
        r'\b비밀번호',
        r'\b상한가',
        r'\b승률',
        r'\b운영자',
        r'\b수익',
        r'\b테마주',
        r'\b종목',
        r'\b정보',
        r'\b체험',
        r'\b신청',
        r'\b입장'
    ]

    # Check if message contains any of the spam patterns
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    # If no spam patterns are found, the message is considered normal
    return False
