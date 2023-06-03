
import re

def is_spam(message):
    # Patterns that can indicate spam
    patterns = [
        r'[0-9]{0,2}\([a-zA-Z가-힣][a-zA-Z가-힣]\)',  # matching formats like '24(월)' or '12(M)'
        r'[a-zA-Z0-9]+\.(kr|com)',                # matching url formats like 'abc.kr' or 'abc.com'
        r'https?://[^\s]+',                       # matching url formats like 'https://me2.kr/cax'
        r'월\s*[0-9]+\s*고정수입',                      # matching income-related messages
        r'\b[a-zA-Z]+\b\s?[0-9_가-힣]상장',          # matching company-related messages
    ]

    for pattern in patterns:
        if re.search(pattern, message):
            return True
            
    return False
