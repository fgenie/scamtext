
import re

def is_spam(message):
    # Regular expression to detect spam patterns
    spam_patterns = [
        r'[ㄱ-ㅎ]+',
        r'[가-힣]+추천',
        r'광고[\s\S]*(t\.me|t\.ly)',
        r'알려드린',
        r'클릭',
        r'https://me2\.kr',
        r'교육방',
        r'1:1+교육',
        r'무료거부\d{10}',
        r'\d{1,2}日',
        r'기존',
        r'안전하고',
        r'해[-,.]?외[-,.]?선[-,.]?.?물[-,.]?[-,.]?',
        r'비밀번호[;,]:\d{4}'
    ]

    # Combine spam patterns into a single regular expression
    spam_regex = re.compile('|'.join(spam_patterns), re.IGNORECASE)

    # Check if the message matches any spam patterns
    if spam_regex.search(message):
        return True
    else:
        return False
