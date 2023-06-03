
import re

def is_spam(message):
    # Check for common spam words in the message
    spam_words = ['천만원', '성공을 위한', '부자', '프로젝트', '축하합니다', '당첨', '실력', '적중']
    for word in spam_words:
        if word in message:
            return True

    # Check for urls containing suspicious parts
    url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls = url_pattern.findall(message)
    spam_url_parts = ['me2.kr', 'han.gl', '/CnGWF', 'CKuVQZ', '5Dg88']
    for url in urls:
        for part in spam_url_parts:
            if part in url:
                return True

    return False
