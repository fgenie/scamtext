
import re

def is_spam(text):
    # Check for common spam keywords
    spam_keywords = ['광고', '비트', '단타', '해선투자', '나스닥', '항샌', '매니저', '무료거부']
    for keyword in spam_keywords:
        if keyword in text:
            return True

    # Check for suspicious URLs
    url_pattern = re.compile(r'(https?|ftps?):\/\/[a-z0-9-]+(\.[a-z0-9-]+)*(\/\S*)?|(www\.)[a-z0-9]+(\.[a-z0-9]+)*(\/\S*)?')
    urls = url_pattern.findall(text)
    for url in urls:
        domain = url[0] + url[1]
        suspicious_domains = ['fastkakao', 'openkakao', 'ocx']
        for s_domain in suspicious_domains:
            if s_domain in domain:
                return True

    # Check for alphanumeric codes
    alphanumeric_pattern = re.compile(r'\d+[a-z]+|[a-z]+\d+')
    if alphanumeric_pattern.search(text):
        return True

    return False
