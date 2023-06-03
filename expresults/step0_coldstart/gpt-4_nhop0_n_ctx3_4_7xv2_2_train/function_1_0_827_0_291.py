
import re

def is_spam(message):
    # Heuristic 1: Check for presence of URLs
    url_regex = r'(https?://\S+|www\.\S+|me2\.kr/\w+)'
    urls = re.findall(url_regex, message)

    # Heuristic 2: Check for use of special characters or non-alphanumeric
    non_alphanumeric_ratio = sum([not c.isalnum() for c in message]) / len(message)

    # Heuristic 3: Check for words related to money or exclusive offers
    money_words = ['투자반', '추천', '실력으로 입증', '체험반', '정보', '무료']
    money_words_count = sum([word in message for word in money_words])

    # Heuristic 4: Check for words related to urgency
    urgency_words = ['금일', '긴급', '시작', '차별화', '오파스넷', '축하', 'FROG']
    urgency_words_count = sum([word in message for word in urgency_words])

    # Combining heuristics
    if len(urls) > 0 or non_alphanumeric_ratio > 0.3 or money_words_count > 1 or urgency_words_count > 0:
        return True

    return False
