
import re

def is_spam(message):
    # Check for common spam keywords and patterns
    spam_keywords = ["광고", "무료", "배달", "상한가", "수익", "프로모션", "추천", "적중", "할인", "선착순", "차익", "소득", "개설", "열립니다", "안내입", "공유", "입장", "연락", "투자", "공개론"]

    message_clean = re.sub("[^가-힣0-9\s]", "", message)
    message_lower = message_clean.lower()
    message_words = message_lower.split(" ")

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in message_words:
            return True
            
    # Check for multiple links
    links = re.findall("(https?://[^\s]+)", message)
    if len(links) > 1:
        return True

    # Check for sequential numbers
    if re.search(r"(\d)\1{2,}", message):
        return True

    return False
