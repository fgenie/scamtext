
import re

def is_spam(message):
    # Detect shortened URL patterns
    short_url_patterns = [
        r'bit\.ly',
        r'gg\.gg',
        r'opcn-kakao\.com',
        r'http[s]?://'
    ]

    # Detect advertising and promotion keywords
    spam_keywords = [
        r'\(광고\)',
        r'스닥',
        r'고수익',
        r'Vip방',
        r'상담환영',
        r'무료거부',
        r'급등예정',
        r'진입시점제공',
        r'HTS/MTS'
    ]

    short_url_regex = '|'.join(short_url_patterns)
    spam_keyword_regex = '|'.join(spam_keywords)

    if re.search(short_url_regex, message) or re.search(spam_keyword_regex, message):
        return True
    else:
        return False
