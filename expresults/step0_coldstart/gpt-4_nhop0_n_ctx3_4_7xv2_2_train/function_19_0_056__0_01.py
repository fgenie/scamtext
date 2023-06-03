
import re

def is_spam(message):
    spam_phrases = [
        r'(목표달성기념)',
        r'(추천 디젠스)',
        r'(고객님께서 요청하신 해외선물 VIP정보방)',
        r'(빠른입장)',
        r'(코/드 :)',
        r'(토토가)',
        r'(?<!\S)(\d{1,})\+(\d{1,})(?!\S)'
    ]

    url_regex = r'((http|https):\/\/)?(www.)?([a-zA-Z0-9]|-|_)+(\.[a-zA-Z]{2,})+(\/[\w\?=#!_%&-]+)*(?<!\.)'
    url_shortener_keywords = [
        r'(bit\.ly)',
        r'(me2\.kr)'
    ]

    for phrase in spam_phrases:
        if re.search(phrase, message):
            return True

    urls = re.findall(url_regex, message)
    for url in urls:
        for keyword in url_shortener_keywords:
            if re.search(keyword, url[0]):
                return True

    return False
