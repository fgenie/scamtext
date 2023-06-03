
import re

def is_spam(message):
    # Check for suspicious keywords
    spam_keywords = ['광고', '계약', '상한가', '바쁜 시간', '매수', '수익', '빠르게', '성과', '차트', '비밀 종목', '오늘 공개', '진입', '골드해선', '체험반', '비용 없습니다']
    for keyword in spam_keywords:
        if keyword in message:
            return True

    # Check for excess of numbers and special characters in message
    numbers_special_chars = re.findall(r'\d|[!#$%&()*+,-./:;<=>?@[\]^_`{|}~]', message)
    if len(numbers_special_chars) / len(message) > 0.2:
        return True

    # Check for presence of urls
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message)
    if len(urls) > 0:
        return True

    # If none of the conditions above are met, the message is considered normal
    return False
