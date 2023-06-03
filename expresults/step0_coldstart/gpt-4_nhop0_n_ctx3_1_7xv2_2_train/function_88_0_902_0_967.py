
import re

def is_spam(message: str) -> bool:
    # Check for common spam keywords
    spam_keywords = ['광고', '적립금', '무료거부', 'I노', '적립금', '선물매매', '현금', '대형', '추천주']
    if any(keyword in message for keyword in spam_keywords):
        return True

    # Check for URL shorteners
    url_shorteners = ['me2.kr', 't.ly', 'bit.ly', 'cutt.ly']
    for shortener in url_shorteners:
        if shortener in message:
            return True

    # Check for unusual letter cases and number usage
    pattern = r'[가-힇a-zA-Z0-9_]+'
    tokens = re.findall(pattern, message)
    count_alphanum = 0
    count_special = 0

    for token in tokens:
        if re.search('[a-zA-Z]', token) or re.search('[0-9]', token):
            count_alphanum += 1
        elif re.search('[가-힣]', token):
            count_special += 1

    if count_special > count_alphanum:
        return True

    return False
