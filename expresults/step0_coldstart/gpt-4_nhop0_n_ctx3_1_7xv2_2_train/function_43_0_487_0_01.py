
import re

def is_spam(text: str) -> bool:
    spam_keywords = ['목표달성', '추천', '체험반', '공시발표', '정회원방', '단독입수']
    has_spam_keyword = any([keyword in text for keyword in spam_keywords])

    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    has_url = bool(url_pattern.search(text))

    offer_pattern = re.compile(r'상승|시작|입장')
    has_offer = bool(offer_pattern.search(text))

    return has_spam_keyword or (has_url and has_offer)

