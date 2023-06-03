import re

def is_spam(message: str) -> bool:
    """
    This function takes a message as an input and returns True if it is a spam message, otherwise returns False.
    """
    # Check for the existence of any URL or short links
    url_pattern = re.compile(r'https?://\S+|www\.\S+|me\d\.kr/\S+|bit\.ly/\S+')
    if url_pattern.search(message):
        return True

    # Check if the message contains specific spam-related keywords or patterns
    spam_keywords = [
        r'\b회원\b', r'\b광고\b', r'\b추천주\b', r'\b적중\b', r'\b다음주 종목\b',
        r'\b수익률\b', r'\b상담\b', r'\b무료거부\b', r'\b최소.*?보장\b',
        r'\b공시\b', r'\b원클릭\b', r'\b공개\b', r'\b매수\b', r'\b비번\b'
    ]
    for keyword in spam_keywords:
        if re.search(keyword, message):
            return True

    # If none of the conditions above are met, the message is not spam
    return False