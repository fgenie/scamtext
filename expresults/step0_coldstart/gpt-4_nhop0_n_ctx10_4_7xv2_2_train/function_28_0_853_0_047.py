
import re

def is_spam(message):
    keywords = ['상한가', '추천주', '투자정보', '종목', '체험반', '단투', 'vip', '4월', '매수', '차트', '증권']

    spam_phrase_count = 0
    words_list = re.findall(r'\w+', message.lower())

    # Check if keywords are part of the content
    for keyword in keywords:
        if keyword.lower() in words_list:
            spam_phrase_count += 1

    # Check for too many spam words
    if spam_phrase_count >= 2:
        return True

    # Check for non-normal URL formats (like me2.kr)
    url_patterns = re.findall(r'(https?://)?(www\.)?(\w+\.\w+)', message)
    for url_group in url_patterns:
        url = url_group[2]
        if not re.match(r'^(?:[a-z]+\.)+(?:com|org|gov|mil|edu|co\.kr)$', url):
            return True

    return False
