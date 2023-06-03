
import re

def is_spam(message):
    # Check for keywords related to spam messages
    spam_keywords = ['광고', '공짜', '바로가기', 'VIP', '투자', '추천', '%', '이유불문', '결과로', '만원', '보상', '약속', '클릭', '무료']

    # Check for presence of URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_url = bool(url_pattern.search(message))

    # Check for the presence of spam keywords and URLs
    if has_url or any(keyword in message for keyword in spam_keywords):
        return True
    else:
        return False
