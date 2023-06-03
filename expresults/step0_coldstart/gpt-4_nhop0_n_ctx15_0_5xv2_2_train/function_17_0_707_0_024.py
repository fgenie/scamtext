
import re

def is_spam(text):
    spam_keywords = ['늘릴', '상한가', '상승 예정', '대량 매집', '%$']
    spam_phrases = ['무료 참여 링크', '추천주', '주식정보', '투자정보', '광고']

    text = text.lower()

    # Check for presence of spam keywords
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for presence of spam phrases
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check if message contains any urls
    url_pattern = re.compile("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    urls = re.findall(url_pattern, text)
    if len(urls) > 0:
        return True

    return False
