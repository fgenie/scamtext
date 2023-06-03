
import re

def is_spam(message):
    # Check for URL patterns
    url_pattern = re.compile(r'(http|https)://[^\s]*')
    url_match = url_pattern.search(message)
    
    # Check for presence of spammy keywords/phrases
    spam_keywords = ["(광고)", "긴급히", "빠른 확인", "증 권", "공시 종목", "상한가", "최대 상승률", "수익률 확정", "발표시", "성과", "자투리 조각구매", "조각구매"]

    # Count the number of spam keywords in the message
    spam_count = sum([1 for keyword in spam_keywords if keyword.lower() in message.lower()])

    # If the message has a URL and more than a threshold of spam keywords, classify it as spam
    if url_match and spam_count > 1:
        return True
    
    return False
