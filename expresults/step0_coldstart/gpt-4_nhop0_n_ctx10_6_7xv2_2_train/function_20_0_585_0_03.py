
import re

def is_spam(message):
    # Check for common spam phrases and patterns
    spam_phrases = ["무료거부", "적중", "수익 실현", "평균 수익", "추천주", "신규인원 모집", "카카오톡제재", "매수하시면", "이어서 공개", "악성광고"]
    url_shorteners = ["https://me2.kr", "https://vvd.bz", "https://openkakao.io"]
    
    # Check for excessive use of special characters
    special_chars = re.findall(r'[^a-zA-Z0-9가-힣\s]', message)
    if len(special_chars) / len(message) > 0.4:
        return True

    # Check for spam phrases in message
    for phrase in spam_phrases:
        if phrase in message:
            return True

    # Check for url shorteners in message
    for url_shortener in url_shorteners:
        if url_shortener in message:
            return True

    # If none of the above conditions are met, classify the message as normal (non-spam)
    return False
