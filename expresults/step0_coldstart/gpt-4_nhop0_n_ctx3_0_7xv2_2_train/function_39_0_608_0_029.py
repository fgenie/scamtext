
import re

def is_spam(text):
    # Check for common spam phrases in the text
    spam_phrases = ['목표달성기념', '美FDA승인', '정부', '추천', '종목']
    for phrase in spam_phrases:
        if phrase in text:
            return True

    # Check for suspicious URLs
    url_regex = re.compile(r'(http|https)://\S+')
    if url_regex.search(text):
        short_url_domains = ['me2.kr']
        url = url_regex.search(text).group(0)
        domain = re.search(r'(http|https)://([\w.-]+)', url).group(2)
        if domain in short_url_domains:
            return True

    # Check for excessive use of special characters or digits
    special_characters = re.findall(r'[^a-zA-Z0-9가-힣]+', text)
    text_length = len(text)
    if len(special_characters) / text_length > 0.5:
        return True

    return False
