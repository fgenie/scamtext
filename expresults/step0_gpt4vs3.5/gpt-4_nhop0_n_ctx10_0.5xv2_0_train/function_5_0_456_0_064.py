
import re

def is_spam(message):
    common_spam_keywords = [
        '가입축하', '배당종류', '대환허', '상한가', '추천주', '당일출금', '이벤트', '들어오세요', '할인',
        '바로가기', '무제한', '지급', '최고', '공개', '순매수', '공짜', 'SMS', '광고',
        '혜택', '당장', 'VIP', '인터넷게임', '텔레그램', '식약처',
    ]

    spam_keyword_pattern = re.compile("|".join(common_spam_keywords), re.IGNORECASE)
    message_no_url = re.sub(r'http\S+', '', message)

    spam_score = 0
    if spam_keyword_pattern.search(message_no_url):
        spam_score += 1

    excess_punctuation = re.findall(r'[^\w\s\.,]', message_no_url)
    if len(excess_punctuation) >= 3:
        spam_score += 1

    decimal_symbols = re.findall(r'\d+', message_no_url)
    if len(decimal_symbols) >= 3:
        spam_score += 1

    return spam_score >= 2
