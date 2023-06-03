def is_spam(text):
    spam_keywords = ["추천", "종목", "상승", "신청하신", "방 입장", "%↑", "http", "https", "io", "kr", "kakaotalk.it", "me2.kr", "openkakao.io"]

    text_lower = text.lower()
    for keyword in spam_keywords:
        if keyword in text_lower:
            return True
    return False