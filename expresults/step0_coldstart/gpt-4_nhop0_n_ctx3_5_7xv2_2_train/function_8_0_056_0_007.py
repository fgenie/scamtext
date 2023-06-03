import re

def is_spam(text: str) -> bool:
    # Check if the message contains a suspicious URL
    url_pattern = re.compile(r'(http(s)?|kakaotalk)\:\/\/([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?')
    urls = url_pattern.findall(text)
    if urls:
        for url in urls:
            suspicious_keywords = ['bit.ly', 'kakaotalk.it', 'openkakao.at']
            if any(keyword in url for keyword in suspicious_keywords):
                return True

    # Check if the message contains a suspicious content, i.e., 일자, 수익률, 목표가
    spam_keywords = ['일자', '수익률', '목표가']
    if any(keyword in text for keyword in spam_keywords):
        return True

    return False