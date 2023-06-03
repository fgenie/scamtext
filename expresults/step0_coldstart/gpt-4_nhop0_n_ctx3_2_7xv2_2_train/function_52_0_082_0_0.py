
import re

def is_spam(message):
    # List of common keywords in spam messages
    spam_keywords = ['무료', '꼭 방문해주세요', '후회안합니다', '최고급 정보', '일체 비용없습니다', '상승 확정', '종목', '상승률', '입장링크']
    
    # Check for suspicious urls
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    suspicious_url = url_pattern.findall(message)
    
    # Check for excessive usage of special characters
    special_char_pattern = re.compile(r'[^a-zA-Z0-9가-힣\s]')
    special_chars = special_char_pattern.findall(message)
    
    spam_score = 0

    # Increment spam_score based on the presence of spam keywords
    for keyword in spam_keywords:
        if keyword in message:
            spam_score += 1

    # Increment spam_score based on the presence of suspicious urls
    if suspicious_url:
        spam_score += 1

    # Increment spam_score based on the excessive usage of special characters
    if len(special_chars) / len(message) > 0.2:
        spam_score += 1

    # If the spam_score is greater than or equal to 3, classify the message as spam
    if spam_score >= 3:
        return True
    else:
        return False
