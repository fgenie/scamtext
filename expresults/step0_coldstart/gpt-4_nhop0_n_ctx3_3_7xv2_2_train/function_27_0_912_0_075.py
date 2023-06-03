
import re

def is_spam(message):
    # Define common spam patterns and keywords
    spam_patterns = [
        r'[0-9]{3,}의길',
        r'[0-9]{1,6}[.,]\s*[0-9a-zA-Z]+',
        r'[0-9]+만|출금\w+만',
        r'[0-9]+%|콤[0-9.,]+%',
        r'https://kakaotalk\.[a-zA-Z]+/air',
        r'https://me2\.kr/[a-zA-Z0-9]+',
        r'[!,@,#,$,%,^,&,*,.,?][(a-zA-Z0-9)]+'
    ]

    # Check if message contains spam patterns
    for pattern in spam_patterns:
        if re.search(pattern, message):
            return True

    return False
