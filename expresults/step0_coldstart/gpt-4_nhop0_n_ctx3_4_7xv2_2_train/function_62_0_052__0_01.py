
import re

def is_spam(text):
    spam_keywords = ['무료', '체험반', '지니틱스', '카카오톡제재', '핵심정보', '악성광고', '텔레그램', 'Vip']
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    spam_score = 0

    for keyword in spam_keywords:
        if keyword in text:
            spam_score += 1

    if url_pattern.search(text):
        spam_score += 1

    return spam_score > 2
