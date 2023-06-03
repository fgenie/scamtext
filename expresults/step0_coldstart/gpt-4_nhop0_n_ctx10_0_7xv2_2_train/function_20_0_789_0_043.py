def is_spam(message):
    import re
    
    keywords = ["광고", "me2.kr", "루징", "참가", "수익", "임대차동호", "체험반", "코드", "월요일부터 시장공략", "추천", "무료거부"]
    message = message.lower()

    if any(keyword in message for keyword in keywords):
        return True

    if re.search(r'https?://\S+', message):
        if re.search(r'(bit\.ly|han\.gl|opcn\-kakao\.com|\w+\.com/0)', message):
            return True
        
        if "(주)" in message or "KRW" in message:
            return True

    if re.search(r'\d{1,3}\,\d{3}원', message):
        return True

    if re.search(r'\+ ?\d{1,2}\D\d{1,3}\,\d{3}', message):
        return True

    return False